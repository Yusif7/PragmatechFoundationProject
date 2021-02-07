from flask import Blueprint,render_template,redirect,request,url_for, flash
from app.models import *
from datetime import date
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from admin.forms import LoginForm

auth=Blueprint(
    'auth',
    __name__,
    url_prefix='/login',
    template_folder='templates',
    static_folder='static')

@auth.route('/')
def login():
    loginForm = LoginForm()
    return render_template ("login.html",form = loginForm)

@auth.route('/main', methods=['POST'])
def login_post():
    loginForm = LoginForm()
    admin = Admin.query.filter_by(name = 'Yusif').one()
    if request.method == 'POST':
        email=loginForm.email.data
        password = loginForm.password.data
        if email == admin.email and password == 'z240820a':
            return redirect ("/admin")
        else:
            flash('Incorrect mail or password')
            return redirect('/login')
    return render_template('/login', form = loginForm)


@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    admin = Admin.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if admin: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect('/signup')

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_admin = Admin(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_admin)
    db.session.commit()
    return redirect ('/login')

@auth.route('/logout')
def logout():
    return 'Logout'