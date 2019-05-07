from . import blueprint
from flask import render_template


@blueprint.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/home')
def home():
    return render_template('index.html')
