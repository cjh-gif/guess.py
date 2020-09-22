from random import randint
from random import seed

def gameStart ():
    num = None
    min = None
    max = None
    numofGuesses = 0
    
    while (min == None):
        try:
            min = int(input("Please enter the minimum value: "))
        except ValueError:
            print("Please enter a valid integer.")
    
    while (max == None):
        try:
            max = int(input("Now please enter a maximum value: "))
        except ValueError:
            print("Please enter a valid integer.")
    
    seed()
    rand = randint(min,max)
    
    while (num != rand):
        try:
            num = int(input("Please make a guess:"))
        except ValueError:
            print ("Please enter an integer value.")
        if num > rand:
            print("Too big!")
        if num < rand:
            print("Too small!")
        numofGuesses += 1
    
    if numofGuesses == 1:
        finalString = "guess"
    else:
        finalString = "guesses"
    print("Congrats! You found the number(",rand,")!")
    print("And it only took you",numofGuesses,finalString,"to find it!")
    


gameStart()
