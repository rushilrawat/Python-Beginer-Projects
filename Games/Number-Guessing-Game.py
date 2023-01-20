#Number Guessing Game

from getpass import getpass

Secret_Number = int(getpass("Please give a secret number:"))
Guess_Limit = int(input("Please give guess limit (ie. How many chances) :"))

print(F"Hint : The Secert Number is any number between {Secret_Number - 60} to {Secret_Number + 60}")
print(f"You have {Guess_Limit} Chances to Guess the Secret Number" )

while Guess_Limit != 0:
    Guess=int(input("Guess a number:"))
    Guess_Limit -= 1
    if Guess != Secret_Number:
        print(f"Wrong, Try Again! and be careful, You only have {Guess_Limit} Chances Left")
    elif Guess== Secret_Number:
        print(f"Your Guess was right, The secret Number was {Secret_Number}. You won the game!")
        break
else:
    print(f"Sorry! None of your guesses were right, The secret Number was {Secret_Number}. You failed!")
