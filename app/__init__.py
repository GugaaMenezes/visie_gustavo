from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
CORS(app)

from app.views.home import home_blueprint

from app.routes import routes
from app.routes.api_routes import api

app.register_blueprint(api, url_prefix='/api')

app.register_blueprint(home_blueprint)
