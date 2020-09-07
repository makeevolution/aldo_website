from flask import request, Flask, render_template, send_from_directory
#from flask_sqlalchemy import SQLAlchemy
import requests
import json
#import jsonpickle

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

#Create database instance for dutch learning
# db = SQLAlchemy(app)
# class Tests(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     question=db.Column(db.String(200),unique=True)
#     answer = db.Column(db.String(200), unique=False)
#
#     def __repr__(self):#Redefine what print(object) is
#         return '{} {}'.format(self.question,self.answer)
# To create a database instance:
    #1. Go to terminal to aldo_webstie_deploy dir and fire up python
    #2. type from app import db
    #3. type db.create_all()
    #4. type from app import Tests
    #5. type test_1=Tests(question='',answer='')
    #6. type db.session.add(test_1)
    #7. type db.session.commit()

@app.route('/dutch_training',methods=['GET','POST'])
def dutch_training():
    data=Tests.query.all()
    if request.method=='POST':
        name=request.form['name']
        return f'<h1> {name} </h1>'
    else:
        return render_template("dutch_training.html",data=data)

@app.route('/get_data',methods=['GET','POST'])
def get_data():
    data=Tests.query.all()
    #Here I use jsonpickle custom library in order to parse Tests class object into JSON form
    return jsonpickle.encode(data)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/print')
def print():
    return render_template('print.html')
#For Favicon

@app.route('/assets/img/<path:filename>')
def favicon(filename):
    return send_from_directory("assets/img",filename)

@app.route('/project_pictures/fullsize/<path:filename>')
def project_pictures_fullsize(filename):
    return send_from_directory("assets/img/portfolio/fullsize",filename)

@app.route('/project_pictures/thumbnails/<path:filename>')
def project_pictures_thumbnails(filename):
    return send_from_directory("assets/img/portfolio/thumbnails",filename)

@app.route('/templates/<path:filename>')
def pictures(filename):
    return send_from_directory("templates",filename)

@app.route('/raspi_camera_project')
def raspi_camera_project():
    return render_template("raspi_camera_project.html")

@app.route('/scara_project')
def scara():
    return render_template("scara.html")

@app.route("/getquestion")
def getquestion():

    response=requests.get("https://opentdb.com/api.php?amount=1&category=30")

    return response.json()["results"]["question"]

@app.route('/Trivia_API')
def Trivia_API():
    return render_template("Trivia_API.html")

@app.route('/waver_stepper_control')
def waver_stepper_control():
    return render_template("waver_stepper_control.html")

@app.route('/exit_survey')
def exit_survey():
    return render_template("exit_survey.html")

@app.route('/spectrogram')
def spectrogram():
    return render_template("spectrogram.html")

if __name__ == '__main__':
    app.run(debug=True)
