from app import db
from model.model_session import Session, SessionLog
from flask_jwt_extended import jwt_manager

class SessionController():
    def create_token(self, discord_nickname: str = None, discord_id: str = None):
        pass

    def create_session(self):
        pass

    def check_session_validation(self):
        pass

    def destory_session(self):
        pass

    def verify_permission(self):
        pass

    def save_session_log(self):
        pass

    def retrieve_session_log(self):
        pass
