from flask import Flask, render_template, send_from_directory
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/print')
def print():
    return render_template('print.html')

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


@app.route('/scara_project')
def scara():
    return render_template("scara.html")

if __name__ == '__main__':
    app.run(debug=True)
