from flask import Blueprint, render_template


from .extensions import db
from .models import User, Question


main = Blueprint('main',__name__)


@main.route('/ask')
def ask():
	return render_template('answer.html')
 
@main.route('/login')
def login():
	return render_template('login.html')

@main.route('/question')
def question():
	return render_template('question.html')


@main.route('/register')
def register():
	return render_template('register.html')

@main.route('/unanswered')
def unanswered():
	return render_template('unanswered.html')

@main.route('/users')
def users():
	return render_template('users.html')
	