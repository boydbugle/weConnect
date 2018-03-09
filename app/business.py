BUSINESS = [
    {
        'useremail': "B@BUG.COM",
        'businessid': 1,
        'businessname': 'wishywashy',
        'businesscategory': 'laundry',
        'businesslocation': 'trm'
    }
]


class Business():

    def __init__(self):
        self.businessname = None
        self.businesscategory = None
        self.businesslocation = None

    def register_business(self, useremail, businessname,
                          businesscategory, businesslocation):
        business = {
            'useremail': useremail,
            'businessid': BUSINESS[-1]['businessid'] + 1,
            'businessname': businessname,
            'businesscategory': businesscategory,
            'businesslocation': businesslocation
        }
        BUSINESS.append(business)
        return business

    def update_business(self, useremail, businessid, businessname,
                        businesscategory, businesslocation):
        for business in BUSINESS:
            if business['businessid'] == businessid and business['useremail'] == useremail:
                business['businessname'] = businessname
                business['businesscategory'] = businesscategory
                business['businesslocation'] = businesslocation
                BUSINESS.update(business)
                return business

    def delete_business(self, useremail, businessid):
        for business in BUSINESS:
            if business['businessid'] == businessid:
                if business[useremail] == useremail:
                    BUSINESS.remove(business)
                    return True
