import unittest
import json
import os
from app import app

class TestBusinessApiResponse(unittest.TestCase):

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
    def register_business_helper(self,businessname="wishywashy",businesscategory="laundry",businesslocation="trm"):
        self.register_user_helper()
        login_req = self.login_helper()
        loggeduserid = json.loads(login_req.data.decode())['userid']
        businessdata = {
                    "userid":loggeduserid,
                    "businessname":businessname,
                    "businesscategory":businesscategory,
                    "businesslocation":businesslocation,
                }
        return self.test.post('/weConnect/api/v1/registerbusiness',
                headers={'Content-Type': 'application/json'},
                data=json.dumps(businessdata)
               )

    def test_can_register_business_successful(self):
        business_req = self.register_business_helper()
        business_resp = json.loads(business_req.data.decode())
        self.assertEqual(business_resp['message'],"business created successfully")
        self.assertEqual(login_req.status_code, 201)

    def test_get_all_business(self):
        self.register_business_helper()
        res = self.test.get('/weConnect/api/v1/business')
        res = json.loads(res.data.decode())
        self.assertEqual(res.status_code,200)
        self.assertTrue(business)

if __name__=='__main__':
    unittest.main()
