from flask import Flask, render_template
import requests
from post import Post

posts = requests.get("https://api.npoint.io/403b4ea1ed0fcc2c8b78").json()
allposts = []

for post in posts:
    postObj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    allposts.append(postObj)



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', posts=allposts)


@app.route('/post/<int:ids>')
def post(ids):
    for post in allposts:
        if post.id == ids:
            requestedPost = post
    return render_template('post.html', posts=requestedPost)


if __name__ == "__main__":
    app.run(debug=True)
