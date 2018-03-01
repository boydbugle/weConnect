class Phonebook(object):

    def __init__(self):
        self.phonebook={}

    def add_contact(self,name,number):
        self.phonebook[name]=number
        return self.phonebook

    def success_entry(self, name):
        return self.phonebook[name]

    def get_names(self):
        return self.phonebook.keys()

    def get_numbers(self):
        return self.phonebook.values()
