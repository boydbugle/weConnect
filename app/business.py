BUSINESS=[
            {
                'userid':1,
                'businessid':1,
                'businessname':'wishywashy',
                'businesscategory':'laundry',
                'businesslocation':'trm'
            }
]
class Business():

    def __init__(self):
        self.businessname=None
        self.businesscategory=None
        self.businesslocation=None

    def register_business(self,useremail,businessname,businesscategory,businesslocation):
            business = {
                'useremail':useremail,
                'businessid':BUSINESS[-1]['businessid'] + 1,
                'businessname':businessname,
                'businesscategory':businesscategory,
                'businesslocation':businesslocation
            }
            BUSINESS.append(business)
            return business

    # def get_single_business(self,businessid):
    #     business = [business for business in BUSINESS if BUSINESS['businessid'] == businessid]
    #     return business

    def update_business(self,businessid):
        business = [business for business in BUSINESS if BUSINESS['businessid'] == businessid and BUSINESS['useremail'] == useremail]
        business[0]['businessname'] = businessname
        business[0]['businesscategory'] = businesscategory
        business[0]['businesslocation'] = businesslocation
        return business

    def delete_business(self,businessid):
        business = [business for business in BUSINESS if BUSINESS['businessid'] == businessid]
        business.remove(business[0])
        return business
