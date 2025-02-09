### BACKTRACKING SOLUTION
# Time Complexity : exponential, looking at 4 directions of the elements in the given word recursively
# Space Complexity : dirs array only - constant, and recurisve stack when we find a character - O(len(word))
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# we start by traversing the given matrix to find the first character in the given word
# then we mark it as visisted (#), save it's old value, and check all it's neighbours
# we find nr and nc, and pas sthat to the rceurse function
# base condition - if we iterated all the indices of the given word, so it means we found the ocmplete word
# if we traversed the complete matrix - we return false
# if we are going on one path and then realize this was not the solution - we will return false and backtrack
# undo the action and mark the cell as not visited again

class Solution(object):
    def __init__(self):
        self.m, self.m = 0, 0
        self.dirs = []
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board is None:
            return False
        
        self.m = len(board)
        self.n = len(board[0])
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]] # U D L R

        # iterate over the board to find the first letter in the given word
        for i in range(self.m):
            for j in range(self.n):
                # found the first char in given word at grid[i][j]
                if board[i][j] == word[0]:
                    # checking all neighbours - using backtracking
                    if(self.backtrack(board, i, j, word, 0)):
                        return True

        return False

    def backtrack(self, board, row, col, word, index):
        # base case
        if index == len(word):
            # this means we have found the complete word
            return True
        if row < 0 or row >= self.m or col < 0 or col >= self.n or board[row][col] == '#':
            return False    

        # logic
        # checking all directions if we have required char at the given indices in the board
        if board[row][col] == word[index]:
            #storing original value, in case of backtracking
            temp = board[row][col]
            # mutating the element in the grid to mark it visited and make sure we dont reuse it - ACTION
            board[row][col] = '#'
            for dir in self.dirs:
                nr = row + dir[0]
                nc = col + dir[1]
                # we will backtrack here, recursively checking for all neighbours searching for element at next index
                
                if (self.backtrack(board, nr, nc, word, index + 1)):
                    return True
            
            # if we did not find the word in the above recurse call - backtrack the current one
            board[row][col] = temp
        
        return False # did not find the word in this recursive call






        