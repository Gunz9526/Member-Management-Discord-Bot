import datetime
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource, Namespace, fields

from controller.controller_session import SessionController

session_namespace = Namespace(
    name = '세션',
    description = '세션 기능의 엔드포인트'
    )


# @session_namespace.route('/create_token', methods=['POST'])
# class CreateToken(Resource):
#     @session_namespace.expect(session_namespace.model("토큰 생성 및 refresh", {'discord_nickname': fields.String(description='디스코드 서버 닉네임'),'discord_id': fields.String(description='디스코드 아이디'), 'discord_unique_id': fields.String(description='디스코드 고유 아이디')}))
#     def post(self):
#         discord_id = request.json['discord_id']
#         discord_nickname = request.json['discord_nickname']
#         discord_unique_id = request.json['discord_unique_id']
#         session_object = SessionController()
#         result = session_object.create_token(discord_id=discord_id, discord_nickname=discord_nickname, discord_unique_id=discord_unique_id)
#         return {"token": result}


# @session_namespace.route('/create_session', methods=['POST'])
# class CreateSession(Resource):
#     @session_namespace.expect(session_namespace.model("세션 생성", {'discord_nickname': fields.String(description='디스코드 서버 닉네임'),'discord_id': fields.String(description='디스코드 아이디'), 'discord_unique_id': fields.String(description='디스코드 고유 아이디')}))
#     def post(self):
#         session_name = request.json['session_name']
#         session_object = SessionController()
#         tokens = session_object.get_token(session_name=session_name)
#         expired_check = session_object.check_expired_session(session_id=tokens.session_id, session_name=tokens.session_name, tokens=tokens.tokens)
#         if expired_check is None:
#             return {"result": "Unauthorized"}
#         session_object.destory_session(session_name==tokens.session_name)
#         return {"token": tokens.tokens, "session_name": tokens.session_name, "result": "valid", "session_id": tokens.session_id}

@session_namespace.route('/entrance_check', methods=['POST'])
class Entrance_check (Resource):
    @jwt_required()
    @session_namespace.expect(session_namespace.model("세션 정보 확인", {"session_id": fields.Integer(description='세션 ID', example=1),"session_name": fields.String(description="세션 name", example='dfsfdsfsdf'), "tokens": fields.String(description="토큰", example="dsfsdfdsfsdf")}))
    def post(self):
        session_id = request.json['session_id']
        session_name = request.json['session_name']
        tokens = request.json['tokens']
        session_object = SessionController()
        validation_check = session_object.cross_check_session_token(session_id=session_id, session_name=session_name, tokens=tokens)
        if validation_check is None:
            return {"result": "Unauthorized"}
        return {"result": "success"}

@session_namespace.route('/get_token', methods=['POST'])
class GetToken(Resource):
    @session_namespace.expect(session_namespace.model("토큰 및 세션 정보 반환", {'session_name': fields.String(description='세션 이름')}))
    def post(self):
        session_name = request.json['session_name']
        session_object = SessionController()
        tokens = session_object.get_token(session_name=session_name)
        if tokens is None:
            return {"result": "failed"}
        return {"result": "success", "token": tokens.tokens, "session_id": tokens.session_id, "session_name": tokens.session_name}

@session_namespace.route('/listing_session', methods=['GET'])
class ListingSession(Resource):
    def get(self):
        result = []
        session_object = SessionController()
        session_list = session_object.listing_session()
        for i, session in enumerate(session_list):
            created_at = str(datetime.datetime.fromtimestamp(int(session.created_at)))            
            result.append({"session_id": session.session_id, "session_name": session.session_name, "discord_nickname":session.discord_nickname, "created_at": created_at, "tokens": session.tokens, "discord_id": session.discord_id, "discord_unique_id": session.discord_unique_id, "expired": session.expired})
        return result
    
@session_namespace.route('/destroy_session', methods=['POST'])
class DestroySession(Resource):
    @session_namespace.expect(session_namespace.model("세션 만료", {"session_name": fields.Integer(description='세션이름', example='test')}))
    def post(self):
        session_name = request.json['session_name']
        session_object = SessionController()
        session_object.destory_session(session_name)
        return {"result": "success"}


# @session_namespace.route('/<string:session_name>', methods=['GET'])
# class CreateEntrance(Resource):
#     def get(self, session_name):
#         session_object = SessionController()
#         tokens = session_object.get_token(session_name=session_name)
#         validation_check = session_object.check_session_validation(session_id=tokens.session_id, tokens=tokens.tokens)
#         if validation_check is None:
#             return {"result": "Unauthorized"}
#         return {"token": tokens.tokens, "session_id": tokens.session_id, "validation": "validate"}
