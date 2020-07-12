This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.


[[1,0,1],
 [2,2,2],
 [1,3,1],
 [1,2,1]]

-> 2 in a line >= No.3 crush

[[1,0,1],
 [0,0,0],
 [1,3,1],
 [1,2,1]]

-> drop the candy on the top

[[0,0,0],
 [1,0,1],
 [1,3,1],
 [1,2,1]]

-> crush No.3 1s in col 0 and col 2

[[0,0,0],
 [0,0,0],
 [0,3,0],
 [0,2,0]] (return)

1. board size? m * n, 
m, n [3,50]

2. crush if same item >= 3
[0,0,0,4],
[0,0,0,3],
[2,4,2,2]

APP1: brute force. 
each round
1 crush: traverse the board, then do DFS on each pos vertically or horizontally, if find same value >= 3, then crush them and set 0 to crushed pos.

2 reshape: from bottom up, if pos == 0, then swap with nearest top non-zero
    
3 check stable: check if any same value >= 3
    -1-1-1-1
    1111
    1111
class Solution:
    def candy_crush(self, board):
        if not board or not board[0]:
            return board
        while not self.crush(board):
            self.reshape(board)
        return board
        
    def crush(self, board): #Time: O(m * n)
        m, n, is_stable = len(board), len(board[0]), True
        for i in range(m):
            for j in range(n):
                ch = board[i][j]
                if ch == 0:
                    continue
                # horizontally crush
                count, k = 0, j
                while k < n and ch == board[i][k]:
                    count += 1
                    k += 1
                if count >= 3:
                    is_stable = False
                    for idx in range(count):
                        board[i][j + idx] = 0
                
                # vertically crush
                count, k = 0, i
                while k < m and ch == board[k][j]:
                    count += 1
                    k += 1
                if count >= 3:
                    is_stable = False
                    for idx in range(count):
                        board[i + idx][j] = 0    
        return is_stable
    
    def reshape(self, board): #Time: O(m * n)
        m, n = len(board), len(board[0])
        for j in range(n):
            k_b = m - 1
            while k_b >= 0 and board[k_b][j] != 0:
                k_b -= 1
            if k_b <= 0:
                continue
            k_t = k_b
            while k_t >= 0:
                while k_t >= 0 and board[k_t][j] == 0:
                    k_t -= 1
                if k_t >= 0:
                    board[k_t][j], board[k_b][j] = 0, board[k_t][j]
                k_t -= 1
                k_b -= 1

                
https://leetcode.com/problems/candy-crush/
