from flask import Flask,jsonify,abort,make_response,request,session
from app import app
from user import User,USERS
import os

app.secret_key = os.urandom(24)

users=User()
@app.route('/weConnect/api/v1/users', methods=['GET'])
def get_users():
    return jsonify({"users":USERS}), 200

@app.route('/weConnect/api/v1/registeruser', methods=['GET','POST'])
def register_user():
    if not request.json:
        abort(400)
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    allemails=[i['email'] for i in USERS if 'email' in i]
    allnames=[i['name'] for i in USERS if 'name' in i]
    for e in allemails[:]:
        if e == email:
            abort(400)
    for u in allnames[:]:
        if u == username:
            abort(400)
    user = users.register_user(username,email,password)
    return jsonify({'user':user}), 201

@app.route('/weConnect/api/v1/login', methods=['POST'])
def login():
    if not request.json:
        abort(400)
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = users.login(email,password)
    if len(user) == 0:
        return jsonify({'status':"not logged"}), 401
    session['useremail'] = user[0]['email']
    # if 'useremail' in session:
    useremail = session['useremail']
    return jsonify({'loggedin':useremail}), 202


@app.route('/weConnect/api/v1/logout', methods=['POST'])
def logout():
    session.pop('useremail', None)
    return jsonify({'status':"logged out successful"}), 200

@app.route('/weConnect/api/v1/resetpassword', methods=['POST'])
def reset_password():
    if not request.json:
        abort(400)
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    newpassword = data.get('newpassword')
    user = users.reset_password(email,password,newpassword)
    return jsonify({'user':user}), 200
