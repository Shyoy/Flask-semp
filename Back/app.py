
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"
 
db = SQLAlchemy(app)
 
# model
class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))
 
    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


app = Flask(__name__)

@app.route('/')
def show_all():
    res=[]
    # for student in students.query.all():
    return f"<p>{list(students.query.all())}</p>"

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"