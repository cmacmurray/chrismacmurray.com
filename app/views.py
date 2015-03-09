from app import app, db, lm oid
from flask import render_template, flash, redirect, session, url_for, request g
from flask.ext import login_user, logout_user, current_user, login_required
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'CMac'} # fake user
    posts = [ #fake array of posts
        {
            'author': {'nickname': 'Jon'},
            'body' : 'Beautiful day in Queens'
        },
        {
            'author': {'nickname': 'Cmac'},
            'body': 'I hope I have a better time tomorrow'
        }
    ]
    return render_template('index.html',
                            title = 'HomePage',
                            user=user)
@app.route('/login', methods=['GET','POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['rmember_me'] form.remember_me.data
        return oid.try_login(from.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                            title='Sign In',
                            form = form,
                            providers=app.config['OPENID_PROVIDERS'])
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
