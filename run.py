#!/usr/bin/env python3.6
from user_credentials_test import User

def create_username(u_name, p_password):
	'''
	Function to create a new user account
	'''
	new_user = User(u_name,p_password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)

def display_user_name(user_name):
	'''
	Function to display user saved by a user
	'''
	User.display_user_name(user_name)


def main():
    print("Hello Welcome to your user list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cu - create a new username, du - display username, fu -find a username, ex -exit the users list ")

                    short_code = input().lower()

                    if short_code == 'cu':

                            print ("User name ....")
                            u_name= input()

                            print("Password ...")
                            password= input()

                            save_user(create_username(u_name,password)) # create and save new contact.
                            print ('\n')
                            print(f"New user {u_name} {password} created")
                            print ('\n')

                    elif short_code == 'du':

                            if display_user_name(user_name):
                                    print("Here is a list of all your username")
                                    print('\n')

                                    for user in display_user_name():
                                            print(f"{user.user_name} {user.Password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any user saved yet")
                                    print('\n')

                    elif short_code == 'fu':

                            print("Enter the username you want to search for")

                            search_user = input()
                            if check_existing_user(search_user):
                                    search_user = find_user(search_user)
                                    print(f"{search_user.u-name} {search_user.password}")
                                    print('-' * 20)
                            else:
                                    print("That user does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()