# Private-Assistant
 stt,tts,ai를 이용한 개인비서(비상업용)

## Installation
 두 가지 방법이 있습니다. (가상 환경(권장), 일반)
 
 1. 가상 환경에 설치
  설치 폴더에서 cmd 진입
  
  py -3 -m venv env
  
  env\Scripts\activate.bat
  
  pip install -r requirements.txt
  
 2. 일반 설치
  설치 폴던에서 cmd 진입
  
  pip install -r requirements.txt

## 필수 작업
 - Vito api키는 https://developers.vito.ai/ 에서 발급
 - Openai api키는 https://openai.com/product#made-for-developers 에서 발급

 설치 폴더에 Privates.py 파일을 만든다.'
 아래 명령어들을 복사 붙여넣기

################################################
 #Vito API
 CLIENT_ID = "Input Your Client ID"
 CLIENT_SECRET = "Input Your Client Secret"

 #Openai API
 api_key = "Input Your Api Key"
#################################################

## 실행 방법
 1. 설치 폴더에서 cmd 진입
 2. Installation의 작업 진행
 3. 다음 명령어 입력 : python vito_stt_streaming_V6.py
 4. Start Now! 가 출력되면 음성인식 가능합니다.