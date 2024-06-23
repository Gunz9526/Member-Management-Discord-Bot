from flask import request
from flask_restx import Resource, Namespace, fields

session_nameapace = Namespace(
    name = '세션',
    description = '세션 기능의 엔드포인트'
    )