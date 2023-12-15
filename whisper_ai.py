import whisper_timestamped as whisper
import json


def ai_output():
    audio = whisper.load_audio("AUDIO.wav")

    model = whisper.load_model("tiny", device="cpu")

    result = whisper.transcribe(model, audio, language="fr")

    return print(json.dumps(result, indent=2, ensure_ascii=False))


help(whisper.transcribe)
