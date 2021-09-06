import random
import time

user_choice = "yes"

while user_choice == "yes" or user_choice == "y":
    print ("Dice is rolling...")
    time.sleep(1)

    dice1= random.randint(1,6)
    dice2= random.randint(1,6)

    print ("Dice-1 value is : " ,dice1, "\nDice-2 value is : ", dice2)
    time.sleep(1)

    if(dice2 == dice1):
        print("Congrats.. you got same values")

    user_choice = input("Do you want to roll the dice again? (y/n)").lower() # YES, Yes, yes=yes, Y, y=y

print("Thank you for playing...")
