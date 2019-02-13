class User:
	"""
	Class to create user accounts and save their information
	"""
	users_list = [] #Empty users
    
	def __init__(self,user_name,password):
			

			# instance variables
			self.user_name = user_name
			self.password = password

	def save_user(self):

			User.users_list.append(self)

	def delete_user(self):
			'''
			delete_contact method deletes a saved contact from the contact_list
			'''

			User.users_list.remove(self)

	@classmethod
	def find_user_by_user_name(cls,user_name):
			'''
			Method that takes in a number and returns a contact that matches that number.

			Args:
				number: Phone number to search for
			Returns :
				Contact of person that matches the number.
			'''

			for user in cls.users_list:
				if user.user_name == user_name:
					return user

	@classmethod
	def user_exist(cls,user_name):
			'''
			Method that checks if a contact exists from the contact list.
			Args:
				number: Phone number to search if it exists
			Returns :
				Boolean: True or false depending if the contact exists
			'''

			for user in cls.users_list:
				if user.user_name == user_name:
						return True

			return False

	@classmethod
	def display_user(cls):
			'''
			method that returns the contact list
			'''
			return cls.users_list