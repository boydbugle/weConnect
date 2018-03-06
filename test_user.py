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
    def test_userlist_get_allusers(self):
        res =self.test.get('/weConnect/api/v1/users')
        self.assertEqual(res.status_code, 200)

    def test_register_user(self):
        res = self.test.post('/weConnect/api/v1/registeruser', data=self.credentials)
        return self.test.post(
                '/weConnect/api/v1/registeruser',
                headers={'Content-Type': 'application/json'},
                data=json.dumps(self.credentials)
               )
        # self.assertEqual(res , data=json.dumps(self.credentials)

if __name__ == '__main__':
    unittest.main()
