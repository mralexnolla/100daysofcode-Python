from flask import Flask, render_template
import requests

posts = requests.get('https://api.npoint.io/09fae2f488f5bedac374').json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", allpost=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:ids>')
def post(ids):
    requested_post = None
    for bpost in posts:
        if bpost["id"] == ids:
            requested_post = bpost
    return render_template("post.html", post=requested_post)

# @app.route('/home')
# def home():
#     return render_template()


if __name__ == "__main__":
    app.run(debug=True)
