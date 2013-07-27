from Board import *
import copy

def main_loop():

    show_positions = [False] # using lists as lists are mutable
    print("Is it can be tic-tac-toe tiem nao plz?")

    #while we still want to play again...
    while 1:
        while 1:
            x_is_human = True
            go_first = input("Do you want to go first and play 'X'? [Y/N] ")
            if go_first == "Y":
                print("Okay. Playing as X.")
                break
            elif go_first == "N":
                print("Okay. Playing as O.")
                x_is_human = False
                break
            else:
                print("Sorry, I didn't understand that input.")

        game = Board()
        #while the game hasn't yet been won...
        turn = 1
        while 1:
            if x_is_human:
                print("Turn " + str(turn) + ":")
                if not game.game_over():
                    #ask player for their move
                    game.move(get_human_move(game, show_positions),'X')
                    if not game.game_over():
                        #ask ai player for their move
                        game.move(get_ai_move(game, x_is_human),'O')
                    else:
                        break #game has been won
                else:
                    break #game has been won
            else:
                #playing as 'O', so the AI goes first...
                if not game.game_over():
                    game.move(get_ai_move(game, x_is_human),'X')
                    if not game.game_over():
                        print("Turn " + str(turn) + ":")
                        if not game.game_over():
                            game.move(get_human_move(game, show_positions),'O')
                        else:
                            break
                    else:
                        break
            turn += 1
        #game has been won at this point
        gameresult = evaluate(game)
        if gameresult == -1:
            print("Game result: win by O!")
        elif gameresult == 0:
            print("Game result: cat's game! >^.^< (Or tie, if you're boring.)")
        else:
            print("Game result: win by X!")
        print(game)
        while 1:
            play_again = input("Play again? [Y/N]")
            if play_again == "Y":
                break
            elif play_again == "N":
                return
            else:
                print("I didn't understand that input.")

#gets player input for a move. will loop until it recieves a legal position to move.
def get_human_move(game, show_positions):
    """Prints game state and then gets player input for a move. 
    Will loop until it recieves a legal position to move.
    If show_positions is true, will show positions rather than blank spaces.
    """
    while 1:
        print(game.format(show_positions[0]))
        if show_positions[0]:
            response = input("Please enter a position, 0 through 8, you wish to mark. Alternately, enter '?' to switch into a mode that displays blank spaces instead of position numbers.")
        else:
            response = input("Please enter a position, 0 through 8, you wish to mark. Alternately, enter '?' to switch into a mode that displays position numbers instead of blank spaces.")
        if response == "?":
            print("Switching position display modes!")
            show_positions[0] = not show_positions[0]
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
  
def evaluate(game):
    """ Returns 1 for an X victory, 0 for a tie, and -1 for an O victory.
    A cat's game (tie) will have all rows with 2 Xs and 1 O, or 1 X and 2 Os.
    The row product of all rows in a tied game will be either 3*3*2 = 18
    or 2*2*3 = 12.
    
    I feel like there's something horribly clever I could have done here
    involving number theory - probably involving assigning each square of the
    board to a prime number? - but I didn't want to make things too complex
    and by the time I thought of it it'd have required way too much backtracking.
    
    """
    valid_row_exists = False
    #check each row to see if it consists of two Xs and an O or vice versa.
    #if there's a row that isn't like that, then it's not a tie!
    for row in ALLROWS:
        if game.integer_state(row) != ROW_XOX and game.integer_state(row) != ROW_OXO:
            valid_row_exists = True
    if not valid_row_exists:
        #cat's game. meow meow meow
        return 0
    # evaluate will only be called in the event of a done game. Therefore, if
    # the game is done, but it's not tied, one of the players has to have won:
    # this will always be the player who has most recently moved, and thus
    # will have more marks on the game board.
    elif game.marks.count(3) > game.marks.count(2):
        return 1
    else:
        return -1

def to_mark(player):
    """Returns a mark corresponding to the current player.
    
    If the current player is the maximising player, it will return 'X'.
    Otherwise - the current player is the minimising player, and it returns 'O'.
    """
    if player:
        return "X"
    else:
        return "O"
  
def generate_children(game, player):
    """Returns a list of games that could result from the given game and player turn.
    player = true means that the current ply is one of X's turns,
    player = false means that the current ply is one of O's turns.
    """
    children = []
    for i in range(0,9):
        if game.is_legal_move(i):
            # check to see if moving there would be a legal move;
            # if it is, make a deep copy of the game board, perform that
            # move on the board, and append a tuple containing it and
            # the position chosen to the list of games.
            gamecopy = copy.deepcopy(game)
            gamecopy.move(i,to_mark(player))
            children.append( (gamecopy, i) )
    return children

