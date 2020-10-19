# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:50:21 2020

@author: arnav
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = "postgres://gksbuwapdhvfhd:b5503a647c34e177936fdf3993534262f73e5bff264cc5a37ce38ef5b0d95eab@ec2-46-137-84-140.eu-west-1.compute.amazonaws.com:5432/dchqt25uu70fd"

engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

title2 = "Aztec"

bookl = db.execute('SELECT title FROM "Book"')

#bookl = db.execute('SELECT * FROM "Book" WHERE title = "{0}";'.format(title2))
