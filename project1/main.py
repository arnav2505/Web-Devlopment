# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:40:14 2020

@author: arnav
"""


def main():
    import csv
    from sqlalchemy import create_engine
    from flask import Flask,render_template, request
    from sqlalchemy.orm import scoped_session, sessionmaker
    from main.py import main
    
    app = Flask(__name__)
    
    @app.route("/")
    def index:
        title=request.form.get(title1)
        
        book = db.execute("SELECT * FROM books WHERE ")
        return render_template(main.html,book)
    