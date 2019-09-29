from flask import Flask, render_template, request, url_for
#from flask_wtf import Form
#from wtforms import Form, RadioField, SubmitField

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/choice', methods=['post','get'])
def choice (id):
	if request == 'post':
		choice = request.form['option']
		return render_template("choice.html", choice=choice)

if __name__ == "__main__":
    app.run(debug=True)