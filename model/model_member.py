import time
from app import db

from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Clan(db.Model):
    __tablename__ = 'Clan'
    clan_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    clanname: Mapped[str] = mapped_column(String(200), nullable=False)
    updated_at: Mapped[int] = mapped_column(Integer, nullable=False, default=time.time())

    users = relationship("ClanMember", cascade="all, delete-orphan")
    blacklists = relationship("BlackList",  cascade="all, delete-orphan")

class ClanMember(db.Model):
    __tablename__ = 'Clan_Member'
    member_id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[int] = mapped_column(default=time.time())
    clan_id: Mapped[int] = mapped_column(Integer, ForeignKey('Clan.clan_id'))
    visible: Mapped[int] = mapped_column(default=1)

    clan = relationship("Clan", back_populates="users")

class BlackList(db.Model):
    __tablename__ = 'BlackList'    
    blacklist_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nickname: Mapped[str] = mapped_column(String(200))
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    gender: Mapped[str] = mapped_column(String(50), nullable=True)
    discord_name1: Mapped[str] = mapped_column(String(200), nullable=True)
    discord_name2: Mapped[str] = mapped_column(String(200), nullable=True)
    extra_information: Mapped[str] = mapped_column(Text, nullable=True)
    player_rank: Mapped[str] = mapped_column(String(100), nullable=True)
    reason1: Mapped[str] = mapped_column(Text)
    reason2: Mapped[str] = mapped_column(Text, nullable=True)
    reason3: Mapped[str] = mapped_column(Text, nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    ban_date: Mapped[int] = mapped_column(Integer)
    sub_account: Mapped[str] = mapped_column(String(200), nullable=True)
    clan_id: Mapped[int] = mapped_column(Integer, ForeignKey('Clan.clan_id'))
    created_at: Mapped[int] = mapped_column(Integer, default=time.time())
    visible: Mapped[int] = mapped_column(Integer, default=1)

    clan = relationship("Clan", back_populates="blacklists")
