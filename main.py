from flask import Flask, render_template, request
import twitter_sentiment_analysis
import sentiment_analysis
import overall_scorer

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('choice.html')


@app.route('/', methods=['POST'])
def index():
    choice = request.form['option']
    # First Long-term Analysis
    twitter_sentiment_analysis.get_tweets(choice, 50)
    result1 = sentiment_analysis.analyze("tweet.text")

    # Second Short-term analysis
    twitter_sentiment_analysis.get_tweets(choice, 10)
    result2 = sentiment_analysis.analyze("tweet.text")

    # Overall Score
    overall_reliability = overall_scorer.isReliable(result1, result2)
    overall_score = overall_scorer.scorer(result1, result2)
    return render_template('result.html', choice=choice, overall_reliability=overall_reliability, overall_score=overall_score )

if __name__ == "__main__":
    app.run(debug=True)
