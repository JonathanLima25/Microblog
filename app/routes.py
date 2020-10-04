from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Jonathan'}
    posts = [
        {
            'author':{'username':'Jhon'},
            'body':'Python é legal'
        },
        {
            'author':{'username':'Tommy'},
            'body':'A diferença entre cura e veneno é a dose'
        },
        {
            'author':{'username':'Arthur'},
            'body':'Não depende do que você fala, mas como fala'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

