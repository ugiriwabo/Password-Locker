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

            User.user_list.remove(self)