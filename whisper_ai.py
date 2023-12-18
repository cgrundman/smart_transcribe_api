import whisper_timestamped as whisper


def output(self):
    # Test Audio Files
    # audio, language = whisper.load_audio("./audio/words.wav"), "fr"
    # audio, language = whisper.load_audio("./audio/gloria.mp3"), "en"

    model = whisper.load_model("tiny", device="cpu")

    result = whisper.transcribe(model, self.audio, language=self.language)

    return result
