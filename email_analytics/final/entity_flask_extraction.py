__author__ = 'root'

import nltk
from flask import Flask, url_for,request,jsonify
app = Flask(__name__)


def meenu(text):
    if request.method == 'GET':
        tokens = nltk.word_tokenize(text)
        print tokens
        tagged = nltk.pos_tag(tokens)
        print tagged[0:6]
        entities = nltk.chunk.ne_chunk(tagged)
        response = {'entities':entities}
    return jsonify(response)


@app.route('/<message>', methods=['GET'])
def entities(message):
    output = meenu(message)
    return output

if __name__ == '__main__':
    app.run(debug=True,port=1000)


