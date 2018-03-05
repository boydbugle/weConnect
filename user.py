from flask import Flask,request

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
        self.username=None
        self.email=None
        self.password=None

    def get_users(self):
        return USERS

    def create_user(self,username,email,password):
        user = {
            "id":USERS[-1]['id'] + 1,
            "username":username,
            "email":email,
            "password":password
        }
        USERS.append(user)
        return user
