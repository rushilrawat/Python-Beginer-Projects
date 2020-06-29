#Number Guessing Game

Secret_Number=int(input("Please give a secret number:"))
Max_Number_Limit=int(input("Please give the maximun number limit"))
Lowest_Number_Limit=int(input("Please give the lowest number limit"))
Guess_Limit= int(input("Please give guess limit:"))
Guess_Count=0
print(F"Hint : The Secert Number is between {Lowest_Number_Limit} to {Max_Number_Limit}")
while Guess_Count != Guess_Limit:
    Guess=int(input("Guess a number:"))
    Guess_Count += 1
    if Guess != Secret_Number:
        print("Try Again!")
    elif Guess== Secret_Number:
        print("You wont the game!")
        break
