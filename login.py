import pyfiglet
import os
import sys


def login():
    # you need to read it only once, not every loop
    users = open('users.txt').read().split('\n')
    for i in range(len(users)): users[i] = users[i].split('|')

    # Now what you want is to loop infinitely
    # until you get correct username/password
    # instead of recursive calling this
    # function over and over again

    while True:
        print('Welcome to the Password Manager')
        # clear the screen
        os.system('clear')

        username = str(input('Username: '))
        password = str(input('Password: '))
    
        for user in users:
            # uname = user[0]
            # pword = user[1]
            
            # here we search a user through SEARCH tech.
            # ....
            uname = ''.join(user[0].split())
            pword = ''.join(user[1].split())
            
            if uname == username and pword == password:
                print('Hello ' + user[1] + '.')
                print('You are logged in as: ' + user[0] + '.')
                # return to the main_menu()
                return main_menu()

            else:
                # if none of the records mathched the input
                print('\n\tWrong Username or Password...!')
                print('\tTry again...\n')
                return False 

def main_menu():
    # trying to clear the screen
    os.system('clear')

    print('\n\t\tWelcome to the Script\n')

    # clear and exit
    os.system('clear') or sys.exit()

def about():
    # this function show to the information 
    # about the script and its functionality
    return 0

def credits():
    # this is all credits shows to the user
    # for this script blblblbla
    return 0

def main():
    
    result = pyfiglet.figlet_format('PasswordManager')
    print(result)

    while True:
        print('1.Login \t2.About \t3.Credits \t0.Exit')
        choice = input()
        
        if choice=='1':
            # login into the Main_menu
            login()
            # return False
        elif choice=='2':
            # about section
            about() 
        elif choice=='3':
            # credit section
            credits()
        elif choice=='0':
            # clear and exit
            os.system('clear') or sys.exit()
        else:
            print('\n\tTry again...\n')
    # return 0

if __name__ == "__main__":
    os.system('clear') or main()
   