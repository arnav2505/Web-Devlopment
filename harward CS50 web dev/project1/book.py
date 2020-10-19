# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:59:40 2020

@author: rajgu
"""
import csv
import os 
import sqlalchemy
from sqlalchemy import create_engine
   

DATABASE_URL = "postgres://gksbuwapdhvfhd:b5503a647c34e177936fdf3993534262f73e5bff264cc5a37ce38ef5b0d95eab@ec2-46-137-84-140.eu-west-1.compute.amazonaws.com:5432/dchqt25uu70fd"

engine = create_engine(DATABASE_URL)

engine.execute( 'CREATE TABLE "Book" (' 
     'id SERIAL PRIMARY KEY,'
     'title VARCHAR NOT NULL,'
     'author VARCHAR NOT NULL,'
     'publication_year INTEGER NOT NULL,'
     'isbn VARCHAR NOT NULL,'
     'reveiw VARCHAR,'
     'rateing INTEGER);')


f = open("books.csv")
reader = csv.reader(f)
next(reader)

'''
for isbn,title,author,publication_year in reader:
    engine.execute('INSERT INTO "Book" (title, author, isbn, publication_year) VALUES (:title, :author, :isbn, :publication_year);',
               {"title":title, "author":author,"isbn":isbn,"publication_year":publication_year})

for isbn,title,author,publication_year in reader:
    engine.execute('INSERT INTO "Book" (isbn,title, author,publication_year) VALUES (isbn, title, author,publication_year)')
               {"title":title, "author":author,"ISBN":isbn,"publication_year":publication_year})
'''
for isbn,title,author,publication_year in reader:
    engine.execute('INSERT INTO "Book" (title, author, isbn, publication_year) VALUES (%s, %s, %s, %s);',
               (title, author,isbn,publication_year))

#engine.execute( 'DROP TABLE "Book"')