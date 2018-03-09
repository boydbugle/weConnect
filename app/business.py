# BUSINESS = [
#     {
#         'useremail': "B@BUG.COM",
#         'businessid': 1,
#         'businessname': 'wishywashy',
#         'businesscategory': 'laundry',
#         'businesslocation': 'trm'
#     }
# ]


class Business():

    def __init__(self,  businessId,
                 businessName, businessCategory, businessLocation, userEmail):
        self.userEmail = userEmail
        self.businessId = businessId
        self.businessName = businessName
        self.businessCategory = businessCategory
        self.businessLocation = businessLocation

    def __str__(self):
        business = {'businessId': self.businessId,
                    'businessName': self.businessName,
                    'businessCategory': self.category,
                    'businessLocation': self.location,
                    'userEmail': self.userEmails
                    }
        return business
