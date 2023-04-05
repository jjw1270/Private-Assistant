import pyttsx3

# 1. HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0

engine = pyttsx3.init()

#print(engine.getProperty('rate')) #default rate = 200
# print(engine.getProperty('voice')) 
# print(engine.getProperty('voices'))

voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   print(engine.getProperty('voice')) 
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()