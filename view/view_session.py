import datetime
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource, Namespace, fields

from controller.controller_session import SessionController

session_nameapace = Namespace(
    name = '세션',
    description = '세션 기능의 엔드포인트'
    )


@session_nameapace.route('/create_token', methods=['POST'])
class CreateToken(Resource):
    @session_nameapace.expect(session_nameapace.model("토큰 생성 및 refresh", {'discord_nickname': fields.String(description='디스코드 서버 닉네임'),'discord_id': fields.String(description='디스코드 아이디'), 'discord_unique_id': fields.String(description='디스코드 고유 아이디')}))
    def post(self):
        discord_id = request.json['discord_id']
        discord_nickname = request.json['discord_nickname']
        discord_unique_id = request.json['discord_unique_id']
        session_object = SessionController()
        result = session_object.create_token(discord_id=discord_id, discord_nickname=discord_nickname, discord_unique_id=discord_unique_id)
        return {"token": result}


@session_nameapace.route('/create_session', methods=['POST'])
class CreateSession(Resource):
    @session_nameapace.expect(session_nameapace.model("세션 생성", {'discord_nickname': fields.String(description='디스코드 서버 닉네임'),'discord_id': fields.String(description='디스코드 아이디'), 'discord_unique_id': fields.String(description='디스코드 고유 아이디')}))
    def post(self):
        discord_id = request.json['discord_id']
        discord_nickname = request.json['discord_nickname']
        discord_unique_id = request.json['discord_unique_id']
        session_object = SessionController()
        tokens = session_object.create_token(discord_id=discord_id, discord_nickname=discord_nickname, discord_unique_id=discord_unique_id)
        session = session_object.create_session(discord_id=discord_id, discord_nickname=discord_nickname, discord_unique_id=discord_unique_id, access_token=tokens['access_token'])
        return {"result": "success", "session_name": session['session_name']}
    

@session_nameapace.route('/listing_session', methods=['GET'])
class ListingSession(Resource):
    def get(self):
        result = []
        session_object = SessionController()
        session_list = session_object.listing_session()
        for i, session in enumerate(session_list):
            created_at = str(datetime.datetime.fromtimestamp(int(session.created_at)))            
            result.append({"session_id": session.session_id, "session_name": session.session_name, "discord_nickname":session.discord_nickname, "created_at": created_at, "tokens": session.tokens, "discord_id": session.discord_id, "discord_unique_id": session.discord_unique_id, "expired": session.expired})
        return result
    
@session_nameapace.route('/destroy_session', methods=['POST'])
class DestroySession(Resource):
    @session_nameapace.expect(session_nameapace.model("세션 만료", {"session_id": fields.Integer(description='세션아이디', example=1)}))
    def post(self):
        session_id = request.json['session_id']
        session_object = SessionController()
        session_object.destory_session(session_id)
        return {"result": "success"}

@session_nameapace.route('/<string:session_name>', methods=['GET'])
class CreateEntrance(Resource):
    def get(self, session_name):
        session_object = SessionController()
        tokens = session_object.get_token(session_name=session_name)
        validation_check = session_object.check_session_validation(session_id=tokens.session_id, tokens=tokens.tokens)
        if validation_check is None:
            return {"result": "Unauthorized"}
        return {"token": tokens.tokens, "session_id": tokens.session_id, "validation": "validate"}
