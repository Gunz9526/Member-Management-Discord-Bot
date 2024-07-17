import time
from app import db

from sqlalchemy import Text, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Session(db.Model):
    __tablename__ = 'Session'
    
    session_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    session_name: Mapped[str] = mapped_column(String(200), nullable=False)
    discord_nickname: Mapped[str] = mapped_column(String(200), nullable=False)
    created_at: Mapped[int] = mapped_column(Integer, nullable=False)
    tokens: Mapped[str] = mapped_column(Text, nullable=False)
    discord_id: Mapped[str] = mapped_column(Text, nullable=False)
    discord_unique_id: Mapped[str] = mapped_column(Text, nullable=False)
    expired:Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    # Relationships
    session_log = relationship("SessionLog", uselist=False, back_populates="session")

class SessionLog(db.Model):
    __tablename__ = 'Session_Log'
    
    history_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    action_table: Mapped[str] = mapped_column(String(200), nullable=False)
    action_type: Mapped[str] = mapped_column(String(200), nullable=False)
    action_data: Mapped[str] = mapped_column(Text, nullable=True)
    session_id: Mapped[int] = mapped_column(Integer, ForeignKey('Session.session_id'), nullable=False)
    created_at: Mapped[int] = mapped_column(Integer, nullable=False)
    
    # Relationships
    session = relationship("Session", back_populates="session_log")