
from collections import deque

a = [1,2,3,4,5]
q = deque(a)  # deque 객체로 변환

q.rotate(2)
print(q)
result = list(q)
print(result)
