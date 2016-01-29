__author__ = 'root'

import os
from flask import Flask, jsonify,request, redirect, url_for
from flask import Response
from textblob import TextBlob
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/list')

def api_articles():
    return 'List of ' + url_for('api_articles')


UPLOAD_FOLDER = '/home/serendio/Desktop/textblob'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    print " Welcome"
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/home/serendio/Desktop/textblob', methods=['POSt'])
def upload_file():
    print " Welcome further"
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file))

           # return redirect(url_for('tt.txt',
                                    filename=file))

            ##read the file n all like f.read() stuff
    return "Done"



@app.route('/home/serendio/Desktop/textblob/<tt>',methods=['GET'])
def sentiment(tt):
    if request.method == 'GET':
        print " Welcome last"
        text = TextBlob(tt)
        response = {'polarity' : text.polarity , 'subjectivity' : text.subjectivity}
    return "Done Again ",jsonify(response)



# file=open("1.txt")
# t=file.read()
# print(type(t))
# testimonial = TextBlob("t")
# c=testimonial.sentiment
# print c


if __name__ == '__main__':
    app.run(debug=True,port=2110)