from flask import render_template, flash, redirect
from app import app
from forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'me'}  # fake user
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
