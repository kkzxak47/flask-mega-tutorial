from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    title = "Flask mega tutorial"
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'Bob'},
            'body': 'Alice, your key has been stolen, I made a new one for ya.'
        }
    ]
    return render_template("index.html", user=user, title=title, posts=posts)
