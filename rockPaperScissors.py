import random

def play():
    user = input("What's the player's choice? 'r' for rock, 'p' for paper, 's' for scissors:  ")
    computer = random.choice(['r', 'p', 's'])

    while user == computer:
        user = input("It's a tie! Guess again:  ")
        computer = random.choice(['r', 'p', 's'])

        if user != computer:
            break

    # r>s, s>p, p>r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    #return true if the player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())