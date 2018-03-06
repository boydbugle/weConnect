USERS=[
    {
                "id": 1,
                "username":"Bbug",
                "email":"B@BUG.COM",
                "password":"whoagain?"
            },
            {
                "id": 2,
                "username":"Lenti",
                "email":"L@NTI.COM",
                "password":"whodat?"
        }
]

class User():
    def __init__(self):
        self.email=None
        self.password=None

    def register_user(self,email,password):
        user = {
            "id":USERS[-1]['id'] + 1,
            "email":email,
            "password":password
        }
        USERS.append(user)
        return user

    def login(self,email,password):
        user = [user for user in USERS if user['email'] == email and user['password'] == password]
        return user

    def reset_password(self,email,password,newpassword):
        user = [user for user in USERS if user['email'] == email and user['password'] == password]
        if len(user) == 0:
            return 'fail'
        user[0]['password'] = newpassword
        return user
