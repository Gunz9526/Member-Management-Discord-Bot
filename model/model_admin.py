import time
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app import db


class Admin(db.Model):
    __tablename__ = 'Admin'
    
    admin_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id: Mapped[str] = mapped_column(String(200), nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)