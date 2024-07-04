from email import message
from flask import Flask, render_template,request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        inp = request.form.get("inp")
        sid =SentimentIntensityAnalyzer()
        score= sid.polarity_scores(inp)
        if score["neg"] != 0:
            return render_template('index.html',message="Negetive 😢😢")
        else:
            return render_template('index.html',message="Positive 🙂🙂")
    return render_template('index.html')

if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(port=800)