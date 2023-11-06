from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from .routes import routes
from .routes.routes import api

app.register_blueprint(api, url_prefix='/api')
