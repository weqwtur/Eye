from sqlalchemy import Column, Integer, BigInteger
from .database import Base


class UserClicks(Base):
    __tablename__ = "user_clicks"

    user_id = Column(BigInteger, primary_key=True)
    clicks = Column(Integer, default=0)
