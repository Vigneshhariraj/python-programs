import random

def get_player_choice():
    options = ["Rock", "Paper", "Scissor"]
    print("Please choose an option:")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    
    choice = input("Enter the number of your choice: ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("Enter the number of your choice: ")
    
    return options[int(choice) - 1].lower()

def main():
    player1 = get_player_choice()
    player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
    print("Player 2 selected:", player2.title())

    if player1 == "rock" and player2 == "paper":
        print("Player 2 Won")
    elif player1 == "paper" and player2 == "scissor":
        print("Player 2 Won")
    elif player1 == "scissor" and player2 == "rock":
        print("Player 2 Won")
    elif player1 == player2:
        print("Tie")
    else:
        print("Player 1 Won")

if __name__ == "__main__":
    main()
