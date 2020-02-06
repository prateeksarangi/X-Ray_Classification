from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    """if request.method == 'POST':
        file = request.files['inputFile']
        return file.filename"""
    return render_template('index.html')

app.run(debug=True)