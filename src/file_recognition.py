import speech_recognition as sr

def audio_file_to_text(file_path):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        return "Error: Could not understand the audio"

    except sr.RequestError:
        return "Error: Speech Recognition service unavailable"

    except FileNotFoundError:
        return "Error: Audio file not found"