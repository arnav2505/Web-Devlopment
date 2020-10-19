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

def index():
    return render_template("login.html")

username = request.form.get("name")
password = request.form.
@app.route("/")get("password")
if db.execute("SELECT * FROM flights WHERE username=:username", {"username": username} AND password = :password", {"password":password}).rowcount == 0:
    return render_template("error.html")

main()

    
