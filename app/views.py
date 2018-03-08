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
    loggeduser = user[0]['email']
    session['useremail'] = user[0]['email']
    return make_response(jsonify({'useremail': loggeduser}), 202)

@app.route('/weConnect/api/v1/logout', methods=['POST'])
def logout():
    session.pop('useremail', None)
    return make_response(jsonify({'status': 'logged out successful'}), 200)

@app.route('/weConnect/api/v1/resetpassword', methods=['POST'])
def reset_password():
    data = request.get_json()
    if not request.json:
        return make_response(jsonify({'error': 'Not acceptable'}), 406)
    email = data.get('email')
    password = data.get('password')
    newpassword = data.get('newpassword')
    user = users.reset_password(email,password,newpassword)
    if len(user) != 0:
        user[0]['password'] = newpassword
    return make_response(jsonify({'message':'successful password reset'}), 201)

@app.route('/weConnect/api/v1/businesses', methods=['GET','POST'])
def register_business():
    auth_header = request.headers.get('Authorization')
    loggeduser = auth_header.split(' ')[1]
    if request.method == 'POST':
        # if request.json:
        #     data = request.get_json()
        #     email = data.get('email')
        #     password = data.get('password')
        #     user = users.register_user(email,password)
        #     user = users.login(email,password)
        #     loggeduser = user[0]['id']
        if loggeduser:
            data = request.get_json()
            useremail = loggeduser,
            businessname = data.get('businessname')
            businesscategory = data.get('businesscategory')
            businesslocation = data.get('businesslocation')
            business.register_business(useremail,businessname,businesscategory,businesslocation)
            return make_response(jsonify({'message': 'business created successfully'}), 201)
    else:
        return make_response(jsonify({'Business':BUSINESS}), 200)


# @app.route('/weConnect/api/v1/businesses/<int:id>', methods=['GET','PUT','DELETE'])
# def update_business(businessid):
    # business = business.update_business(businessid)
    # task = [task for task in tasks if task['id'] == task_id]
    # if len(task) == 0:
    #     abort(404)
    # if not request.json:
    #     abort(400)
    # if 'title' in request.json and type(request.json['title']) != unicode:
    #     abort(400)
    # if 'description' in request.json and type(request.json['description']) is not unicode:
    #     abort(400)
    # if 'done' in request.json and type(request.json['done']) is not bool:
    #     abort(400)
    # business[0]['businessname'] = request.json.get('businessname', business[0]['title'])
    # business[0]['businesscategory'] = request.json.get('businesscategory', business[0]['businesscategory'])
    # business[0]['businesslocation'] = request.json.get('businesslocation', business[0]['businesslocation'])
    # return jsonify({'business': business[0]})
    # if request.method == 'PUT':
    #     if request.json:
    #         data = request.get_json()
    #         email = data.get('email')
    #         password = data.get('password')
    #         user = users.register_user(email,password)
    #         user = users.login(email,password)
    #         loggeduser = user[0]['id']
    #         if loggeduser:
    #             data = request.get_json()
    #             userid = loggeduser,
    #             businessname = data.get('businessname')
    #             businesscategory = data.get('businesscategory')
    #             businesslocation = data.get('businesslocation')
    #             business.register_business(userid,businessname,businesscategory,businesslocation)
    #             newbusinessname = data.get('businessname')
    #             newbusinesscategory = data.get('businesscategory')
    #             newbusinesslocation = data.get('businesslocation')
    #             business = business.update_business(userid,businessname,businesscategory,businesslocation)
                # if len(updatedbiz) != 0:
                #     business[0]['businessname'] = businessname
                #     business[0]['businesscategory'] = businesscategory
                #     business[0]['businesslocation'] = businesslocation
                # return make_response(jsonify({'message':'successful password reset'}), 201)
@app.route('/weConnect/api/v1/businesses/<businessid>', methods=['GET'])
def get_business(businessid):
    # business = [business for business in BUSINESS if BUSINESS['businessid'] == businessid]
    business = business.get_single_business(businessid)
    return make_response(jsonify({'Business':business[0]}), 200)
