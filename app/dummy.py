import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:////Users/richa/PycharmProjects/ClimbOn/app/tutorial.db', echo=True)

#Create a session
Session = sessionmaker (bind=engine)
session = Session()

user = User("admin", "password", "richard@mail.com", "10")
session.add(user)

user = User("python", "python", "henrik@salt.org", "0")
session.add(user)

user = User("jumpiness", "python", "killme@napier.ac.uk", "5")
session.add(user)

# commit the record to the database
session.commit()

session.commit()