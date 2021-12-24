import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)


