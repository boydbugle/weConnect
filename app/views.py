import random
from flask import Flask, jsonify, abort, make_response, request, session
from app import app
from app.user import User, USERS
from app.business import Business

users = User()
# business = Business()
allBusinesses = []


@app.route('/weConnect/api/v1/registeruser', methods=['GET', 'POST'])
def register_user():
    data = request.get_json()
    if not request.json:
        return make_response(jsonify({'error': 'Not acceptable'}), 406)
    email = data.get('email')
    password = data.get('password')
    allemails = [i['email'] for i in USERS if 'email' in i]
    for e in allemails[:]:
        if e == email:
            return make_response(jsonify({'error': 'user in existence'}), 406)
    user = users.register_user(email, password)
    return make_response(jsonify({'message': 'successful registration'}), 201)


@app.route('/weConnect/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    if not request.json:
        return make_response(jsonify({'error': 'Not acceptable'}), 406)
    email = data.get('email')
    password = data.get('password')
    user = users.login(email, password)
    if user:
        loggeduser = user['email']
        return make_response(jsonify({
            'message': 'loggedin successfully',
            'token': loggeduser}), 202)
    else:
        return make_response(jsonify({
            'error': 'Not an existing user or wrong credentials'}), 401)


@app.route('/weConnect/api/v1/logout', methods=['POST'])
def logout():
    auth_header = request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    if token:
        token = ''
        return make_response(jsonify({'message': 'logged out successful',
                                      'token': token}), 200)


@app.route('/weConnect/api/v1/resetpassword', methods=['POST'])
def reset_password():
    data = request.get_json()
    if not request.json:
        return make_response(jsonify({'error': 'Not acceptable'}), 406)
    email = data.get('email')
    password = data.get('password')
    newpassword = data.get('newpassword')
    user = users.reset_password(email, password, newpassword)
    if user:
        reset = user['email']
        return make_response(jsonify({'message': 'successful password reset',
                                      'user': reset}), 201)
    else:
        return make_response(jsonify({
            'message': 'unsuccessful password reset'}), 201)


@app.route('/weConnect/api/v1/businesses', methods=['GET', 'POST'])
def register_business():
    auth_header = request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    print auth_header
    print token
    if request.method == 'POST':
        try:
            if token:
                data = request.get_json()
                useremail = token,
                businessname = data.get('businessname')
                businesscategory = data.get('businesscategory')
                businesslocation = data.get('businesslocation')
                biz = business.register_business(
                    useremail, businessname, businesscategory, businesslocation)
                return make_response(jsonify({
                    'message': 'business created successfully',
                    'business': biz['businessid']
                }), 201)
            return make_response(jsonify({'message': 'not created'}), 201)
        except Exception as e:
            response = {'message': str(e)}
            return response
    else:
        return make_response(jsonify({'Business': BUSINESS}), 200)


# @app.route('/weConnect/api/v1/businesses/<int:businessid>', methods=['GET', 'PUT', 'DELETE'])
# def update_business(businessid):
#     auth_header = request.headers.get('Authorization')
#     # token = auth_header.split(' ')[1]
#     if request.method == 'PUT':
#         if token:
#             data = request.get_json()
#             useremail = token,
#             businessname = data.get('businessname')
#             businesscategory = data.get('businesscategory')
#             businesslocation = data.get('businesslocation')
#             business.register_business(userid, businessname, businesscategory, businesslocation)
#             biz = business.update_business(
#                 useremail, businessid, businessname, businesscategory, businesslocation)
#             return make_response(jsonify({'message': 'successfully updated business',
#                                           'updated': biz
#                                           }), 200)
#     if request.method == 'DELETE':
#         if token:
#             usermail = token
#             biz = business.delete_business(usermail, businessid)
#             return make_response(jsonify({'message': 'successfully deleted business',
#                                           'business': biz
#                                           }), 200)


# @app.route('/weConnect/api/v1/businesses/<businessid>', methods=['GET'])
# def get_business(businessid):
#     # business = [business for business in BUSINESS if BUSINESS['businessid'] == businessid]
#     business = business.get_single_business(businessid)
#     return make_response(jsonify({'Business':business[0]}), 200)
