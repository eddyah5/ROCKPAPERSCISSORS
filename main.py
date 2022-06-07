import random
# Print multiline instruction
# performstring concatenation of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->Paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->Scissor wins \n")
CHOICES = ['r', 'p', 's']

opt = {    # changing the keys of the dictionary to lower case to match the `CHOICES`
    'r': "Rock",
    's': "Scissors",
    'p': "Paper"
}
def get_player_choice():
    """Get user input and validate it is one of the choices above"""
    player_choice = None
    while player_choice is None:
        player_choice = input('Please pick your Choice using only the first alphabets: \n(R)ock \n(P)aper \n(S)cissors \n\nPick: ')
        if player_choice.lower() not in CHOICES:
            print('Invalid choice(Error), please try again')
            player_choice = None
    return player_choice.lower()
def get_computer_choice():
    """Have the computer pick one of the valid choices at random"""
    # using random.choice method as stated in the task description
    computer_choice = random.choice(CHOICES)   
    return computer_choice
def is_draw(player_choice, computer_choice):
    """Check if game was a draw"""
    if player_choice == computer_choice:
        return True
def print_winner(player_choice, computer_choice):
    """Check to see who won"""
    if player_choice == 'r' and computer_choice == 's':
        print('Player wins!')
    elif player_choice == 's' and computer_choice == 'p':
        print('Player wins!')
    elif player_choice == 'p' and computer_choice == 'r':
        print('Player wins!')
    else:
        print('Computer wins!')
        # reformat the winning message
        print('%s beats %s' % (opt[computer_choice], opt[player_choice]))
def play_game():
    """play the game"""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    if is_draw(player_choice, computer_choice):
        print("It's a tie, both players picked %s: " % CHOICES[player_choice])
    else:
        print("CPU: %s" % opt[computer_choice])
        print("Player: %s" % opt[player_choice])
        print_winner(player_choice, computer_choice)
if __name__ == "__main__":
    play_game()