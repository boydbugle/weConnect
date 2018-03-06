import unittest
import json
import os
from app import app

# from user import User
"""Test for user response"""
class TestUserApiResponse(unittest.TestCase):
    def setUp(self):
        self.test = app.test_client()
        self.credentials = {
            # "id": USERS[-1]['id'] + 1,
            "username":"unique",
            "email":"unique.COM",
            "password":"whodat?"
        }

    def register_user_helper(self,email="unique.COM",username="unique",password="un#Que"):
        credentials = {
            "username":username,
            "email":email,
            "password":password
            }
        return self.test.post('/weConnect/api/v1/registeruser',
                headers={'Content-Type': 'application/json'},
                data=json.dumps(credentials)
               )

    def login_helper(self,email="unique.COM",password="un#Que"):
        credentials = {
            "email":email,
            "password":password
            }
        return self.test.post('/weConnect/api/v1/login',
                headers={'Content-Type': 'application/json'},
                data=json.dumps(credentials)
               )
    def test_userlist_get_allusers(self):
        res =self.test.get('/weConnect/api/v1/users')
        self.assertEqual(res.status_code, 200)

    def test_register_user(self):
        res = self.register_user_helper()
        self.assertEqual(res.status_code, 201)

    # def test_duplicate_registration_user(self):
    #     self.register_user_helper("unique.COM","unique","un#Que")
    #     register_res1 = self.register_user_helper(email="unique.COM",username="unique",password="un#Que")
    #     self.assertEqual(register_res1.status_code, 400)

    def test_cannot_login_unregistered_user(self):
        res = self.login_helper()
        self.assertEqual(res.status_code, 401)

    def test_can_login_in_registered_user(self):
        res = self.register_user_helper(email="me.COM",username="mimi",password="m@m%")
        self.assertEqual(res.status_code, 201)
        res = self.login_helper(email="me.COM",password="m@m%")
        self.assertEqual(res.status_code, 202)

    def test_wrong_login_password(self):
        res = self.register_user_helper(email="me.COM",username="mimi",password="m@m%")
        self.assertEqual(res.status_code, 201)
        res = self.login_helper(email="me.COM",password="m@m")
        self.assertEqual(res.status_code, 401)




if __name__ == '__main__':
    unittest.main()
