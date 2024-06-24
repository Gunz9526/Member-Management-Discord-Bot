from flask import jsonify, request
from flask_restx import Resource, Namespace, fields

import datetime

from controller.controller_member import MemeberController

member_namespace = Namespace(
    name = "멤버",
    description = "블랙리스트, 클랜원 관리 엔드포인트"
    )

blacklist_info_nested = member_namespace.model(
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

blacklist_info = member_namespace.model(
    "array",
    {
        "array": fields.Nested(blacklist_info_nested),
    },
)

member_controller = MemeberController()


@member_namespace.route('/all_clan', methods=['GET'])
class RetrieveAllClan(Resource):
    def get(self):
        result = {}
        clan_list = member_controller.retrieve_all_clan()
        for i in range(len(clan_list)):
            updated_time = str(datetime.datetime.fromtimestamp(int(clan_list[i].updated_at)))
            result[i] = {"clan_id": clan_list[i].clan_id, "clan_name": clan_list[i].clanname, "clan_created_at": updated_time}
        
        return result
    
@member_namespace.route('/all_clanmember', methods=['POST'])
class RetrieveClanMember(Resource):
    @member_namespace.expect(member_namespace.model("클랜 별 인원 나열", {"clan_id": fields.Integer(description="조회 할 클랜 id", example=2)}))
    def post(self):
        result = {}
        clan_id = request.json['clan_id']
        member_list = member_controller.retrieve_clan_member(clan_id=clan_id)
        for i in range(len(member_list)):
            result[i] = {"member_id": member_list[i].member_id, "nickname": member_list[i].nickname, "created_at": member_list[i].created_at}

        return result

@member_namespace.route('/all_blacklist', methods=['GET'])
class RetrieveBlackList(Resource):
    def get(self):        
        model_list = ["blacklist_id", "nickname", "age", "gender", "discord_name1", "discord_name2", "extra_information", "player_rank", "reason1", "reason2", "reason3", "description", "ban_date", "sub_account", "clan_id", "created_at"]
        result = {}
        blacklist = member_controller.retrieve_blacklist()
        # for i in model_list:
        #     test = exec({eval(f'{i}:blacklist.{i}')})
        #     print(test)
        for i in range(len(blacklist)):
            result[i]={}
            for j in model_list:
                if j == 'ban_date':
                    result[i]['ban_date']= str(datetime.datetime.fromtimestamp(blacklist[i].ban_date).strftime('%Y-%m-%d'))
                    continue

                if j == 'created_at':
                    result[i]['created_at'] = str(datetime.datetime.fromtimestamp(blacklist[i].created_at))
                    continue

                if j == 'age':
                    result[i]['age'] = str(datetime.datetime.now().year - int(blacklist[i].age) + 1)
                    continue
                # print(f'result[{i}]["{j}"] = blacklist[{i}].{j}')
                exec(f'result[{i}]["{j}"] = blacklist[{i}].{j}')
            result[i]['clan_name'] = member_controller.retrieve_clan_info(blacklist[i].clan_id)
            # exec(f'result[i] = { i:blacklist.i for i in model_list }')
        return result

@member_namespace.route('/add_clan', methods=['POST'])
class AddClan(Resource):
    @member_namespace.expect(member_namespace.model("클랜 추가", {'clan_name': fields.String(description="클랜 이름", example="테스트클랜1")}))
    def post(self):
        clan_name = request.json['clan_name']
        member_controller.add_clan(clan_name)
        return {"result": "success"}
    
@member_namespace.route('/edit_clan', methods=['PATCH'])
class EditClan(Resource):
    @member_namespace.expect(member_namespace.model("클랜 이름 수정", {"clan_id": fields.Integer(description="클랜 id", example=2) ,"clan_name": fields.String(description="수정 할 클랜 이름", example="수정 클랜 이름")}))
    def patch(self):
        clan_id = request.json['clan_id']
        edit_clan_name = request.json['clan_name']
        result = member_controller.edit_clan(clan_id, edit_clan_name)
        if result is True:
            return {"result": "success"}
        else:
            return {"result": "failed"}
        
@member_namespace.route('/delete_clan', methods=['DELETE'])
class DeleteClan(Resource):
    @member_namespace.expect(member_namespace.model("클랜 삭제", {"clan_id": fields.Integer(description="삭제할 클랜 id", example=2)}))
    def delete(self):
        clan_id = request.json['clan_id']
        result = member_controller.delete_clan(clan_id)
        if result is True:
            return {"result": "success"}
        else:
            return {"result": "failed"}
        
@member_namespace.route('/add_clanmember', methods=['POST'])
class AddClanMember(Resource):
    @member_namespace.expect(member_namespace.model("클랜원 추가", {"nickname": fields.String(description="클랜원 닉네임,배틀태그", example="헥토파스칼킥#1234"), "clan_id": fields.Integer(description="소속 클랜 id", example=2)}))
    def post(self):
        clan_id = request.json['clan_id']
        nickname = request.json['nickname']
        member_controller.add_clan_member(clan_id=clan_id, nickname=nickname)
        return {"result": "success"}
    
@member_namespace.route('/edit_clanmember', methods=['PATCH'])
class EditClanMember(Resource):
    @member_namespace.expect(member_namespace.model("클랜원 닉네임 수정", {"member_id": fields.Integer(description="클랜원 고유 id", example=1), "nickname": fields.String(description="닉네임", example="내취미는윈드밀#1234")}))
    def patch(self):
        member_id = request.json['member_id']
        nickname = request.json['nickname']
        member_controller.edit_clan_member(member_id=member_id, nickname=nickname)
        return {"result": "success", "value": nickname}

@member_namespace.route('/delete_clanmember', methods=['DELETE'])
class DeleteClanMember(Resource):
    @member_namespace.expect(member_namespace.model("클랜원 삭제", {"member_id": fields.Integer(description="삭제 할 클랜원 고유 id", example=1)})) 
    def delete(self):
        member_id = request.json['member_id']
        member_controller.delete_clan_member(member_id=member_id)
        return {"result": "success"}
    

@member_namespace.route('/add_blacklist', methods=['POST'])
class AddBlackList(Resource):
    @member_namespace.expect(member_namespace.model("블랙리스트 추가", blacklist_info))
    def post(self):
        array = request.json['array']
        member_controller.add_blacklist(array=array)
        return {"result": "success", "value": array }
    
@member_namespace.route('/edit_blacklist', methods=['PATCH'])
class EditBlackList(Resource):
    @member_namespace.expect(member_namespace.model("블랙리스트 수정", {"blacklist_id": fields.Integer(description="수정 할 블랙리스트 고유 id", example=1), "array":fields.Nested(blacklist_info_nested) }))
    def patch(self):
        blacklist_id = request.json['blacklist_id']
        array = request.json['array']
        member_controller.edit_blacklist(blacklist_id=blacklist_id, array=array)
        return {"result": "success", "value":array}