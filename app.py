from datetime import timedelta

from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import  SQLAlchemy
from flask_cors import CORS

from config import db_url


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours=2)

jwt = JWTManager(app)

db = SQLAlchemy()
CORS(app)
db.init_app(app)

from view.view_session import session_namespace
from view.view_member import member_namespace


authorizations = {'bearer_auth': {
    'type': 'apiKey',
    'in': 'header',
    'name': 'Authorization'
    }}

api = Api(
    app,
    version='0.1',
    title='OW2 Clan Management REST API',
    description='Rest api 정리',
    authorizations=authorizations,
    security='bearer_auth',
    doc="/api-docs")


api.add_namespace(session_namespace, '/session')
api.add_namespace(member_namespace, '/member')
