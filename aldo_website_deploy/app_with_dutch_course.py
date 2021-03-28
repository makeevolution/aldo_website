from flask import request, Flask, render_template, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import requests
import json
import jsonpickle
from os import listdir
import os

app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_BINDS']={'les6':'sqlite:///les6.db',
                                'les7':'sqlite:///les7.db',
                                'les8':'sqlite:///les8.db',
                                'les9':'sqlite:///les9.db',
                                'reflexief':'sqlite:///reflexief.db',
                                'waar':'sqlite:///waar.db',
                                'zich':'sqlite:///zich.db',
                                'vertaling':'sqlite:///vertaling.db',
                                'diedatwat':'sqlite:///diedatwat.db',
                                'onregelmatig_verba':'sqlite:///onregelmatig_verba.db',
                                'separabelverba':'sqlite:///separabelverba.db',
                                'ER_VRAGEN':'sqlite:///ER_VRAGEN.db'
                                }
#https://www.youtube.com/watch?v=SB5BfYYpXjE
#Create database instance for dutch learning
db = SQLAlchemy(app)


class Tests(db.Model):
     id=db.Column(db.Integer, primary_key=True)
     question=db.Column(db.String(200),unique=True)
     answer = db.Column(db.String(200), unique=False)
     hint = db.Column(db.String(20000), unique=False)
     def __repr__(self):#Redefine what print(object) is
         return ';{}!{}!{}!{};'.format(self.id,self.question,self.answer,self.hint)
# To create a database instance:
    #1. Go to terminal to aldo_webstie_deploy dir and fire up python
    #2. type from app import db
    #3. type db.create_all()
    #4. type from app import Tests
    #5. type test_1=Tests(question='',answer='')
    #6. type db.session.add(test_1)
    #7. type db.session.commit()
class reflexief(db.Model):
    __bind_key__ = 'reflexief'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(2000), unique=False)
    answer = db.Column(db.String(2000), unique=False)
    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question, self.answer)

class separabelverba(db.Model):
    __bind_key__ = 'separabelverba'
    id = db.Column(db.Integer, primary_key=True)
    question_dutch = db.Column(db.String(2000), unique=False)
    question_english = db.Column(db.String(2000), unique=False)
    gatentekst = db.Column(db.String(2000), unique=False)
    answer_dutch = db.Column(db.String(2000), unique=False)
    answer_english = db.Column(db.String(2000), unique=False)
    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question_dutch, self.question_english)

class diedatwat(db.Model):
    __bind_key__ = 'diedatwat'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(2000), unique=False)
    answer = db.Column(db.String(2000), unique=False)

    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question, self.answer)

class onregelmatig_verba(db.Model):
    __bind_key__ = 'onregelmatig_verba'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(2000), unique=False)
    answer = db.Column(db.String(2000), unique=False)

    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question, self.answer)

class waar(db.Model):
    __bind_key__ = 'waar'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(2000), unique=False)
    answer = db.Column(db.String(2000), unique=False)
    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question, self.answer)

class zich(db.Model):
    __bind_key__ = 'zich'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(2000), unique=False)
    answer = db.Column(db.String(2000), unique=False)
    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question, self.answer)

class les6(db.Model):
    __bind_key__='les6'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), unique=True)
    answer = db.Column(db.String(200), unique=False)
    hint = db.Column(db.String(2000), unique=False)

    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question, self.answer)

class vertaling(db.Model):
    __bind_key__ = 'vertaling'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(2000), unique=False)
    answer = db.Column(db.String(2000), unique=False)
    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question, self.answer)

@app.route("/dutch_testgatentekst_oefenen")
def gatenteksttest():
    return render_template("dutch_testgatentekst_oefenen.html")

class ER_VRAGEN(db.Model):
    __bind_key__='ER_VRAGEN'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), unique=True)
    answer = db.Column(db.String(200), unique=False)
    hint = db.Column(db.String(2000), unique=False)

    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question, self.answer)


class les7(db.Model):
    __bind_key__ = 'les7'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), unique=True)
    answer = db.Column(db.String(200), unique=False)
    hint = db.Column(db.String(2000), unique=False)

    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question, self.answer)


