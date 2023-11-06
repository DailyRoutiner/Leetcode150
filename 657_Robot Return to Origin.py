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

# different solution
# from enum import Enum 

class Sol2():
    x = y = 0
    def up(self):
        self.y += 1
        return self.y 

    def down(self):
        self.y -= 1
        return self.y 

    def left(self):
        self.x -= 1
        return self.x
    def right(self):
        self.x += 1
        return self.x

    switcher = { # 상수가 아니고 function을 넣어서 복잡해짐..
        'U': up,
        'D': down,
        'L': left,
        'R': right
    }

    def switch(self, cha):
        move_function = self.switcher.get(cha)
        if move_function:
            move_function(self)
            print(f'Current x: {self.x}, Current y: {self.y}')
        else:
            print("Invalid move")


sol2 = Sol2()
moves = "RRDD"
for i in moves:
    sol2.switch(i)

print(sol2.x)
print(sol2.y)
