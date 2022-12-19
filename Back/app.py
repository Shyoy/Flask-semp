
# import datetime
from dataclasses import dataclass
import time
import json
# from datetime import datetime
from flask.helpers import datetime
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "super_duper_secretKEy%$!@JWT@()"

CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://poc-todo.netlify.app"]}})

db = SQLAlchemy(app)
 
# model
@dataclass
class Todo(db.Model):
    id:int
    title:str
    desc:str
    date_added:datetime
    done:bool

    id = db.Column('todo_id', db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    desc = db.Column(db.Text, nullable=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    done = db.Column(db.Boolean,default=False, nullable=True)
 
    def __init__(self, title:str, desc=''):
        self.title = title
        self.desc = desc
    def __repr__(self):
        return f'Todo: {self.title}'


@app.route('/todos/',methods=['POST','GET'])
def all_todos():
    if request.method == 'GET':
        return  jsonify(Todo.query.all())
    if request.method == 'POST':
        todo = Todo(**request.json)
        print(request.get_json())
        db.session.add(todo)
        db.session.commit()
        return 'Todo added successfully'

@app.route('/todos/<id>',methods=['PUT','GET','DELETE'])
def todo(id):
    if request.method == 'GET':
        return  jsonify(Todo.query.get_or_404(id))

    if request.method == 'PUT':
        todo = Todo.query.get_or_404(id)
        for key,val in request.json.items():
            if hasattr(todo,key) and key not in ['id', 'date_added']:
                setattr(todo, key, val)
        db.session.commit()
        return jsonify([todo])

    if request.method == 'DELETE':
        todo = Todo.query.get_or_404(id)
        db.session.delete(todo)
        db.session.commit()
        return f'DELETE id:{id} successfully'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)