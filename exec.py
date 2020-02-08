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
    dno = db.Column(db.Integer, nullable=False)
    did = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Doctor('{self.dname}', '{self.dno}', '{self.did}')"
db.create_all()

#output=[[1]]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
    	file = request.files['images']
    	path = os.getcwd()+'/static/profile_pics/'+file.filename
    	file.save(path)
    	print('PATH: {}'.format(path))
    	print(request.form['name'])
    	image_file = url_for('static', filename='profile_pics/' + file.filename)
    	output=predict_class(path)
    	if output[0][0]==1:
    		labelans="Normal"
    	else:
    		labelans="Pneumonia"
    	user1 = User(pname=request.form['name'], gender=request.form['gender'], age=request.form['age'], result=labelans)
    	db.session.add(user1)
    	db.session.commit()
    	uin=User.query.filter_by(pname=request.form['name']).first()
    	return render_template('index.html',predict=labelans,image_file=image_file,pname=uin.pname,gender=uin.gender,age=uin.age)
if __name__ == '__main__':
	app.run(debug=True)

