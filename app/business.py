BUSINESS=[
    {
                "userid":1,
                "businessid":1,
                "businessname":"wishywashy",
                "businesscategory":"laundry",
                "businesslocation":"trm",
                # "reviews"=[]

            }
]
class Business():

    def __init__(self):
        self.businessname=None
        self.businesscategory=None
        self.businesslocation=None

    def register_business(self,userid,businessname,businesscategory,businesslocation):
            business = {
                "userid":userid,
                "businessid":BUSINESS[-1]['businessid'] + 1,
                "businessname":businessname,
                "businesscategory":businesscategory,
                "businesslocation":businesslocation
            }
            BUSINESS.append(business)
            return business
