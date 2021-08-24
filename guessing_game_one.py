import random
def guessing_game_one():
    computer_choice = random.randint(2, 9)
    number_of_guesses = 0
    print(computer_choice)
    new_game = True
    while new_game:
        new_game = input("Enter a number or type exit.")
        if new_game == 'exit':
            new_game = False
        else:
            number_of_guesses += 1
            user_number = int(new_game)
            new_game = True  
            if user_number == computer_choice:
                print("You guessed the right number")
                print(f"You took {number_of_guesses} guesses")
                number_of_guesses = 0
                computer_choice = random.randint(2, 9)
            elif user_number > computer_choice:
                print("you guessed a number which bigger than actual number")
            else:
                print("you guessed a number which lesser than actual number")


guessing_game_one()