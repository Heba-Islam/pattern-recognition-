import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something!")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio)

print(text)