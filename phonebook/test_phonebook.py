from unittest import TestCase
from phonebook import Phonebook

class PhonebookTest(TestCase):

    def setUp(self):
        self.contact = Phonebook()

    def test_success_entry(self):
            # example showing use of two asserts in a test case
            self.contact.add_contact('whodat', '12345')
            self.assertIn('whodat', self.contact.get_names())
            self.assertIn('12345', self.contact.get_numbers())
            
    def test_success_match(self):
        self.contact.add_contact('Bbug', '077')
        self.assertEqual('077',self.contact.success_entry('Bbug'))

    def test_no_entry_of_name(self):
        self.assertEqual([],self.contact.get_names())

    def test_no_entry_of_number(self):
        self.assertEqual([],self.contact.get_numbers())
