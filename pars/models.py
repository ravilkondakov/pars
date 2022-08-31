from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Info(Base):
    __tablename__ = "site information"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
