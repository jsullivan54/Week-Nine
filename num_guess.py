#Name: Johnathan Sullivan
#Lab9part2
#10/27/24
import random as r

def main():
# Generate the random number
    my_choice = number_gen()
    # Total # of Guesses
    total_guesses = 0
#Boolean True to continue guessing
    keep_going = True
#Enter my doomsday guessing game
    print("Welcome to my Horrific Guessing Game!")
    print("Should, you want to live. Pick a number between 1 and 50.")
#Ask the user to input a number
    while keep_going:
        user_input = input("Enter your guess (or die): ")

# Validate user input using boolean expressions
        valid_number = user_input != ''
#Another loop for checking/ making input integers
        if valid_number:
            user_guess = int(user_input)
            if 1 <= user_guess <= 50:
                total_guesses += 1
                keep_going = guess_check(user_guess, my_choice)
            else:
                print("Please enter a number between 1 and 50, or by midnight tonight you'll get several spam email chains")
        else:
            print("Please enter a valid number. Don't push us.")

    print(f"You made a total of {total_guesses} guesses. Don't quit you day job.")
# Generate a random number between 1 and 50 Function 1
def number_gen():
    return r.randint(1, 50)


# Function 2 check the guess
def guess_check(user_guess, random_number):
    if user_guess == random_number:
        print(f"You've guessed correctly! The number was {random_number}. YOU GET TO LIVE!")
        return False  # Stop guessing
    elif user_guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    return True  # Continue guessing

main()
