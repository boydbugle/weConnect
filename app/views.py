from flask import Flask,jsonify,abort,make_response,request,session
from app import app
from user import User,USERS
from business import Business,BUSINESS
import os

app.secret_key = os.urandom(24)
users=User()
business=Business()


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
    loggeduser = user[0]['id']
    session['useremail'] = user[0]['email']
    return make_response(jsonify({'userid': loggeduser}), 202)

@app.route('/weConnect/api/v1/logout', methods=['POST'])
def logout():
    session.pop('useremail', None)
    return make_response(jsonify({'status': 'logged out successful'}), 200)

@app.route('/weConnect/api/v1/resetpassword', methods=['POST'])
def reset_password():
    if not request.json:
        return make_response(jsonify({'error': 'Not acceptable'}), 406)
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    newpassword = data.get('newpassword')
    user = users.reset_password(email,password,newpassword)
    if len(user) != 0:
        user[0]['password'] = newpassword
    return make_response(jsonify({'message':'successful password reset'}), 201)

@app.route('/weConnect/api/v1/businesses', methods=['GET','POST'])
def register_business():
    if not request.json:
        return make_response(jsonify({'error': 'Not acceptable'}), 406)
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = users.register_user(email,password)
    user = users.login(email,password)
    loggeduser = user[0]['id']
    if loggeduser:
        if request.method == 'POST':
            data = request.get_json()
            userid = loggeduser,
            businessname = data.get('businessname')
            businesscategory = data.get('businesscategory')
            businesslocation = data.get('businesslocation')
            business.register_business(userid,businessname,businesscategory,businesslocation)
            return make_response(jsonify({'message': 'business created successfully'}), 201)
    return make_response(jsonify({'Business':BUSINESS}), 200)
