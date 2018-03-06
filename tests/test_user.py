import unittest
import json
import os
from app import app

# from user import User
"""Test for user response"""
class TestUserApiResponse(unittest.TestCase):
    def setUp(self):
        self.client = self.app.test_client
        self.credentials = {
            # "id": USERS[-1]['id'] + 1,
            "username":"Lenti",
            "email":"L@NTI.COM",
            "password":"whodat?"
        }
    def test_userlist_get_allusers(self):
        res =self.client().get('/weConnect/api/v1/users')
        self.assertEqual(res.status_code, 200)
