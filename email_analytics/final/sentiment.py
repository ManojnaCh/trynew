
from flask import Flask, url_for,request,jsonify

from textblob import TextBlob
app = Flask(__name__)

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<mesage>',methods=['GET'])
def api_article(message):
    if request.method == 'GET':
        text = TextBlob(message)
        response = {'polarity' : text.polarity , 'subjectivity' : text.subjectivity}
    return jsonify(response)

@app.route('/sentiments',methods=['POST'])
def api_sentiment():
    if request.method == 'POST':
        text = request.form['text']
        result = TextBlob(text)
        response = {'polarity' : result.polarity , 'subjectivity' : result.subjectivity}
    return jsonify(response)


if __name__ == '__main__':
   app.run(port=3501)
