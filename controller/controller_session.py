from app import db
from model.model_session import Session, SessionLog
from util.generate_phrases import generate_random_phrases
from flask_jwt_extended import create_access_token, create_refresh_token

class SessionController():
    def create_token(self, discord_nickname: str = None, discord_id: str = None):
        pass

    def verify_token(self, args):
        pass

    def create_session(self):
        pass

    def check_session_validation(self):
        pass

    def destory_session(self):
        pass

    def verify_permission(self):
        pass

    def save_session_log(self,discord_nickname: str = None, discord_id: str = None, discord_unique_id: str = None):
        pass

    def retrieve_session_log(self):
        pass

    def create_uri(self):
        pass

    