from flask import Flask, jsonify

from whisper_ai import TranscribeAudio

from transformers import pipeline


app = Flask(__name__)

employees = [{'id': 1, 'name': 'Ashley'},
             {'id': 2, 'name': 'Kate'},
             {'id': 3, 'name': 'Joe'}]

things = [{'id': 1, 'name': 'Banana'},
          {'id': 2, 'name': 'Apple'},
          {'id': 3, 'name': 'Pear'}]


@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)


@app.route('/', methods=['GET'])
def sentiment():
    sentiment_pipeline = pipeline("sentiment-analysis")
    transcription = TranscribeAudio().output()['text']
    transcript_list = transcription.split(".")
    # data = ["I love you", "I hate you"]
    analysis = sentiment_pipeline(transcript_list)
    for idx in range(len(analysis)):
        analysis[idx]['value'] = transcript_list[idx]
    return analysis


if __name__ == '__main__':
    app.run(port=5000, debug=True)


