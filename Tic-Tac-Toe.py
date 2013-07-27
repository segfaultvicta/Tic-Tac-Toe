from Board import Board

def main_loop():
    print("Is it can be tic-tac-toe tiem nao plz?")

    playerX = True

    while 1:
        go_first = input("Do you want to go first and play 'X'? [Y/N] ")
        if go_first == "Y":
            print("Okay. Playing as X.")
            break
        elif go_first == "N":
            print("Okay. Playing as O.")
            playerX = False
            break
        else:
            print("Sorry, I didn't understand that input.")

    game = Board()

    #while we still want to play again...
    while 1:
        #while the game hasn't yet been won...
        turn = 1
        while 1:
            if playerX:
                print("Turn " + str(turn) + ":")
                print(game.print_format())
                if not game.game_over():
                    #ask player for their move
                    game.move(get_human_move(game),'X')
                    if not game.game_over():
                        #ask ai player for their move
                        game.move(get_ai_move(game, playerX),'O')
                    else:
                        break #game has been won
                else:
                    break #game has been won
            else:
                #playing as 'O', so the AI goes first...
                if not game.game_over():
                    game.move(get_ai_move(game, playerX),'X')
                    if not game.game_over():
                        print("Turn " + str(turn) + ":")
                        print(game.print_format())
                        if not game.game_over():
                            game.move(get_human_move(game),'O')
                        else:
                            break
                    else:
                        break
        #game has been won at this point
        print("Yaaay, game has won or drawn")
        break
    print("Exiting program.")

#gets player input for a move. will loop until it recieves a legal position to move.
def get_human_move(game):
    """Gets player input for a move. 
    Will loop until it recieves a legal position to move.
    """
    while 1:
        response = input("Please enter a position, 0 through 8, you wish to mark. Alternately, enter '?' to print out a reminder of all positions.")
        if response == "?":
            print("The positions are as follows:")
            print(game.print_format(True))
        else:
            try:
                int_response = int(response)
                if 0 <= int_response <= 8:
                    #then it would seem we have a valid integer position; check to make sure it's a legal move.
                    if game.is_legal_move(int_response):
                        #we're good to go, return that as the move
                        return int_response
                    else:
                        print("That position isn't a legal move. As much as you'd like to mark there, someone else already has!")
                else:
                    print("That position isn't between 0 and 8. Perhaps you want to play Nine Men's Morris instead?")
            except ValueError:
                print("I couldn't understand that input.")
  
def get_ai_move(game, playerX):
    """Returns the AI's best position to mark given the state of the board.
    
    General heuristic steps:
    1. If there's a 2-in-a-row of the AI's, it should complete it.
    2. If there's a 2-in-a-row of the human player's, it should block it. 
    (Order doesn't matter, since if there's more than one human 2-in-a-row and
    both can't be blocked with a single move, the AI's screwed anyway.
    However, that shouldn't ever even be the case.)
    3. If the centre square is clear, mark it.
    4. Recursively search the game tree using alpha-beta pruning to determine
    the best move to take.
    """
    if playerX:
        #AI is playing player O
        row_near_victory = ROW_NEARLY_WON_O
        row_near_loss = ROW_NEARLY_WON_X
    else:
        #AI is playing player X
        row_near_victory = ROW_NEARLY_WON_X
        row_near_loss = ROW_NEARLY_WON_O
    # If there's a 2-in-a-row of the AI's, it should complete it.
    for row in ALLROWS:
        if board.integer_state(row) == row_near_victory:
            #complete the row
            for position in row:
                if board.is_legal_move(position):
                    return position
    # If there's a 2-in-a-row of the human player's, it should block it.               
    for row in ALLROWS:
        if board.integer_state(row) == row_near_loss:
            #complete the row to prevent the opponent from winning
            for position in row:
                if board.is_legal_move(position):
                    return position
    # If the centre square is clear, mark it.
    if board.is_legal_move(4):
        return 4
    # Here's the fun part.
    while 1:
        #AAHAHAHAHA no this isn't really the AI.
        #Maybe this is the AI when it was 4 years old, or something.
        random_position = random.randint(0,8)
        if board.is_legal_move(random_position):
            return random_position

main_loop() #start the game now that all functions have been defined :)
