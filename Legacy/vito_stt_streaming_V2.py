import argparse
import logging
import time
from io import DEFAULT_BUFFER_SIZE

import grpc
import vito_stt_client_pb2 as pb
import vito_stt_client_pb2_grpc as pb_grpc
from requests import Session
import pyaudio
import subprocess
import multiprocessing as mp
import os
import Privates

API_BASE = "https://openapi.vito.ai"
GRPC_SERVER_URL = "grpc-openapi.vito.ai:443"
CLIENT_ID = Privates.CLIENT_ID
CLIENT_SECRET = Privates.CLIENT_SECRET

SAMPLE_RATE = 8000
ENCODING = pb.DecoderConfig.AudioEncoding.LINEAR16

cmd = 'python Openai_Api_V2.py'

class VITOOpenAPIClient:
    def __init__(self, client_id, client_secret):
        super().__init__()
        self._logger = logging.getLogger(__name__)
        self.client_id = client_id
        self.client_secret = client_secret
        self._sess = Session()
        self._token = None

    @property
    def token(self):
        if self._token is None or self._token["expire_at"] < time.time():
            resp = self._sess.post(
                API_BASE + "/v1/authenticate",
                data={"client_id": self.client_id, "client_secret": self.client_secret},
            )
            resp.raise_for_status()
            self._token = resp.json()
        return self._token["access_token"]

    def transcribe_streaming_grpc(self, stream, config):
        base = GRPC_SERVER_URL
        with grpc.secure_channel(
            base, credentials=grpc.ssl_channel_credentials()
        ) as channel:
            stub = pb_grpc.OnlineDecoderStub(channel)
            cred = grpc.access_token_call_credentials(self.token)

            def req_iterator():
                yield pb.DecoderRequest(streaming_config=config)

                # Initialize PyAudio
                p = pyaudio.PyAudio()
                stream = p.open(format=pyaudio.paInt16, channels=1, rate=SAMPLE_RATE, input=True,
                                frames_per_buffer=DEFAULT_BUFFER_SIZE)

                while True:
                    buff = stream.read(DEFAULT_BUFFER_SIZE)
                    if len(buff) == 0:
                        break
                    yield pb.DecoderRequest(audio_content=buff)

                # Stop the stream
                stream.stop_stream()
                stream.close()
                p.terminate()

            req_iter = req_iterator()
            resp_iter = stub.Decode(req_iter, credentials=cred)
            for resp in resp_iter:
                resp: pb.DecoderResponse
                for res in resp.results:
                    if res.is_final:
                        print(res.alternatives[0].text)
                        # Create a new process to execute the command
                        p = mp.Process(target=self.execute_command, args=(cmd, res.alternatives[0].text))
                        p.start()

    @staticmethod
    def execute_command(cmd):
        subprocess.run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    args = parser.parse_args()

    config = pb.DecoderConfig(
        sample_rate=SAMPLE_RATE,
        encoding=ENCODING,
        use_itn=True,
        use_disfluency_filter=True,
        use_profanity_filter=False,
    )

    client = VITOOpenAPIClient(CLIENT_ID, CLIENT_SECRET)
    client.transcribe_streaming_grpc(None, config)
