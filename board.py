class Board:
  
    # 'marks' maintains a list of integers corresponding to the present board      
    # state. It is initialised to a completely blank board by default.
    # '1' corresponds to a blank spot on the board.
    # '2' corresponds to an 'O' mark on the board.
    # '3' corresponds to an 'X' mark on the board.
    # This facilitates determining the state of any given row, column, 
    # or diagonal.
    def  __init__(self, initial_state=None):
        print "init board"
        if initial_state is None:
            print "initial state none, making blank board"
            self.marks = [1,1,1,1,1,1,1,1,1]
        else:
            print "given an initial state, using that as the board"
            self.marks = initial_state
        print self.marks

    #Returns a string of the current board in a printable format.
    def print_format(self):
        string =  "-|---|---|---|-\n | " 
        string += self.translate(0) + " | " + self.translate(1) + " | " + self.translate(2) + " |\n"
        string += "-|---|---|---|-\n | "
        string += self.translate(3) + " | " + self.translate(4) + " | " + self.translate(5) + " |\n"
        string += "-|---|---|---|-\n | "
        string += self.translate(6) + " | " + self.translate(7) + " | " + self.translate(8) + " |\n"
        string += "-|---|---|---|-\n"
        return string

    def translate(self,position):
        # Positions are defined as follows:
        # -|---|---|---|-
        #  | 0 | 1 | 2 |
        # -|---|---|---|-
        #  | 3 | 4 | 5 |
        # -|---|---|---|-
        #  | 6 | 7 | 8 |
        # -|---|---|---|-
        if self.marks[position] == 1:
            return " "
        elif self.marks[position] == 2:
            return "O"
        elif self.marks[position] == 3:
            return "X"
        else:
            return "?"


boardtest = Board()
boardtest2 = Board([1,2,3,1,1,1,1,3,2])

print boardtest.print_format()
print boardtest2.print_format()