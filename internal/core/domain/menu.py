from sqlalchemy import Column, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Menu(Base):
    __tablename__ = 'menus'

    token = Column(String, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now()) 
    active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Menu(token={self.token}, name={self.name}, active={self.active})>"
