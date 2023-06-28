# Queens end problem, need to have a board with a queen on each row that cant 
# attack another queen, eg:
#
# 0 0 1 0
# 1 0 0 0
# 0 0 0 1
# 0 1 0 0

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for x in range(size)] for x in range(size)] 
        # first number is row (up and down) second is col (left and right)
        self.solve(0)
        self.print_board()


    def print_board(self):
        for i in self.grid:
            print("".join(str(i)))


#  0 1 2 3
#0 0 0 1 0 
#1 1 0 0 0
#2 0 0 0 1
#3 0 1 0 0

# row is up and down and col is left and right

# to left -1 to col, to look up you -1 to row, and to look down you +1 to row


    def is_valid(self, row, col):
        
        for x in range(col):
            if self.grid[row][x] == 1:
                return False
            
        # minus one from each index with -1 (none inclusive) being the stop point
        # this means you are going up and to the left, you only check left as you only
        # need to check whats been placed behind you 
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)): # look to the left and up
            if self.grid[i][j] == 1:
                return False
            

        # minus one from col so you're still looking to the left but you increase
        # row meaning you go downwards on the grid.                                
        for a, b in zip(range(row, self.size) , range(col, -1, -1)): # look to the left and down
            if self.grid[a][b] == 1:
                return False
            
        return True

    def solve(self, col):
        if col >= self.size: # if we have reached the end of grid
            return True
        
        for x in range(self.size): # for each row
            if self.is_valid(x, col): # if the queen/1 can be placed there
                self.grid[x][col] = 1 # change the value to 1

                if self.solve(col+1): # calls itself and checks the next line, if its True then funection carries on
                    return True
                
                self.grid[x][col] = 0 # if false however it resets the grid the value it just changed

        return False 


Board(5)