__author__ = 'root'

import nltk
from flask import Flask,request,jsonify
app = Flask(__name__)

def meenu(text):
    def extract_entity_names(t):
        print "got into extract"
        if hasattr(t, 'label') and t.label:
            if t.label() == 'NE':
                entity_names.append(' '.join([child[0] for child in t]))
            else:
                for child in t:
                    entity_names.extend(extract_entity_names(child))
        return entity_names
    print "Got into meenu"
    sentences = nltk.sent_tokenize(text)
    print sentences
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.chunk.ne_chunk_sents(tagged_sentences,binary=True)
    entity_names = []
    for tree in chunked_sentences:
        print "got into tree"
        entity_names.extend(extract_entity_names(tree))
    response = set(entity_names)
    print set(entity_names)
    return jsonify(output=str(response))
    # return ','.join(response)
    # return jsonify({'entity_name_output':response})




@app.route('/<message>', methods=['GET'])
def entities(message):
    print "got into entities"
    output = meenu(message)
    return output
if __name__ == '__main__':
    app.run(debug=True,port=2080)

