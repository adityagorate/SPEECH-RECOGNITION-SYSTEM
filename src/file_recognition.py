import speech_recognition as sr    # import library

def audio_file_to_text(file_path):
    recognizer = sr.Recognizer()        # create recognizer object

    try:
        with sr.AudioFile(file_path) as source:      # open audio file
            audio = recognizer.record(source)      # read audio data

        text = recognizer.recognize_google(audio)    # convert speech to text
        return text       # return result

    except sr.UnknownValueError:
        return "Error: Could not understand the audio"      # audio not clear

    except sr.RequestError:
        return "Error: Speech Recognition service unavailable"         # API issue

    except FileNotFoundError:

        return "Error: Audio file not found"   # file missing
