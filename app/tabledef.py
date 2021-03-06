from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:////Users/richa/PycharmProjects/ClimbOn/app/tutorial.db', echo=True)
Base = declarative_base()

#################################
class User(Base):
    """"""
    __tablename__ = "users"

    id=Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    xp = Column(Integer)

    #------------------------------------------------------
    def __init__(self, username, password, email, xp):
        """"""
        self.username = username
        self.password = password
        self.email = email
        self.xp = xp

#create tables
Base.metadata.create_all(engine)

