from app import app
from app.views import home

from flask import redirect, url_for


@app.route("/")
def index():
    return home.index()

@app.route("/pessoa/<int:id_pessoa>")
def info_person(id_pessoa):
    return home.info_person(id_pessoa)
@app.route("/pessoa")
def new_person():
    return home.new_person()

