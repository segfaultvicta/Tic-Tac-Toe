import functools

CATSGAME1 = 3888
CATSGAME2 = 2592
    
ROW_WON_X = 27
ROW_WON_O = 8
ROW_NEARLY_WON_X = 9
ROW_NEARLY_WON_O = 4
    
# All possible configurations that could contain a 3-in-a-row
TOP      = [0,1,2]
LEFT     = [0,3,6]
RIGHT    = [2,5,8]
BOTTOM   = [6,7,8]
MIDROW   = [3,4,5]
MIDCOL   = [1,4,7]
DIAG1    = [0,4,8]
DIAG2    = [2,4,6]
ALLROWS  = [TOP, LEFT, RIGHT, BOTTOM, MIDROW, MIDCOL, DIAG1, DIAG2]

class Board:
    """
    'marks' maintains a list of integers corresponding to the present board      
    state. It is initialised to a completely blank board by default.
    '1' corresponds to a blank spot on the board.
    '2' corresponds to an 'O' mark on the board.
    '3' corresponds to an 'X' mark on the board.
    This facilitates determining the state of any given row, column, 
    or diagonal.
    """
    def  __init__(self):
        self.marks = [1,1,1,1,1,1,1,1,1]

    def print_format(self, showPositions=False):
        """Returns a string of the current board in a printable format.
        If showPositions is true, it'll print out the number of each position,
        rather than the mark at each position.
        """
        string =  "-|---|---|---|-\n | " 
        string += self.translate(0, showPositions) + " | " + self.translate(1, showPositions) + " | " + self.translate(2, showPositions) + " |\n"
        string += "-|---|---|---|-\n | "
        string += self.translate(3, showPositions) + " | " + self.translate(4, showPositions) + " | " + self.translate(5, showPositions) + " |\n"
        string += "-|---|---|---|-\n | "
        string += self.translate(6, showPositions) + " | " + self.translate(7, showPositions) + " | " + self.translate(8, showPositions) + " |\n"
        string += "-|---|---|---|-\n"
        return string

    def translate(self,position, showPositions=False):
        """Given a board position, return a character representing that
        position's status in a manner fit for human consumption.
        If showPositions is true, will return the current position rather than the mark at that position.
        Positions are defined as follows:
        -|---|---|---|-
         | 0 | 1 | 2 |
        -|---|---|---|-
         | 3 | 4 | 5 |
        -|---|---|---|-
         | 6 | 7 | 8 |
        -|---|---|---|-
        """
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
        if integer_state == CATSGAME1 or integer_state == CATSGAME2:
            return True
        else:
            #print("Iterating over all rows...")
            for row in ALLROWS:
                #for every possible row, calculate its integer state and 
                #compare that to the integer state of a row containing all
                #'X' or all 'O', to determine if a player has won the game.
                #print("Row " + str(row));
                if self.integer_state(row) == ROW_WON_X or self.integer_state(row) == ROW_WON_O:
                    return True
        return False
    
    def move(self, position, mark):
        """Marks a given position with a given mark. 
        
        Assumes that 'mark' will be "X" or "O", and that the position is a legal move.
        """
        if mark == 'X':
            self.marks[position] = 3
        else:
            self.marks[position] = 2

    def is_legal_move(self, position):
        """Returns True if the position is a legal move, and false otherwise.
        
        A legal move in Tic-Tac-Toe is any move that will not place a mark
        in a position already containing a mark, i.e., an index in self.marks
        whose value is still 1.
        """
        return self.marks[position] == 1
    
    def integer_state(self, mask=[0,1,2,3,4,5,6,7,8]):
        """Returns a normalised integer state of the game board.
        
        Determined by multiplying the contents of self.marks together.
        see also: http://en.wikipedia.org/wiki/G%C3%B6del_numbering ish.
        If mask is provided, it'll only give you the integer state of that 
        particular set of positions - this is useful for determining if a 
        row is in a win or almost-win state.
        
        States of note are provided in constants at the top of this file. 
        """
        masked_marks = []
        for position in range(0,9):
            if position in mask:
                masked_marks.append(self.marks[position])
        return functools.reduce(lambda x, y: x*y, masked_marks)

#boardtest = Board()
#boardtest2 = Board([1,2,3,1,1,1,1,3,2])

#print(boardtest.print_format())
#print(boardtest2.print_format())
