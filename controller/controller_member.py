import datetime
from app import db, app
from model.model_member import Clan, ClanMember, BlackList

class MemeberController:

    # 세션 검사 프로세스 추후 추가

    def retrieve_all_clan(self):
        result = db.session.execute(db.select(Clan)).scalars().fetchall()
        return result
    
    def retrieve_clan_name(self, clan_id):
        result = db.session.execute(db.select(Clan.clanname).filter_by(clan_id=clan_id)).scalar_one()
        return result
    
    def retrieve_clan_id(self, clan_name):
        result = db.session.execute(db.select(Clan.clan_id).filter_by(clanname=clan_name)).scalar()
        return result

    def retrieve_clan_member(self, clan_id):
        result = db.session.execute(db.select(ClanMember).filter_by(clan_id=clan_id)).scalars().fetchall()
        return result

    def retrieve_blacklist(self):
        result = db.session.execute(db.select(BlackList)).scalars().fetchall()
        return result
    
    def add_clan(self, clan_name):        
        result = Clan(clanname=clan_name)
        db.session.add(result)
        db.session.commit()

    def edit_clan(self, clan_id, edit_clan_name):
        result = db.session.execute(db.select(Clan).filter_by(clan_id=clan_id)).scalar_one()
        result.clanname = edit_clan_name
        db.session.commit()
        return True

    def delete_clan(self, clan_id):
        result = db.session.execute(db.select(Clan).filter_by(clan_id=clan_id)).scalar_one()
        db.session.delete(result)
        db.session.commit()
        return True

    def add_clan_member(self, nickname, clan_id):
        result = ClanMember(nickname=nickname, clan_id=clan_id)
        db.session.add(result)
        db.session.commit()

    def edit_clan_member(self, member_id, nickname):
        result = db.session.execute(db.select(ClanMember).filter_by(member_id=member_id)).scalar_one()
        result.nickname = nickname
        db.session.commit()
        return True

    def delete_clan_member(self, member_id):
        result = db.session.execute(db.select(ClanMember).filter_by(member_id=member_id)).scalar_one()
        db.session.delete(result)
        db.session.commit()
        return True

    def add_blacklist(self, array):
        age = datetime.datetime.now().year - int(array['age']) + 1
        ban_date = datetime.datetime.timestamp(datetime.datetime.strptime(array['ban_date'], "%Y-%m-%d"))
        result = BlackList(
            nickname=array['nickname'], age=age, gender=array['gender'], discord_name1=array['discord_name1'], discord_name2=array['discord_name2'],
            extra_information=array['extra_information'], player_rank=array['player_rank'], reason1=array['reason1'],
            reason2=array['reason2'], reason3=array['reason3'], description=array['description'],
            ban_date=ban_date, sub_account=array['sub_account'], clan_id=array['clan_id'])
        db.session.add(result)
        db.session.commit()

    def edit_blacklist(self, blacklist_id, array):
        result = db.session.execute(db.select(BlackList).filter_by(blacklist_id=blacklist_id)).scalar_one()
        age = datetime.datetime.now().year - int(array['age']) + 1
        ban_date = datetime.datetime.timestamp(datetime.datetime.strptime(array['ban_date'], "%Y-%m-%d"))
        model_list = ["nickname", "age", "gender", "discord_name1", "discord_name2", "extra_information", "player_rank", "reason1", "reason2", "reason3", "description", "ban_date", "sub_account", "clan_id"]
        for i in model_list:
            if i == 'age':
                exec(f'if array["{i}"]: result.{i} = {age}')
                continue
            if i == 'ban_date':
                exec(f'if array["{i}"]: result.{i} = {ban_date}')
                continue

            exec(f'if array["{i}"]: result.{i} = array["{i}"]')
            db.session.commit()
        return True

    def delete_blacklist(self, blacklist_id):
        result = db.session.execute(db.select(BlackList).filter_by(blacklist_id=blacklist_id)).scalar_one()
        db.session.delete(result)
        db.session.commit()
        return True
