from flask import Flask,jsonify,abort,make_response,request,session
from app import app
from user import User,USERS
import os

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
    # return jsonify({'user':user}), 201
