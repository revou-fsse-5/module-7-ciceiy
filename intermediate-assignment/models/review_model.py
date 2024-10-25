from sqlalchemy import Column, Integer, String, ForeignKey
from connectors.db import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    description = Column(String(255), nullable=False)
    rating = Column(Integer, nullable=False)
    email = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)