from flask import Flask,jsonify,abort,make_response,request,session
from app import app
from user import User,USERS
import os

app.secret_key = os.urandom(24)
users=User()

@app.route('/weConnect/api/v1/registeruser', methods=['GET','POST'])
def register_user():
    if not request.json:
        return make_response(jsonify({'error': 'Not acceptable'}), 406)
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    allemails=[i['email'] for i in USERS if 'email' in i]
    for e in allemails[:]:
        if e == email:
            return make_response(jsonify({'error': 'user in existence'}), 406)
    user = users.register_user(email,password)
    return make_response(jsonify({'message': 'successful registration'}), 201)

@app.route('/weConnect/api/v1/login', methods=['POST'])
def login():
    if not request.json:
        return make_response(jsonify({'error': 'Not acceptable'}), 406)
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = users.login(email,password)
    if len(user) == 0:
        return make_response(jsonify({'error': 'Not an existing user or wrong credentials'}), 401)
    session['useremail'] = user[0]['email']
    return make_response(jsonify({'logged in': session['useremail']}), 202)

@app.route('/weConnect/api/v1/logout', methods=['POST'])
def logout():
    session.pop('useremail', None)
    return make_response(jsonify({'status': 'logged out successful'}), 200)
