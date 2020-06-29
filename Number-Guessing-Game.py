#Number Guessing Game

Secret_Number = int(input("Please give a secret number:"))
Guess_Limit = int(input("Please give guess limit (ie. How many chances) :"))
Guess_Count = 0

print(F"Hint : The Secert Number is between {Secret_Number - 50} to {Secret_Number + 50}")

while Guess_Count != Guess_Limit:
    Guess=int(input("Guess a number:"))
    Guess_Count += 1
    if Guess != Secret_Number:
        print("Try Again!")
    elif Guess== Secret_Number:
        print("You wont the game!")
        break
