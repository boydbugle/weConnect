import unittest
import json
import os
from app import app


"""Test for user API endpoints"""
class TestUserApiResponse(unittest.TestCase):
    def setUp(self):
        self.test = app.test_client()

    def tearDown(self):
        pass

    def register_user_helper(self,email="unique@unique",password="u#n~q"):
        credentials = {
            "email":email,
            "password":password
            }
        return self.test.post('/weConnect/api/v1/registeruser',
                headers={'Content-Type': 'application/json'},
                data=json.dumps(credentials)
               )

    def login_helper(self,email="unique@unique",password="u#n~q"):
        credentials = {
            "email":email,
            "password":password
            }
        return self.test.post('/weConnect/api/v1/login',
                headers={'Content-Type': 'application/json'},
                data=json.dumps(credentials)
               )

    def test_register_user(self):
        res = self.register_user_helper()
        resp = json.loads(res.data.decode())
        self.assertEqual(resp['message'],"successful registration")
        self.assertEqual(res.status_code, 201)

    def test_duplicate_registration_user(self):
        self.register_user_helper("unique.COM","unique","un#Que")
        register_res1 = self.register_user_helper(email="unique.COM",username="unique",password="un#Que")
        resp = json.loads(register_res1.data.decode())
        self.assertEqual(resp['message'],"user in existence")
        self.assertEqual(register_res1.status_code, 400)





if __name__ == '__main__':
    unittest.main()
