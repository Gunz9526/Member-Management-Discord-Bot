from app import db
from model.model_session import Session, SessionLog
from util.generate_phrases import RandomPhraseGenerator
from flask_jwt_extended import create_access_token, decode_token


class SessionController():
    def create_token(self, discord_nickname: str, discord_id: str, discord_unique_id: str):
        additional_claims = {"discord_id": discord_id, "discord_unique_id": discord_unique_id}
        access_token = create_access_token(identity=discord_nickname, additional_claims=additional_claims)
        # decoded_token = decode_token(access_token)
        return {"access_token": access_token}
    
    def get_token(self, session_name):
        result = db.session.execute(db.select(Session).filter(Session.session_name==session_name, Session.expired==0).order_by(Session.created_at.desc())).scalar()
        return result

    def verify_token(self, discord_nickname: str, discord_id: str, discord_unique_id: str):
        pass

    def create_session(self, discord_nickname: str, discord_id: str, discord_unique_id: str, access_token):
        phrase_object = RandomPhraseGenerator()
        session_name = phrase_object.generate_random_phrase()
        result = Session(session_name=session_name, discord_nickname=discord_nickname, discord_id=discord_id, discord_unique_id=discord_unique_id, tokens=access_token)
        db.session.add(result)
        db.session.commit()
        return {"session_name": session_name}

    def check_expired_session(self, session_id, session_name, tokens):
        result = db.session.execute(db.select(Session).filter(Session.session_id==session_id, Session.session_name==session_name, Session.tokens==tokens, Session.expired==0).order_by(Session.created_at.desc())).scalar()
        return result

    def cross_check_session_token(self, session_id, session_name, tokens):
        result = db.session.execute(db.select(Session).filter(Session.session_id==session_id, Session.session_name==session_name, Session.tokens==tokens).order_by(Session.created_at.desc())).scalar()
        return result
    
    def destory_session(self, session_name):
        result = db.session.execute(db.select(Session).filter(Session.session_name==session_name).order_by(Session.created_at.desc())).scalar()
        result.expired = 1
        # db.session.delete(result)
        db.session.commit()
        return True

    def listing_session(self):
        result = db.session.execute(db.select(Session).order_by(Session.created_at.desc())).scalars().all()
        return result

    def save_session_log(self,discord_nickname: str, discord_id: str, discord_unique_id: str, ):
        pass

    def retrieve_session_log(self):
        pass

    def create_uri(self):
        pass
