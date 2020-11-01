import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
with mic as source:
    print("Start speaking") 
    audio = r.listen(source)
    print("Recording complete") 
result = r.recognize_google(audio, language = 'en-US', show_all=True)
print(result)
