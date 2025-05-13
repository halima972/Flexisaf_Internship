import random

def play_rps():
    """Simulates a game of Rock, Paper, Scissors between the user and the computer."""

    choices = ["rock", "paper", "scissors"]

    # Get the user's choice
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in choices:
            break
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

    # Generate the computer's choice
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    play_rps()