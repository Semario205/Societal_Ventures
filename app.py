from functools import wraps
from bson.objectid import ObjectId
from flask import Flask, render_template, jsonify, request, redirect, session, abort, flash
from flask_pymongo import PyMongo
from flask_session import Session
from passlib.hash import pbkdf2_sha256
import pymongo
from config import Config, db

app = Flask("Congressional App Challenge")
app.config.from_object(Config)
Session(app)

# Routes that load a html page
@app.route('/', methods=['GET']) # Has the url "/" and specify that this is only for getting a page
def example():
    return render_template("example.html")
@app.route('/login', methods=['GET']) # Has the url "/" and specify that this is only for getting a page
def login():
    return render_template("login.html")
@app.route('/signup', methods=['GET']) 
def signup():
    return render_template("signup.html")
@app.route('/addblog', methods=['GET']) 
def blog():
    return render_template("addblog.html")


# # Routes that are used when the client (frontend) sends over data
# @app.route('/api/login', methods=['POST']) # Has the url "/api/login" and specify that this is only for when user is posting/sending data
# def api_login():
#     pass

if __name__ == "__main__":
    app.config['SECRET_KEY'] = '123qwi34iWge9era89F1393h3gwJ0q3'
    app.run(debug=True)