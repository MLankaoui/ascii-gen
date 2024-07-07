from art import *
import sys
import time


"""
    to take the user name and return it
"""
def get_user_name():
    return input("what is your name : ")


"""
    to welcome the user to the app
"""
def welcome_message(name):
    
    sys.stdout.write(f'{text2art("hello " + name)}', )
    time.sleep(1)

"""
    displaying the options available to the user
"""
def options():
    sys.stdout.write("""
1- generating a random art
2- from text to draw
3- from text to art
4- wizard mode
""")
    return int(input("your option here : "))

"""
    the main function - entry point
"""
def main():
    welcome_message(get_user_name())
    optionn = options()

if __name__ == "__main__":
    main()