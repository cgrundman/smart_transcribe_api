from flask import Flask, jsonify, render_template

import whisper_timestamped as whisper

from transformers import pipeline


# TODO add comments to all code files
app = Flask(__name__)


# TODO add more files
# List of all available audio files to transcribe
audio_files = [{'file': "./audio/bonjour.wav",
                'language': "fr"},
               {'file': "./audio/smartphone.mp3",
                'language': "fr"},
               {'file': "./audio/gloria.mp3",
                'language': "en"}]


# TODO automate routing
# Home page - displays sound file options for transcribing
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


# Transcription page - displays transcription of selected sound file
@app.route('/transcribe/<int:file>', methods=['GET'])
def transcription(file):
    model = whisper.load_model("tiny", device="cpu")
    text = whisper.transcribe(model=model, audio=str(audio_files[file]['file']), language=audio_files[file]['language'])
    # return render_template("transcribe.html", text=text['text'])
    return render_template("transcribe.html", text=text['text'], file=file), text


# Analysis page - displays sentiment analysis of transcription
@app.route('/transcribe/<int:file>/analyze', methods=['GET'])
def analysis(file, text):
    # transcript_list = text.split(".")
    # sentiment_pipeline = pipeline("sentiment-analysis")
    # analysis = sentiment_pipeline(transcript_list)
    return render_template("analyze.html", analysis=text, file=audio_files[file]['file'][8:])


# TODO split into two routes, one for each ai
# @app.route('/sentimate', methods=['GET'])
# def sentiment():
#     sentiment_pipeline = pipeline("sentiment-analysis")
#     transcription = whisper_ai.output()['text']
#     transcript_list = transcription.split(".")
#     analysis = sentiment_pipeline(transcript_list)
#     for idx in range(len(analysis)):
#         analysis[idx]['value'] = transcript_list[idx]
#     return analysis


# TODO add a third route for a third ai


if __name__ == '__main__':
    app.run(port=5000, debug=True)


