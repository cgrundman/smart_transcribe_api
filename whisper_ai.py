import whisper_timestamped as whisper


class TranscribeAudio:
    def __init__(self):
        # Test Audio Files
        # audio, language = whisper.load_audio("./audio/words.wav"), "fr"
        self.audio, self.language = whisper.load_audio("./audio/gloria.mp3"), "en"

    def output(self):
        # Test Audio Files
        # audio, language = whisper.load_audio("./audio/words.wav"), "fr"
        # audio, language = whisper.load_audio("./audio/gloria.mp3"), "en"

        model = whisper.load_model("tiny", device="cpu")

        result = whisper.transcribe(model, self.audio, language=self.language)

        return result
