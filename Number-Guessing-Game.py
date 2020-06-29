#Number Guessing Game
from getpass import getpass
Secret_Number = int(getpass("Please give a secret number:"))
Guess_Limit = int(input("Please give guess limit (ie. How many chances) :"))
Guess_Count = 0

print(F"Hint : The Secert Number is any number between {Secret_Number - 60} to {Secret_Number + 60}")

while Guess_Count != Guess_Limit:
    Guess=int(input("Guess a number:"))
    Guess_Count += 1
    if Guess != Secret_Number:
        print("Try Again!")
    elif Guess== Secret_Number:
        print(f"Your Guess was right, The secret Number was {Secret_Number}. You wont the game!")
        break
else:
    print(f"Sorry! None of your guesses were right, The secret Number was {Secret_Number}. You failed!")
