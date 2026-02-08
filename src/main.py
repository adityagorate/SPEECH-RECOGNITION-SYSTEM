from file_recognition import audio_file_to_text    # import function

def main():
    audio_path = "audio\sample1.wav"  # audio file path

    print("🎧 Processing audio file...")    # processing message
    result = audio_file_to_text(audio_path)    # convert audio to text

    print("📝 Transcribed Text:")    # output heading
    print(result)      # print result

if __name__ == "__main__":         # program start point
    main()

