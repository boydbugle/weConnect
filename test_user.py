import unittest
import json
import os
from app import app


"""Test for user API endpoints"""
class TestUserApiResponse(unittest.TestCase):
    def setUp(self):
        self.test = app.test_client()

    def register_user_helper(self,email='unique@unique',password='u#n~q'):
        credentials = {
            'email':email,
            'password':password
            }
        return self.test.post('/weConnect/api/v1/registeruser',
                headers={'Content-Type': 'application/json'},
                data=json.dumps(credentials)
               )

    def login_helper(self,email='unique@unique',password='u#n~q'):
        credentials = {
            'email':email,
            'password':password
            }
        return self.test.post('/weConnect/api/v1/login',
                headers={'Content-Type': 'application/json'},
                data=json.dumps(credentials)
               )

    def test_register_user(self):
        res = self.register_user_helper()
        result= json.loads(res.data.decode())
        self.assertEqual(result['message'],'successful registration')
        self.assertEqual(res.status_code, 201)

    def test_duplicate_registration_user(self):
        self.register_user_helper('unique.COM','un#Que')
        res2 = self.register_user_helper(email='unique.COM',password='un#Que')
        result = json.loads(res2.data.decode())
        self.assertEqual(result['error'],'user in existence')
        self.assertEqual(res2.status_code, 406)

    def test_cannot_login_unregistered_user(self):
        res = self.login_helper()
        result = json.loads(res.data.decode())
        self.assertEqual(result['error'],'Not an existing user or wrong credentials')
        self.assertEqual(res.status_code, 401)

    def test_can_login_in_registered_user(self):
        register_res = self.register_user_helper(email='me.COM',password='m@m%')
        register_result = json.loads(register_res.data.decode())
        self.assertEqual(register_res.status_code, 201)
        login_res = self.login_helper(email='me.COM',password='m@m%')
        login_result = json.loads(login_res.data.decode())
        loggeduserid = json.loads(login_res.data.decode())['userid']
        self.assertEqual(login_result['userid'],loggeduserid)
        self.assertEqual(login_res.status_code, 202)

    def test_wrong_login_password(self):
        register_res = self.register_user_helper(email='me.COM',password='m@m%')
        login_res = self.login_helper(email='me.COM',password='m@m')
        login_result = json.loads(login_res.data.decode())
        self.assertEqual(login_result['error'],'Not an existing user or wrong credentials')
        self.assertEqual(login_res.status_code, 401)

    def test_can_successfully_logout(self):
        res = self.test.post('/weConnect/api/v1/logout')
        logout_result = json.loads(res.data.decode())
        self.assertEqual(logout_result['status'],'logged out successful')
        self.assertEqual(res.status_code, 200)

    def test_reset_password(self):
        register_res = self.register_user_helper(email='me.COM',password='m@m%')
        login_res = self.login_helper(email='me.COM',password='m@m%')
        credentials = {
            'password':'m@m%',
            'newpassword':'m@m'
            }
        reset_res = self.test.post('/weConnect/api/v1/resetpassword',
                headers={'Content-Type': 'application/json'},
                data=json.dumps(credentials)
               )
        reset_result = json.loads(reset_res.data.decode())
        self.assertEqual(reset_result['message'],'successful password reset')
        self.assertEqual(reset_res.status_code, 201)



if __name__ == '__main__':
    unittest.main()
