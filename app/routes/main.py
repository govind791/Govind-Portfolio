from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', active='home')

@main.route('/projects')
def projects():
    return render_template('projects.html', active='projects')

@main.route('/skills')
def skills():
    return render_template('skills.html', active='skills')

@main.route('/education')
def education():
    return render_template('education.html', active='education')

@main.route('/experience')
def experience():
    return render_template('experience.html', active='experience')