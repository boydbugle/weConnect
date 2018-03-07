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
                    "businesslocation":businesslocation
                }
        return self.test.post('/weConnect/api/v1/businesses',
                headers={'Content-Type': 'application/json',
                        'Authorization':'Bearer' + 'loggeduserid'},
                data=json.dumps(businessdata)
               )

    def test_can_register_business_successfully(self):
        business_req = self.register_business_helper()
        business_resp = json.loads(business_req.data.decode())
        self.assertEqual(business_resp['message'],"business created successfully")
        self.assertEqual(business_req.status_code, 201)

    def test_can_get_all_businesses(self):
        self.register_business_helper()
        res = self.test.get('/weConnect/api/v1/businesses')
        resp = json.loads(res.data.decode())
        self.assertTrue('Business')

    # def test_can_get_business_by_id(self):
    #     self.register_business_helper()


if __name__=='__main__':
    unittest.main()
