from flask import Blueprint

from app.controller import persons


api = Blueprint("api", __name__)


@api.route("/", methods=["GET","POST"])
def index_api():
    return "Welcome a my mini app - Created by Gustavo Menezes!"

@api.route("/pessoas", methods=["GET","POST"])
def person():
    return persons.person()

@api.route("/pessoa/<int:id_pessoa>", methods=["GET","PUT","DELETE"])
def data_person(id_pessoa):
    return persons.data_person(id_pessoa)