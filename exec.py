import os

from flask import *
from ServerSide import predict_class

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['inputFile']
        path = os.getcwd()+'/uploads/'+file.filename
        file.save(path)
        print('PATH: {}'.format(path))
        output=predict_class(path)
        print('OUTPUT: {}'.format(output))
        return render_template('index.html',predict=output)

app.run(debug=True)