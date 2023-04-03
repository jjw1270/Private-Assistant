# Private-Assistant
 stt,tts,ai를 이용한 개인비서(비 상업용)

## Installation
 두 가지 방법이 있습니다. (가상 환경(권장), 일반)
 
 1. 가상 환경에 설치
 
  설치 폴더에서 cmd 진입
  
    py -3 -m venv env
  
    env\Scripts\activate.bat
  
    pip install -r requirements.txt
  
 2. 일반 설치

  설치 폴더에서 cmd 진입
  
    pip install -r requirements.txt

## 필수 작업
 - Vito api키는 https://developers.vito.ai/ 에서 발급
 - Openai api키는 https://openai.com/product#made-for-developers 에서 발급

  1. 메모장을 열어 아래 코드 입력
  
         #Vito API
         CLIENT_ID = ""
         CLIENT_SECRET = ""

         #Openai API
         api_key = ""
  2. ""안에 발급받은 api키 입력
  3. Privates.py 이름으로 저장
    
## 실행 방법
 1. 설치 폴더에서 cmd 진입
 2. Installation의 작업 진행
 3. 다음 명령어 입력 : python vito_stt_streaming_V6.py
 4. Start Now! 가 출력되면 음성인식 가능합니다.
