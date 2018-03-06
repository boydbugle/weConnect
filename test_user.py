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
        req = self.register_user_helper()
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['message'],"successful registration")
        self.assertEqual(req.status_code, 201)

    def test_duplicate_registration_user(self):
        self.register_user_helper("unique.COM","un#Que")
        register_res1 = self.register_user_helper(email="unique.COM",password="un#Que")
        resp = json.loads(register_res1.data.decode())
        self.assertEqual(resp['error'],"user in existence")
        self.assertEqual(register_res1.status_code, 406)

    def test_cannot_login_unregistered_user(self):
        req = self.login_helper()
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['error'],"Not an existing user")
        self.assertEqual(req.status_code, 401)

    def test_can_login_in_registered_user(self):
        register_req = self.register_user_helper(email="me.COM",password="m@m%")
        register_resp = json.loads(register_req.data.decode())
        self.assertEqual(register_req.status_code, 201)
        login_req = self.login_helper(email="me.COM",password="m@m%")
        login_resp = json.loads(login_req.data.decode())
        self.assertEqual(login_resp['logged in'],"me.COM")
        self.assertEqual(login_req.status_code, 202)

    def test_can_successfully_logout(self):
        req = self.test.post('/weConnect/api/v1/logout')
        logout_resp = json.loads(req.data.decode())
        self.assertEqual(logout_resp['status','logged out successful'])
        self.assertEqual(req.status_code, 200)

if __name__ == '__main__':
    unittest.main()
