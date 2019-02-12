#!/usr/bin/env python3.6

def main():
    print("Hello Welcome to your user list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new username, dc - display username, fc -find a username, ex -exit the users list ")

                    short_code = input().lower()

                    if short_code == 'cc':

                            print ("User name ....")
                            u_name= input()

                            print("Password ...")
                            password= input()

                            save_user(create_username(u_name,password)) # create and save new contact.
                            print ('\n')
                            print(f"New user {u_name} {password} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_user():
                                    print("Here is a list of all your username")
                                    print('\n')

                                    for user in display_user():
                                            print(f"{user.user_name} {user.Password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the username you want to search for")

                            search_user = input()
                            if check_existing_user(search_user):
                                    search_user = find_user(search_user)
                                    print(f"{search_user.first_name} {search_user.password}")
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