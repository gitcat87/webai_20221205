from gtts import gTTS

tts = gTTS(text='안녕하세요',lang='ko')
tts.save('hi_ko.mp3')

tts = gTTS(text='날씨정보를 불러왔습니다',lang='ko')
tts.save('hi_weather.mp3')

import playsound
import threading

def dohi():
    playsound.playsound('hi_ko.mp3')
def dowea():
    playsound.playsound('hi_weather.mp3')

t1 = threading.Thread(target=dohi)
t2 = threading.Thread(target=dowea)
t1.start()
import time
if t1.join():