import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, flash
from ServerSide import predict_class

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    result=db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return f"User('{self.pname}', '{self.gender}', '{self.age}','{self.result}')"
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dname = db.Column(db.String(20), nullable=False)
    did = db.Column(db.Integer, nullable=False)
    dno = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Doctor('{self.dname}', '{self.did}', '{self.dno}')"
db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['images']
        path = os.getcwd()+'/static/tempdata/'+file.filename
        file.save(path)
        image_file = url_for('static', filename='tempdata/' + file.filename)
        output = predict_class(path)
        if output[0][0] == 1:
            labelans = "Normal"
        else:
            labelans = "Pneumonia"
        user1 = User(pname=request.form['name'], gender=request.form['gender'], age=request.form['age'], result=labelans)
        db.session.add(user1)
        db.session.commit()
        doctor1 = Doctor(dname=request.form['d_name'], did=request.form['d_id'], dno=request.form['d_mob'])
        db.session.add(doctor1)
        db.session.commit()
        return render_template('index.html',predict=labelans,image_file=image_file,pname=user1.pname,gender=user1.gender,age=user1.age,dname=doctor1.dname,dno=doctor1.dno,did=doctor1.did)

if __name__ == '__main__':
    app.run(debug=True)

