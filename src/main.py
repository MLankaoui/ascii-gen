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
    handling user options
"""
def option_handler(option):
    if option == 1: #the first option random art
        gen_random(input("write random : ").lower())

    
    if option == 2: #from text to draw
        text_to_draw(input("enter a word like: coffee, man, woman... : "), int(input("and how many : ")))

    
    if option == 3: #from text to art
        pass

    
    if option == 4: # wizard mode
        pass

"""
    generate random art
"""
def gen_random(string: str):
    print(randart())


"""
    text to draw function
"""
def text_to_draw(text: str, number: int):
    sys.stdout.write(art(text, number) + "\n")


"""
    the main function - entry point
"""
def main():
    welcome_message(get_user_name())
    optionn = options()
    option_handler(option=optionn)

if __name__ == "__main__":
    main()