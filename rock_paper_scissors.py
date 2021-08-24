def rock_paper_scissors():
    import random
    new_game = True
    user_choice = ''
    choices = ['r','p','s']

    while new_game:
        computer_choice = random.choice(choices)
        user_choice = input("press 'r' for rock, 'p' for paper, 's' for scissors: ")
        if computer_choice == user_choice:
            print("Match draw")
        elif user_choice == "r":
            if computer_choice == "s":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_choice == "p":
            if computer_choice == "r":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_choice == "s":
            if computer_choice == "p":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        new_game = input("Do you want to play another game? Press 'y' or 'n': ")
        if new_game == 'y':
            new_game = True
        else:
            new_game = False

rock_paper_scissors()