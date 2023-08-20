class Solution:
    def tictactoe(self, moves: [[int]]) -> str:
        n = 3 # size of the grid
        grid = [[' ' for _ in range(n)] for _ in range(n)]

        # Fill the grid
        for i, move in enumerate(moves):
            if i % 2 == 0:  # even A, odd B
                grid[move[0]][move[1]] = 'X'
            else:
                grid[move[0]][move[1]] = 'O'

        # Check rows
        for row in grid:
            if row[0] == row[1] == row[2] != ' ':
                return 'A' if row[0] == 'X' else 'B'
            
        # Check columns
        for i in range(n):
            if grid[0][i] == grid[1][i] == grid[2][i] != ' ':
                return 'A' if grid[0][i] == 'X' else 'B'
            
        # Check diagonals
        if grid[0][0] == grid[1][1] == grid[2][2] != ' ':  # left diagonal
            return 'A' if grid[0][0] == 'X' else 'B'
        if grid[0][2] == grid[1][1] == grid[2][0] != ' ':  # right diagonal
            return 'A' if grid[0][2] == 'X' else 'B'
        

        # No Winner
        return 'Draw' if len(moves) == 9 else 'Pending'

        

# Test code:
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
print(Solution().tictactoe(moves))

moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
print(Solution().tictactoe(moves))

moves = [[0,0],[1,1]]
print(Solution().tictactoe(moves))

moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
print(Solution().tictactoe(moves))
