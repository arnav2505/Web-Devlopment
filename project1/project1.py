'''
import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from flask import Flask,render_template, request
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

DATABASE_URL = "postgres://gksbuwapdhvfhd:b5503a647c34e177936fdf3993534262f73e5bff264cc5a37ce38ef5b0d95eab@ec2-46-137-84-140.eu-west-1.compute.amazonaws.com:5432/dchqt25uu70fd"

#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))
'''
# import os

from flask import Flask, session, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from flask import Flask,render_template, request
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment 
DATABASE_URL = "postgres://gksbuwapdhvfhd:b5503a647c34e177936fdf3993534262f73e5bff264cc5a37ce38ef5b0d95eab@ec2-46-137-84-140.eu-west-1.compute.amazonaws.com:5432/dchqt25uu70fd"
'''
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")
'''
# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

'''
@app.route("/")
def index():
    return "Project 1: TODO"
'''

@app.route("/")
def index():
    return render_template("input.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signin", methods = ['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get("crname")
        password = request.form.get("crpassword") 
        db.execute('INSERT  INTO "user" (username,password) VALUES (:username,:password)',\
                   {"username" : username , "password" : password})            
        db.commit()
        return render_template('succes.html')    
    return render_template("signin.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("name")
        password = request.form.get("password")
        if db.execute('SELECT * FROM "user" WHERE username=:username AND password = :password',\
                     {"username": username ,"password":password}).rowcount == 0:
            return render_template("error.html")

        return redirect("/search")
              
    return render_template("login.html")


@app.route("/search", methods = ['GET','POST'])
def search():
    if request.method == 'POST':
        title2=request.form.get("title1") 
        if title2!=None:
            booklist=db.execute("""SELECT * FROM "Book" WHERE title LIKE '{0}%'""".format(title2))
            return render_template('search.html', booklist=booklist)
    booklist = db.execute('SELECT * FROM  "Book" WHERE ID<51').fetchall()
    print("search book list ", len(booklist))
    return render_template('search.html', booklist=booklist)

@app.route("/review/<string:ISBN>", methods = ['GET','POST'])
def review(ISBN):
    
    print("ISBN aa gaya")
    print(ISBN)
    if db.execute("""SELECT * FROM "Book" WHERE isbn LIKE '{0}%'""".format(ISBN)).rowcount == 0:
        print("not found")
    print("found it !!!")
    review_book=db.execute("""SELECT * FROM "Book" WHERE isbn LIKE '{0}%'""".format(ISBN)).fetchall()
    for review_book_first in review_book:
        print(review_book_first.author)
        import requests
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "1Ye0t8LjwsWpLDRxXTsEw", "isbns": ISBN})
        res1 = res.json()
        review_book1 = dict(review_book_first.items())
        review_book1['reveiw']=str(res1['books'][0]['reviews_count'])
        review_book1['rateing']=str(res1['books'][0]['average_rating'])
        return render_template('review.html', review_book=review_book1)
    print(review_book_first[0].title)
    '''    
    #review_book_temp = dict(review_book.items())
    print(review_book.author)
    '''
    print("got isbn list")
    return render_template('review.html', review_book=review_book)
'''
@app.route("/update_review", methods = ['GET','POST'])
def update_review():
    rate=requests.form.get(rate)
    boook2['rateing']=((boook2['rateing']*boook2['reveiw'])+rate2)/(boook2['reveiw']+1)
    boook2['reveiw']+=1
'''
if __name__ == '__main__':
   app.run()



