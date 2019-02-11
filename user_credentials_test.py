import unittest 
from user import User #, Credential

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
    


	def setUp(self):
		'''
		Function to create a user account before each test
		'''
        # self.new_contact =User("James","Muriuki","12") # create contact object
		self.new_user = User('Consolee','Umutoni','12')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of user instances is properly done
		'''
		self.assertEqual(self.new_user.first_name,'Consolee')
		self.assertEqual(self.new_user.last_name,'Umutoni')
		self.assertEqual(self.new_user.password,'12')

if __name__ == '__main__':
    unittest.main()
