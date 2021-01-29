import speech_recognition as sr

def stt_with_ambient(filename):
    r = sr.Recognizer()
    file = sr.AudioFile(filename)
    with file as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    return r.recognize_google(audio)