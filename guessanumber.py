
import random

hc = random.randrange(1, 101)

winner = False

counter = 0

while not winner:
    counter += 1  
    userInput = input("Enter a number: ")
    userNum = int(userInput)
    
    if hc > userNum:
        print("Your guess is too low!")
    elif hc < userNum:
        print("Your guess is too high!")
    else:
        print("You win!!")
        print("in "+ str(counter) + " tries")
        winner = True


    