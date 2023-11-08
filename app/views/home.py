from flask import Blueprint, flash, redirect, render_template, request, url_for
from ..controller.persons import select_person


home_blueprint = Blueprint("home", __name__, template_folder="templates\home")


def index():
    return render_template("index.html")

def info_person(id_pessoa):
    info_person = select_person(id_pessoa)
    info_person = info_person[2]
    return render_template("info_person.html", info_person=info_person)