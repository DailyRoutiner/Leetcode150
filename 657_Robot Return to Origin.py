class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

# test code:
moves = "UD"
print(Solution().judgeCircle(moves))

moves = "LL"
result = False
assert Solution().judgeCircle(moves) == result
print("Test1: pass")


moves = "RRDD"
print(Solution().judgeCircle(moves))

moves = "LDRRLRUULR"
print(Solution().judgeCircle(moves))
