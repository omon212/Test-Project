from gtts import gTTS
import os
import chardet

text = "hello"
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")
os.system("start output.mp3")
