from flask import Flask, render_template, send_from_directory
import requests

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

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
