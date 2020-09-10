#Dependencies
from flask import Flask, render_template, request, flash, session
from PIL import Image
from io import BytesIO
from check_ag_lists import check_name
from prawKeysOG import reddit
import requests, time, secrets, unidecode, jsons
#import spacy
import spacy[en_core_web_sm] as en_core_web_sm

# Flask Init
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)

#Praw Init
def init_praw(s,n):
    return reddit.subreddit(s).top("all", limit=n)

#Player Score
class PlayerScore:
    def __init__(self):
        self.totalEncountered = 0
        self.amountCorrect = 0
        self.cumulativeCorrect = 0
        self.cumulative_HS = 0

#Quiz Object class
class QuizObj:
    def __init__(self, img, imgRatio, correctAnswer, titleWas):
        self.img = img
        self.imgRatio = imgRatio
        self.correctAnswer = correctAnswer
        self.titleWas = titleWas

#Return City Name From Post Title:
def get_city_name(title):
    nlp = en_core_web_sm.load()
    doc = nlp(title)
    gpe = [ent.text for ent in doc.ents]
    for parse in gpe:
        for city in check_name:
            if parse.casefold() in city:
                return city
            else:
                return None

#Pic Generator
def gen(top_posts):
    for submission in top_posts:
        if not submission.stickied:
            try:
                assert get_city_name(submission.title) != None
                response = requests.get(submission.url)
                img = Image.open(BytesIO(response.content))
                width, height = img.size
                obj = QuizObj(submission.url, width/height, get_city_name(submission.title), submission.title)
                yield jsons.dump(obj)
            except StopIteration as e:
                print(e)
	
generator = gen(init_praw('cityporn', 10000))

#Check Guess and Update Player Scores
def check_answer(guess):
	answer = session['a']['correctAnswer']
	if guess.casefold() in map(unidecode.unidecode, answer):
		player['amountCorrect'] += 1
		player['totalEncountered'] += 1
		player['cumulativeCorrect'] += 1
		if player['cumulativeCorrect'] > player['cumulative_HS']:
			player['cumulative_HS'] = player['cumulativeCorrect']
		flash(f'Correct! That was {answer[0].title()}', "info")
	else:
		player['cumulativeCorrect'] = 0
		player['totalEncountered'] += 1
		flash(f'Incorrect that was {answer[0].title()}\n | Your Answer: {guess.title()}', "info")
	session['player'] = player
	
#Index
@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        if request.method == 'POST':
            check_answer(request.form['content'])
            session['a'] = next(generator)
            return render_template('index.html', session=session)
        else:
            session['player'] = jsons.dump(PlayerScore())
            session['a'] = next(generator)
            return render_template('index.html', session=session)
    except ValueError:
        pass

# Flask RUN:
if __name__ == "__main__":
	app.run()
