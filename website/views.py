from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/login')
def login():
    return "<h1>Login Page</h1>"

@views.route('/sign-up')
def sign_up():
    return "<h1>Sign Up Page</h1>"

