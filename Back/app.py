from flask import Flask
import sqlite3
# pip install flask_


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"