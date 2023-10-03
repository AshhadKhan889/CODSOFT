import random

def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, Scissors: ")
        
        if user_choice in ('Rock', 'Paper', 'Scissors'):
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, Scissors: ")

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determining_winner(user_choice, computer_choice):
    print(f"You choose: {user_choice}")
    print(f"Computer choose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie!")
        return None  

    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Scissors' and computer_choice == 'Paper') or
        (user_choice == 'Paper' and computer_choice == 'Rock')
    ):
        print(f"{user_choice} beats {computer_choice}")
        print("You Win!")
        return True  

    else:
        print(f"{computer_choice} beats {user_choice}")
        print("Computer Wins!")
        return False  

def main():
    user_score = 0
    computer_score = 0

    print("                    Welcome to the Rock, Paper, Scissors gaming Application\n")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determining_winner(user_choice, computer_choice)

        if result is not None:
            if result:
                user_score += 1
            else:
                computer_score += 1

        print(f"Your Score: {user_score}")
        print(f"Computer Score: {computer_score}")

        play_again = input("Do you want to play again? (Yes/No): ")
        if play_again == 'Yes':
            print("Good. You are really enjoying this game.")

        elif play_again == 'No':
            print("Thankyou for playing this game.")
            break

main()
