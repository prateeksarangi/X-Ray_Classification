import os
from flask import Flask, render_template, request, url_for
from ServerSide import predict_class

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['images']
        path = os.getcwd()+'/static/profile_pics/'+file.filename
        file.save(path)
        #print('PATH: {}'.format(path))
        image_file = url_for('static', filename='profile_pics/' + file.filename)
        output = predict_class(path)
        #print(output)
        if output[0][0]==1:
            labelans="Normal"
        else:
            labelans="Pneumonia"
        return render_template('index.html',predict=labelans,image_file=image_file)

app.run(debug=True)