def alpha_beta(maximising_player, game, alpha, beta):
    """Returns the move that minimises the maximal loss to the board evaluation
    function, defined as 'the board is in a position such that X wins the game'.
    
    With help from http://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    and also http://en.wikipedia.org/wiki/Minimax#Minimax_algorithm_with_alternate_moves
    Aren't zero-sum games fun? :D
    
    maximising_player will be true if, on the first pass, the AI is playing 'X',
    and then on further passes, if the AI is calculating the best position for 'O'.
    
    Since X is the maximising player, whenever maximising_player is true,
    alpha_beta is calculating a turn for X, and whenever it's false, alpha_beta
    is calculating a turn for O.
    
    game is actually a tuple consisting of the game state being considered,
    and the position that was moved to in order to reach that state.
    """
    #check to see if the board is currently in a game over state (i.e. this is a terminal node)
    if game[0].game_over():
        return (evaluate(game[0]), game[1]) #return tuple of score and last position moved
    #generate the set of all possible legal moves from this point.
    children = generate_children(game[0], maximising_player)
    if maximising_player:
        #player X is trying to minimise its maximal loss on the evaluation function
        #recursively call alpha_beta on all children of the current node
        for child in children:
            #recursively run alpha_beta to determine next best move after this child
            best = alpha_beta(not maximising_player, child, alpha, beta)
            if best[0] > alpha[0]:
                alpha = best #found a better best move to make
            if alpha[0] >= beta[0]:
                return alpha #cut off this branch
        return alpha #move that minimises maximal loss of evaluation function
    else:
        # player O is trying to maximise its minimal loss on the evaluation function
        for child in children:
            best = alpha_beta(not maximising_player, child, alpha, beta)
            if best[0] < beta[0]:
                beta = best #opponent has a better worst move
            if alpha[0] >= beta[0]:
                return beta #cut off this branch
        return beta #minimiser's best move at this juncture
  
def get_ai_move(game, x_is_human):
    """Returns the AI's best position to mark given the state of the board.
    
    General heuristic steps:
    1. If there's a 2-in-a-row of the AI's, it should complete it.
    2. If there's a 2-in-a-row of the human player's, it should block it. 
    (Order doesn't matter, since if there's more than one human 2-in-a-row and
    both can't be blocked with a single move, the AI's screwed anyway.
    However, that shouldn't ever even be the case.)
    3. If the centre square is clear, mark it.
    4. Recursively search the game tree using minimax algorithm with
    alpha-beta pruning to determine the best move to take.
    """
    if x_is_human:
        #AI is playing player O
        row_near_victory = ROW_NEARLY_WON_O
        row_near_loss = ROW_NEARLY_WON_X
    else:
        #AI is playing player X
        row_near_victory = ROW_NEARLY_WON_X
        row_near_loss = ROW_NEARLY_WON_O
    # If there's a 2-in-a-row of the AI's, it should complete it.
    for row in ALLROWS:
        if game.integer_state(row) == row_near_victory:
            #complete the row
            for position in row:
                if game.is_legal_move(position):
                    return position
    # If there's a 2-in-a-row of the human player's, it should block it.               
    for row in ALLROWS:
        if game.integer_state(row) == row_near_loss:
            #complete the row to prevent the opponent from winning
            for position in row:
                if game.is_legal_move(position):
                    return position
    # If the centre square is clear, mark it.
    if game.is_legal_move(4):
        return 4
    """Here's the fun part.
    pass the inverse of x_is_human because alpha_beta takes
    "is this the maximising player", i.e. X, as its input, and the first
    call to alpha_beta is for the AI's turn. 
    We start alpha_beta with an alpha value of -∞ and beta value of ∞,
    meaning that the best the AI can do is lose, and the worst the opponent
    can do is letting the AI win.
    Game, alpha, and beta are given as tuples with the dummy value of -1 for
    position played to get to this point - these tuples find use in the
    alpha_beta function recursion to remember the position choice that led to 
    a particular game tree path.
    """    
    result = alpha_beta(not x_is_human, (game, -1), (float("-inf"), -1), (float("inf"), -1))
    return result[1]
    

main_loop() #start the game now that all functions have been defined :)
print("A strange game. The only winning move is not to play.")
print("...although playing against a tired programmer will do in a pinch.")