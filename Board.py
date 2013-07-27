class Board:
  
    CATSGAME_1 = 3888
    CATSGAME_2 = 2592
    
    # All possible configurations that could contain a 3-in-a-row
    TOP      = [0,1,2]
    LEFT     = [0,3,6]
    RIGHT    = [2,5,8]
    BOTTOM   = [6,7,8]
    MIDROW   = [3,4,5]
    MIDCOL   = [1,4,7]
    DIAG1    = [0,4,8]
    DIAG2    = [2,4,6]
    # 'marks' maintains a list of integers corresponding to the present board      
    # state. It is initialised to a completely blank board by default.
    # '1' corresponds to a blank spot on the board.
    # '2' corresponds to an 'O' mark on the board.
    # '3' corresponds to an 'X' mark on the board.
    # This facilitates determining the state of any given row, column, 
    # or diagonal.
    def  __init__(self, initial_state=None):
        #print("init board")
        if initial_state is None:
            #print("initial state none, making blank board")
            self.marks = [1,1,1,1,1,1,1,1,1]
        else:
            #print("given an initial state, using that as the board")
            self.marks = initial_state
        #print(self.marks)

    # Returns a string of the current board in a printable format.
    # If showPositions is true, it'll print out the number of each position,
    # rather than the mark at each position.
    def print_format(self, showPositions=False):
        string =  "-|---|---|---|-\n | " 
        string += self.translate(0, showPositions) + " | " + self.translate(1, showPositions) + " | " + self.translate(2, showPositions) + " |\n"
        string += "-|---|---|---|-\n | "
        string += self.translate(3, showPositions) + " | " + self.translate(4, showPositions) + " | " + self.translate(5, showPositions) + " |\n"
        string += "-|---|---|---|-\n | "
        string += self.translate(6, showPositions) + " | " + self.translate(7, showPositions) + " | " + self.translate(8, showPositions) + " |\n"
        string += "-|---|---|---|-\n"
        return string

    def translate(self,position, showPositions=False):
        # Positions are defined as follows:
        # -|---|---|---|-
        #  | 0 | 1 | 2 |
        # -|---|---|---|-
        #  | 3 | 4 | 5 |
        # -|---|---|---|-
        #  | 6 | 7 | 8 |
        # -|---|---|---|-
        # translate() will, given a board position, return a character representing that position's
        # status in a manner fit for human consumption.
        # If showPositions is true, will return the current position rather than the mark at that position.
        if showPositions:
            return str(position)
        if self.marks[position] == 1:
            return " "
        elif self.marks[position] == 2:
            return "O"
        elif self.marks[position] == 3:
            return "X"
        else:
            return "?"

    def game_over(self):
        integer_state = self.integer_state()
        if integer_state == 3888 or integer_state == 2592:
    
    # assumes that position is a legal move. The check for that -should- be in this function,
    # but I didn't want to spend forever on fiddly game loop UI things. I might refactor that later?
    def move(self, position, mark):
        if mark == 'X':
            self.marks[position] = 3
        else:
            self.marks[position] = 2

    # will return true if the position is a legal move, and false otherwise.
    # a legal move in Tic-Tac-Toe is any move that will not place a mark
    # in a position already containing a mark.
    def is_legal_move(self, position):
        return self.marks[position] == 1
    
    # returns a normalised integer state of the game board, determined by
    # multiplying the contents of self.marks together.
    # see also: http://en.wikipedia.org/wiki/G%C3%B6del_numbering ish.
    # states of note:
    # 3888 and 2592 are the only possible cat's games (5 X and 4 O, or 5 O and 4 X)
    # (see constants at top of class)
    def integer_state(self):
        return reduce(lambda x, y: x*y, self.marks)

#boardtest = Board()
#boardtest2 = Board([1,2,3,1,1,1,1,3,2])

#print(boardtest.print_format())
#print(boardtest2.print_format())
