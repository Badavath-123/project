import random

def play():
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"
    else:
        return "You lost!"

def is_win(player, opponent):
    # return true if player wins
    # rock > scissors, scissors > paper, paper > rock
    if (player == "rock" and opponent == "scissors") or \
       (player == "scissors" and opponent == "paper") or \
       (player == "paper" and opponent == "rock"):
        return True
    return False

# Run the game
print(play())
