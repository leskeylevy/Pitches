
from flask import render_template
from . import main


@main.route('/', methods = ['GET','POST'])
def index():
    title = 'YOU HAVE ONE MINUTE TO IMPRESS ME!'
    return render_template('index.html', title = title)
