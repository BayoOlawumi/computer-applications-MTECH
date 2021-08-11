# your friend will complete this function

def play_once(human_plays_first):
    """
        Must play one round of the gam.If the parameter is
        True, the human to play first, else the computer
        gets to play first. Whwn the round ends, the return
        value of the function is one of -1 (human wins),
        0(game drawn), 1(computer wins).

    """
    # This is all dummy scaffolding code right at the moment
    import random
    rng =random.Random()
    # Pick a random result -1 and 1
    result = rng.randrange(-1,2)
    print("Human plays first ={0}, winner={1} ". format(human_plays_first,result))
    return result


# This function plays the game
def play_game():
    total_games = 0
    computer_wins = 0
    human_wins = 0
    drawn_games = 0
    continue_game = True

    while continue_game:
        total_games += 1
        winner = play_once(True)
        # Conditional statement to identify who won each game
        if winner == -1:
            human_wins = human_wins + 1
            print("You win!")
        elif winner == 1:
            computer_wins =computer_wins+1
            print("I win!")
        elif winner == 0:
            drawn_games = drawn_games + 1
            print("Game Drawn!")
        # Get a response from player whether he wants to continue the game
        response = input("Do you want to play again? Yes(Y) or No(N)")
        response = response.upper()
        if response == 'Y' or response == "YES":
            continue_game = True
        else:
            print("Goodbye!")
            continue_game = False

    # Score Annoucement
    print("                GAME OVER              ")
    print("********AT THE END OF {0} ROUND(S):***********".format(total_games))
    print("Computer won {0} round(s)".format(computer_wins))
    print("Human won {0} round(s)".format(human_wins))
    print("{0} games were drawn".format(drawn_games))


play_game()