def play_game(player1, player2, beats):
    """Returns the result of the game with player1 vs player2."""
    if (player1 == player2):
        print ("Tie")
    elif (player1 == beats[player2]):
        print ("Player 1 wins.")
    elif (player2 == beats[player1]):
        print ("Player 2 wins.")

def main():
    beats = {
        'scissors': 'rock',
        'rock': 'paper',
        'paper': 'scissors',
    }

    print ("The choices are " + str(beats.keys()))

    player1 = input("What is player 1's move? ")
    while player1 not in beats.keys():
        player1 = input("I didn't get that. Please choose from " + str(beats.keys()))

    player2 = input("What is player 2's move? ")
    while player2 not in beats.keys():
        player2 = input("I didn't get that. Please choose from " + str(beats.keys()))

    play_game(player1,player2,beats)

main()
