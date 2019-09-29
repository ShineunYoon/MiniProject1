from flask import Flask, render_template, request, url_for
import twitter_sentiment_analysis
import sentiment_analysis
from wtforms import Form, StringField, RadioField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('choice.html')


@app.route('/', methods=['POST'])
def index():
    choice = request.form['text']
    processed_text = choice.upper()
    twitter_sentiment_analysis.get_tweets(choice, 100)
    result = sentiment_analysis.analyze("tweet.text")
    return result

if __name__ == "__main__":
    app.run(debug=True)
