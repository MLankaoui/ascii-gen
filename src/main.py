from art import *
import sys
import time


"""
    to take the user name and return it
"""
def get_user_name():
    return input("what is your name")


"""
    to welcome the user to the app
"""
def welcome_message(name):
    
    sys.stdout.write(f'hello {name}')
    time.sleep(1)

def main():
    welcome_message(get_user_name())
    

if __name__ == "__main__":
    main()