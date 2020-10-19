# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:49:27 2020

@author: arnav
"""


import csv
from sqlalchemy import create_engine
from flask import Flask,render_template, request
from sqlalchemy.orm import scoped_session, sessionmaker
from main.py import main

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("signin.html")

username = request.form.get("crname")
password = request.form.get("crpassword")
db.execute('INSERT  INTO "user"(username,password) VALUES (%s, %s);',
           ("username","password"))

main()

    
