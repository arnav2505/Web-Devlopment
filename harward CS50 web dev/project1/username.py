# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:34:14 2020

@author: arnav
"""

import csv
from sqlalchemy import create_engine
from flask import Flask,render_template, request
from sqlalchemy.orm import scoped_session, sessionmaker
   

DATABASE_URL = "postgres://gksbuwapdhvfhd:b5503a647c34e177936fdf3993534262f73e5bff264cc5a37ce38ef5b0d95eab@ec2-46-137-84-140.eu-west-1.compute.amazonaws.com:5432/dchqt25uu70fd"

engine = create_engine(DATABASE_URL)

'''
engine.execute('CREATE TABLE "user" ('  
     'id SERIAL PRIMARY KEY,'
     'username VARCHAR NOT NULL,'
     'password VARCHAR NOT NULL);')
'''
db = scoped_session(sessionmaker(bind=engine))



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("input.html")
