import os

import anthropic
from flask import Flask, jsonify, request  # , render_template, redirect

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


@app.route("/completion", methods=['POST'])
def completion():
    data = request.get_json()  # Get the JSON data from request
    title = data.get('title')
    sections = data.get('sections')

    prompt = (f"{anthropic.HUMAN_PROMPT} I need your help to collaboratively write an article. The article has a "
              f"title and several sections."
              f"I will provide you with the title and the contents of the sections, and I want you to help me improve "
              f"them."
              f"Your improvements should focus on enhancing the readability, correcting any grammatical errors, "
              f"and improving the writing style while keeping the original meaning and intent of the text intact."
              f"Feel free to expand and develop the writing while maintaining coherence of the overall writing."
              f"Please also ensure that the content generated is safe and free from harmful contents such as "
              f"violence, sex, swear words, hate speech, and warmongering."
              f"Finally, please use markdown to write your revision, so I can render it on my user interface."
              f"{anthropic.AI_PROMPT} Understood, I will assist you in improving the provided text while ensuring the "
              f"content safety."
              f"{anthropic.HUMAN_PROMPT} Great, here is the title and the sections for you to revise. The title is {title}")

    for i, section in enumerate(sections):
        prompt += f"; Next section - title: {section['title']}; section content: {section['content']}"

    c = anthropic.Client(os.getenv("CLAUDE_KEY"))
    resp = c.completion(
        prompt=f"{prompt} {anthropic.AI_PROMPT}",
        stop_sequences=[anthropic.HUMAN_PROMPT],
        model="claude-v1.3-100k",
        max_tokens_to_sample=1500,
    )
    return resp


if __name__ == '__main__':
    app.run(port=5000, debug=True)
