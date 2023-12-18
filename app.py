from flask import Flask, jsonify, render_template

import whisper_timestamped as whisper

from transformers import pipeline


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
    return render_template("index.html", files=audio_files, num_files=len(audio_files))


# Transcription page - displays transcription of selected sound file
@app.route('/transcribe/<int:file>', methods=['GET'])
def transcription(file):
    # Load the whisper_timestamped model
    model = whisper.load_model("tiny", device="cpu")

    # Pass the audio file and the language into the model, save the output
    audio_transcript = whisper.transcribe(model=model, audio=audio_files[file]['file'], language=audio_files[file]['language'])

    # Add text output from model into the audio file dictionary
    audio_files[file]['text'] = audio_transcript['text']

    return render_template("transcribe.html",
                           text=audio_files[file]['text'],
                           file=audio_files[file]['file'][8:],
                           file_idx=file)


# Analysis page - displays sentiment analysis of transcription
@app.route('/transcribe/<int:file>/analyze', methods=['GET'])
def analysis(file):
    # Split full transcript into a list of sentences
    transcript_list = audio_files[file]['text'].split(".")

    # Assert the list as a string and add into the dictionary
    audio_files[file]['sentence_list'] = str(transcript_list)

    # Load the hugging face model for sentiment analysis
    sentiment_pipeline = pipeline("sentiment-analysis")

    # Pass the sentence list into the hugging face model, analyze on a sentence by sentence basis
    analysis = sentiment_pipeline(transcript_list)

    # Save sentiments into dictionary
    audio_files[file]['sentiment'] = str(analysis)

    return render_template("analyze.html",
                           transcript=audio_files[file]['sentence_list'],
                           analysis=audio_files[file]['sentiment'],
                           file=audio_files[file]['file'][8:],
                           file_idx=file)


# TODO add a third route for a third ai


if __name__ == '__main__':
    app.run(port=5000, debug=True)


