from flask import request
from flask_restx import Resource, Namespace, fields

member_nameapace = Namespace(
    name = '멤버',
    description = '블랙리스트, 클랜원 관리 엔드포인트'
    )