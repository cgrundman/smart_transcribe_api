# import json
from flask import Flask, jsonify  # , request, render_template, redirect
import whisper_ai
import whisper_timestamped as whisper
import os
from scipy.io import wavfile

# app = Flask(__name__)
#
# employees = [{'id': 1, 'name': 'Ashley'},
#              {'id': 2, 'name': 'Kate'},
#              {'id': 3, 'name': 'Joe'}]
#
# things = [{'id': 1, 'name': 'Banana'},
#           {'id': 2, 'name': 'Apple'},
#           {'id': 3, 'name': 'Pear'}]
#
#
# @app.route('/employees', methods=['GET'])
# def get_employees():
#     return jsonify(employees)
#
#
# @app.route('/ai', methods=['GET'])
# def ai_output():
#     return "Hello, I am your AI."  # TODO (simple example from ai model)
#
#
# if __name__ == '__main__':
#     app.run(port=5000, debug=True)

# help(whisper.load_audio)
samplerate, data = wavfile.read("./audio/words.wav")

# whisper_ai.ai_output()
