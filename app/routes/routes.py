from flask import Blueprint, redirect, url_for


api = Blueprint('api', __name__)


@api.route("/", methods=['GET','POST'])
def login():
    return "Hello World!"