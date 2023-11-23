from flask import Flask, request, render_template, url_for, redirect
from todo.models import ToDo, db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app


app = create_app()


@app.get('/')
def home():
    pass

@app.get('/')
def add():
    pass

@app.get('/')
def update():
    pass

@app.get('/')
def delete():
    pass
