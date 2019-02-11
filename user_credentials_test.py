import unittest 
from user import User

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
		self.new_user=User('sandrine','12')

	def __init__(self,user_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = user_name
		self.password = password

if __name__ == '__main__':
    unittest.main()
