from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import  SQLAlchemy

from config import db_url


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()

db.init_app(app)

from view.view_session import session_nameapace
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


api.add_namespace(session_nameapace, '/view_session')
api.add_namespace(member_namespace, '/view_member')

@app.route('/')
def index():
    test=0
    print("변수 : " + str(test)) 
    return ('Hello1 World!' + str(test))
