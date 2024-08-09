from flask import request
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required

import datetime

from controller.controller_admin import AdminController

admin_namespace = Namespace(
    name = '관리자',
    description = '관리자 기능의 엔드포인트'
    )

blacklist_info_nested = admin_namespace.model(
    "블랙리스트 정보",
    {
        "nickname": fields.String(required=True, description="닉네임", example="뒤돌려차기#1234"),
        "age": fields.String(description="나이", example="30"),
        "gender": fields.String(description="성별 ( M / W )", example="M"),
        "discord_name1": fields.String(description="디스코드 닉네임", example="디코닉네임#1234"),
        "discord_name2": fields.String(description="디스코드 닉네임", example="닉코디네임#1234"),
        "extra_information": fields.String(description="신상정보 기타", example="카톡아이디 pascalkick1234"),
        "player_rank": fields.String(description="점수대", example="마스터0층 찍고내려옴"),
        "reason1": fields.String(description="사유1", example="피지컬만 있음"),
        "reason2": fields.String(description="사유2", example="자꾸 윈드밀하려함"),
        "reason3": fields.String(description="사유3", example="헥토파스칼킥!"),
        "description": fields.String(description="기타설명", example="게임을 못하는 걸 이해하지 못함"),
        "ban_date": fields.String(description="추방 날짜", example="2024-06-24"),
        "sub_account": fields.String(description="부계정", example="앞으로안돌려차기#1234"),
        "clan_id": fields.String(description="추방 클랜", example=2),
       
    },
)

blacklist_info = admin_namespace.model(
    "array",
    {
        "array": fields.Nested(blacklist_info_nested),
    },
)

@admin_namespace.route('/get_all_session', methods=['GET'])
class GetAllSession(Resource):
    def get(self):
        admin_object = AdminController()
        result = admin_object.get_all_session()
        return {"result": result}

@admin_namespace.route('/get_all_clan', methods=['GET'])
class GetAllClan(Resource):
    def get(self):
        admin_object = AdminController()
        result = admin_object.get_all_clan()
        return {"result": result}
    
@admin_namespace.route('/get_all_clan_member', methods=['GET'])
class GetAllClanMember(Resource):
    def get(self):
        admin_object = AdminController()
        result = admin_object.get_all_clan_member()
        return {"result": result}
    
@admin_namespace.route('/get_all_blacklist', methods=['GET'])
class GetAllBlacklist(Resource):
    def get(self):
        admin_object = AdminController()
        result = admin_object.get_all_blacklist()
        return {"result": result}
    
@admin_namespace.route('/add_clan', methods=['POST'])
class AddClan(Resource):
    @admin_namespace.expect(admin_namespace.model("클랜 추가", {'clan_name': fields.String(description='클랜 이름')}))
    def post(self):
        clan_name = request.json['clan_name']
        admin_object = AdminController()
        result = admin_object.add_clan(clan_name=clan_name)
        return {"result": result}
    
@admin_namespace.route('/edit_clan', methods=['POST'])
class EditClan(Resource):
    @admin_namespace.expect(admin_namespace.model("클랜 수정", {'clan_id': fields.Integer(description='클랜 ID'), 'edit_clan_name': fields.String(description='수정할 클랜 이름')}))
    def post(self):
        clan_id = request.json['clan_id']
        edit_clan_name = request.json['edit_clan_name']
        admin_object = AdminController()
        result = admin_object.edit_clan(clan_id=clan_id, edit_clan_name=edit_clan_name)
        return {"result": result}
    