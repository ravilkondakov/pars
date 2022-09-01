from sqlalchemy import Column, Integer, String, VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Info(Base):
    __tablename__ = "site_information"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String())