class les8(db.Model):
    __bind_key__ = 'les8'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), unique=True)
    answer = db.Column(db.String(200), unique=False)
    hint = db.Column(db.String(2000), unique=False)

    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question, self.answer)


class les9(db.Model):
    __bind_key__ = 'les9'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), unique=True)
    answer = db.Column(db.String(200), unique=False)
    hint = db.Column(db.String(200), unique=False)

    def __repr__(self):  # Redefine what print(object) is
        return '{} {}'.format(self.question, self.answer)

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.route("/dutch_training_list")
def dutch_training_list():
    mypath = os.getcwd()
    mypath = "{}/templates".format(mypath)
    routes = [f for f in listdir(mypath) if f[-4:] == "html"]

    routes.remove("dutch_training_list.html")
    routes.remove("dutch_training_tonen_10_pages.html")

    routes_alleen_dutch=[i for i in routes if i[0:5]=="dutch"]
    links=["/{}".format(f) for f in routes_alleen_dutch]
    links = [f[0:len(f)-5] for f in links]

    names=[f[0:len(f)-5] for f in routes_alleen_dutch]
    return render_template("dutch_training_list.html",list=links,names=names)

@app.route('/dutch_training',methods=['GET','POST'])
def dutch_training():
    data=Tests.query.all()
    return render_template("dutch_training.html",data=data)

@app.route('/dutch_training_vertal_engels',methods=["GET","POST"])
def dutch_training_vertal_engels():
    data=Tests.query.all()
    return render_template("dutch_training_vertal_engels.html",data=data)

@app.route('/dutch_separabel_verba_oefenen',methods=["GET","POST"])
def dutch_separabel_verba_oefenen():
    data=separabelverba.query.all()
    return render_template("dutch_separabel_verba_oefenen.html",data=data)

@app.route('/<name>_oefenen')
def oefening_oefenen(name="reflexief"):
    return render_template(name+"_oefenen.html")

@app.route('/get_<name>_data')
def get_oefening_data(name=None):
    data2=eval(name).query.all()
    app.logger.info(data2)
    return jsonpickle.encode(data2)

@app.route('/add_question_<name>',methods=['GET','POST'])
def add_question_oefenen(name='None'):
    new_question=request.form['fname']
    new_answer=request.form['lname']
    db.create_all()

     # change question and answer field to reflect what you want
    test_1 = eval(name)(question=new_question, answer=new_answer)

    db.session.add(test_1)
    db.session.commit()
    return render_template("dutch_"+name+"_oefenen.html")

@app.route('/add_questionspecial_separabel',methods=['GET','POST'])
def add_question_special_separabel(name='None'):
    new_question = request.form['fname']
    new_answer1 = request.form['lname1']
    new_answer2 = request.form['lname2']
    new_answer3 = request.form['lname3']
    new_answer4 = request.form['lname4']
    db.create_all()

     # change question and answer field to reflect what you want
    test_1 = separabelverba(question_dutch=new_question, question_english=new_answer1, gatentekst=new_answer2, answer_dutch=new_answer3,answer_english=new_answer4)

    db.session.add(test_1)
    db.session.commit()
    return render_template("dutch_separabel_verba_oefenen.html")

@app.route('/dutch_beelden_oefenen',methods=['GET','POST'])
def dutch_beelden_oefenen():
    return render_template("dutch_beelden_oefenen.html")

@app.route('/delete_<name>',methods=['GET','POST'])
def delete_data_oefenen(name=None):
    delete_question=request.form['deletes']
    missing = eval(name).query.filter_by(id=delete_question).first()
    db.session.delete(missing)
    db.session.commit()

    data = eval(name).query.all()
    j=1
    for i in data:
        i.id=j
        j=j+1
    db.session.commit()
    return render_template("dutch_"+name+"_oefenen.html")

