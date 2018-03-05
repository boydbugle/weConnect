from flask import Flask,jsonify,abort,make_response,request
from user import User

app = Flask(__name__)

USERS=User()

@app.route('/weConnect/api/v1/users', methods=['GET'])
def get_users():
    allusers = USERS.get_users()
    return jsonify({"users":allusers})

@app.route('/weConnect/api/v1/users', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    user = USERS.create_user(username,email,password)
    if not request.json or not 'email' in request.json:
        abort(400)
    return jsonify({'user':user})


if __name__=='__main__':
    app.run(debug=True)
