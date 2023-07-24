from flask import Flask
import random

random_number = random.randint(0,9)
print(random_number)
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9 </h1>' \
           '<img src="https://media4.giphy.com/media/l378khQxt68syiWJy/200w.webp?cid' \
           '=ecf05e475o6ee8qqos6iebumoath85yzd79sun4b96t7qfny&ep=v1_gifs_search&rid=200w.webp&ct=g" />'

@app.route('/user/<int:number>')
def guessedNumber(number):
    numb = True
    while numb:
        if number < random_number:
            return f'<h1> {number} Too low</h1>' \
                   '<img src="https://media3.giphy.com/media/i6TiqPLXSRfs2L86fy/200w.webp?cid' \
                   '=ecf05e4704e3oe8zegit6xnp79rdil5ixvguszln7auibhy0&ep=v1_gifs_search&rid=200w.webp&ct=g">'
        elif number > random_number:
            return f'<h1>{number} too High</h>' \
                   '<img src="https://media0.giphy.com/media/ebkHmvltNtGAQn0WEq/200.webp?cid' \
                   '=ecf05e475tkde2xgw83wsa2v1xhb20h962av90aga4wic15m&ep=v1_gifs_search&rid=200.webp&ct=g">'
        else:
            return f'<h1>and {number} is just the right number</h1>' \
                   f'<img src="https://media3.giphy.com/media/3HDVFbFQZzJRlC9j1X/200w.webp?cid' \
                   f'=ecf05e47ors5sowlk2jf3ovxxbkh6ziigh9mi0rnuwharyzp&ep=v1_gifs_search&rid=200w.webp&ct=g">'
            numb = False



if __name__ == "__main__":
    app.run()