
# import datetime
from dataclasses import dataclass
from datetime import datetime , timedelta
import time
import json
import jwt
from  werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime
from flask.helpers import datetime
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "super_duper_secretKEy%$!@JWT@()"

CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://poc-todo.netlify.app"]}})

db = SQLAlchemy(app)




# Database ORMs
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(70), unique = True)
    password = db.Column(db.String(80))
 
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

@app.route('/token')
def get_token():
    auth = request.authorization
    print(auth)
    if auth and auth.password == 'password':
        token = jwt.encode({
            'user':auth.username,
            'exp':datetime.utcnow()+ timedelta(minutes=5),
            }, app.config['SECRET_KEY'])
        print(token)
        return jsonify({'token':token})
    return make_response('could not verify!', 401, {'WWW-Authnticate': 'Basic realm="Login Required"'})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)