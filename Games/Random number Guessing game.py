#Advanced Number Guessing game made in Python
#define the functions
import random
def guess_num():
    print("You will be defining the range you would like the numbers to be in.")
    while True:
        try:
            num_one = int(input("Where do you want the range of numbers to start?"))
            num_two = int(input("Where do you want the range of numbers to end?"))
            num_two_plus_one = num_two + 1
            num_list = [n for n in range(num_one, num_two_plus_one)]
            answer = random.choice(num_list)
            user_number = input("What number do you think I am thinking of?")
            user_number_int = int(user_number)
            if (user_number_int == answer):
                print("You got it right! The number I was thinking of was " + str(answer) + "!")
            elif (user_number_int != answer):
                print("Sorry, you got it wrong. The number I was thinking of was " + str(answer) + "!" + " Better luck next time!")
        except ValueError:
            print("Sorry, I did not understand your response. Please enter numbers only.")
        except IndexError:
            print("You cannot have the range of numbers end at a number less than the starting number.")

#Program Starts
while True:
    while True:
        start_game = input("Would you like to play Guess The Number?")
        if (start_game.casefold()[0] == "y"):
            guess_num()
        elif (start_game.casefold()[0] == "n"):
            print("No")
        else:
            print("Sorry, I do not understand your answer. Please enter yes or no.")
