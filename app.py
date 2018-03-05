from flask import Flask,jsonify,abort,make_response,request,session
from user import User,USERS

app = Flask(__name__)
# Session(app)
users=User()

@app.route('/weConnect/api/v1/users', methods=['GET'])
def get_users():
    return jsonify({"users":USERS})

@app.route('/weConnect/api/v1/users', methods=['POST'])
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
    return jsonify({'user':user})

@app.route('/weConnect/api/v1/login', methods=['POST'])
def login():
    # Session['id']=
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    users = USERS.get_users()
    user = [user for user in users if user['id'] == user_id]

if __name__=='__main__':
    app.run(debug=True)
