import argparse

import Openai_Api_V2 as cb
import vito_stt_streaming_V4 as stt

myCommands = [
    "날씨",
    "파이썬"
]

def Command(self, request):
    if check_substrings(myCommands, request):
        return
    else:
        chatbot.converse(request)

def check_substrings(string, substrings):
    for substring in substrings:
        if substring in string:
            return True
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    args = parser.parse_args()

    config = stt.pb.DecoderConfig(
        sample_rate=stt.SAMPLE_RATE,
        encoding=stt.ENCODING,
        use_itn=True,
        use_disfluency_filter=True,
        use_profanity_filter=False,
    )

    chatbot = cb.Chatbot()
    client = stt.VITOOpenAPIClient(stt.CLIENT_ID, stt.CLIENT_SECRET)

    client.transcribe_streaming_grpc(None, config)
