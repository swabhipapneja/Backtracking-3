### BACKTRACKING SOLUTION
# Time Complexity : O(N!), because we have a recurive call in every row, and the no of possible positions for the queen keep on decreasing and we increase the rows
# Space Complexity : O(n^2) + O(n) - recursive stack space - O(n) - higher order - O(n^2) (grid)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# we are iterating every row of the given board
# we try to place a Queen in a cell if it sis safe to place the queen there
# so for loop is running on cols and recursion is iterating on the rows
# if we exhaust columns, we know that the previous Queen's placement in previous row was incorrect, so we backtrack and undo that action
# we keep on doing this until we exhaust our rows
# usng a boolean matrix to keep track where we placed the queens, when we have a colution, we save it in a list of lists
# where T => Q abd F => .



class Solution(object):
    def __init__(self):
        self.grid = []
        self.result = []
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # n is no of queens

        # we dont have grid
        # creating a boolean grid 
        self.grid = [[False for _ in range(n)] for _ in range(n)]
        self.backtrack(0, n)
        return self.result
    
    def backtrack(self, row, n):
        # base case
        if row ==  n:
            answer = []
            for i in range(n):
                # a new string builder for every row
                sb = []
                for j in range(n):
                    if self.grid[i][j] == True:
                        sb.append("Q")
                    else:
                        sb.append(".")
                answer.append("".join(sb))

            self.result.append(answer)
            return

        # logic
        # logic is to place the queen one by one in each column of the given row
        # checking that if it is safe to place the queen in that column
        # for loop running for columns
        for i in range(0, n):
            # checking if it safe to place the queen
            if(self.issafe(row, i)):
                # changing the cell value to T if queen is placed - ACTION
                self.grid[row][i] = True
                # after placing the queen, we move to the next row - RECURSE
                self.backtrack(row+1, n)
                # and then we backtrack - BACKTRACK
                self.grid[row][i] = False

    def issafe(self, row, col):
        # check above - row-- and col same
        for i in range(row, -1, -1):
            if self.grid[i][col] == True:
                return False


        # check upper left diagonal
        i = row # decreases
        j = col # decreases
        while(i >=0 and j >= 0):
            if self.grid[i][j] == True:
                return False
            
            i -= 1
            j -= 1

        # check upper right diagonal
        i = row # decreases
        j = col # increases
        while(i >= 0 and j < len(self.grid)):
            if self.grid[i][j] == True:
                return False
            
            i -= 1
            j += 1

        return True



        
        