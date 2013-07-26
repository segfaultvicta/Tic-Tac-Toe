from Board import Board

print "Is it can be tic-tac-toe tiem nao plz?"

playerX = True

while 1:
    go_first = raw_input("Do you want to go first and play 'X'? [Y/N] ")
    if go_first == "Y":
        print "Okay. Playing as X."
        break
    elif go_first == "N":
        print "Okay. Playing as O."
        playerX = False
        break
    else:
        print "Sorry, I didn't understand that input."

game = Board()

#while we still want to play again...
while 1:
    #while the game hasn't yet been won...
    turn = 1
    while 1:
        
        print "Turn " + str(turn) + ":"
        print game.print_format()
        

    