@app.route('/tonen_alleen_10',methods=['GET','POST'])
def tonen_alleen_10():
    tonen_alleen = request.form['tonen']
    data_render_final=[]
    if int(tonen_alleen)+10 > int(Tests.query.count()):
        tonen_alleen_end=int(Tests.query.count())
    else:
        tonen_alleen_end=int(tonen_alleen)+10
    for i in np.linspace(int(tonen_alleen),tonen_alleen_end,11):
        data_render=Tests.query.\
            filter_by(id = i).all()
        data_render_final.append(data_render)
    no_of_rows=i
    return render_template("dutch_training_tonen_10_pages.html",data_render_final=data_render_final,no_of_rows=no_of_rows)

@app.route('/tonen_alleen_10_vertal',methods=['GET','POST'])
def tonen_alleen_10_vertal():
    tonen_alleen = request.form['tonen']
    data_render_final=[]
    if int(tonen_alleen)+10 > int(Tests.query.count()):
        tonen_alleen_end=int(Tests.query.count())
    else:
        tonen_alleen_end=int(tonen_alleen)+10
    for i in np.linspace(int(tonen_alleen),tonen_alleen_end,11):
        data_render=Tests.query.\
            filter_by(id = i).all()
        data_render_final.append(data_render)
    no_of_rows=i
    return render_template("dutch_training_tonen_10_pages_vertal.html",data_render_final=data_render_final,no_of_rows=no_of_rows)

@app.route('/dutch_training<name>',methods=['GET','POST'])
def dutch_training_les(name=None):
    data=eval(name).query.all()
    app.logger.info('success_into_new_les_Routes')
    return render_template("dutch_training"+name+".html",data=data)

@app.route('/get_data',methods=['GET','POST'])
def get_data():
    data=Tests.query.all()
    #Here I use jsonpickle custom library in order to parse Tests class object into JSON form
    return jsonpickle.encode(data)

@app.route('/get_data/<name>',methods=['GET','POST'])
def get_data_les(name=None):
    data=eval(name).query.all()
    #Here I use jsonpickle custom library in order to parse Tests class object into JSON form
    return jsonpickle.encode(data)

@app.route('/hint/<question_need_hint>')
def hint(question_need_hint):
    data=Tests.query.filter_by(question=question_need_hint).first()
    return f'<h1> {data.hint} </h1>'

@app.route('/hint/<question_need_hint>/<name>',methods=['GET','POST'])
def hint_les(name,question_need_hint):
    data=eval(name).query.filter_by(question=question_need_hint).first()
    return f'<h1> {data.hint} </h1>'


@app.route('/add_question',methods=['GET','POST'])
def add_question():
    new_question=request.form['fname']
    new_answer=request.form['lname']
    new_hint = request.form['hints']
    db.create_all()

     # change question and answer field to reflect what you want
    test_1 = Tests(question=new_question, answer=new_answer, hint=new_hint)

    db.session.add(test_1)
    db.session.commit()
    return render_template("dutch_training.html")

@app.route('/add_question<name>',methods=['GET','POST'])
def add_question_les(name='None'):
    new_question=request.form['fname']
    new_answer=request.form['lname']
    new_hint = request.form['hints']
    db.create_all()

     # change question and answer field to reflect what you want
    test_1 = eval(name)(question=new_question, answer=new_answer, hint=new_hint)

    db.session.add(test_1)
    db.session.commit()
    return render_template("dutch_training"+name+".html")

@app.route('/delete',methods=['GET','POST'])
def delete():
    delete_question=request.form['deletes']
    missing = Tests.query.filter_by(id=delete_question).first()
    db.session.delete(missing)
    db.session.commit()

    data = Tests.query.all()
    j=1
    for i in data:
        i.id=j
        j=j+1
    db.session.commit()
    return render_template("dutch_training.html")

@app.route('/delete<name>',methods=['GET','POST'])
def delete_les(name=None):
    delete_question=request.form['deletes']
    missing = eval(name).query.filter_by(id=delete_question).first()
    db.session.delete(missing)
    db.session.commit()

    data = eval(name).query.all()
    j=1
    for i in data:
        i.id=j
        j=j+1
    db.session.commit()
    return render_template("dutch_training"+name+".html")

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
    app.run(debug=True,port=5000,host='0.0.0.0')
