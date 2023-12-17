from flask import Flask, jsonify  # , request, render_template, redirect
from whisper_ai import TranscribeAudio


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


@app.route('/whisper_ai', methods=['GET'])
def whisper_ai():
    transcription = TranscribeAudio().output()['text']
    return transcription


if __name__ == '__main__':
    app.run(port=5000, debug=True)
