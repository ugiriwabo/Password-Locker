class User:
	'''
	Class to create user accounts and save their information
	'''
	users_list = []
    
	def __init__(self,username,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.username=username
		self.password=password