from flask import Flask, request, render_template, url_for, redirect


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
