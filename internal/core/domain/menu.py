from sqlalchemy import Column, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Menu(Base):
    __tablename__ = "menus"

    token = Column(String, primary_key=True, server_default=func.gen_random_uuid())
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    active = Column(Boolean, default=True)
