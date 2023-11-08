from app import db
from flask import Blueprint

from app.controller import persons


api = Blueprint("api", __name__)

session = db.session

@api.route("/", methods=["GET","POST"])
def index():
    return "Welcome a my mini app - Created by Gustavo Menezes!"

@api.route("/pessoas", methods=["GET","POST"])
def person():
    return persons.person()

@api.route("/pessoas/<int:id_pessoa>", methods=["PUT","DELETE"])
def data_person(id_pessoa):
    return persons.data_person(id_pessoa)