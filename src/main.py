from file_recognition import audio_file_to_text

def main():
    audio_path = "audio\sample1.wav"

    print("🎧 Processing audio file...")
    result = audio_file_to_text(audio_path)

    print("📝 Transcribed Text:")
    print(result)

if __name__ == "__main__":
    main()

#python src\main.py