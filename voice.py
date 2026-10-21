import sounddevice as sd
import speech_recognition as sr

recognizer = sr.Recognizer()
SAMPLE_RATE = 16000
SECONDS = 4

def listen():
    try:
        print(f"Listening for {SECONDS} seconds... speak now")
        with sd.RawInputStream(samplerate=SAMPLE_RATE, channels=1, dtype="int16") as stream:
            data, _ = stream.read(SAMPLE_RATE * SECONDS)
        audio = sr.AudioData(bytes(data), SAMPLE_RATE, 2)
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Speech service not reachable. Check your internet.")
    except Exception as e:
        print("Microphone problem:", e)
    return ""