# 회전형 리스트? deque 데크를 이용하여 쉽게 구현 가능

from collections import deque

a = [1,2,3,4,5]
q = deque(a)  # deque 객체로 변환

q.rotate(2)
print(q)
result = list(q)
print(result)

# 또한 스택과 큐로 사용 가능
q.appendleft(6)
print(q)
q.popleft()


# 참고 : https://docs.python.org/ko/3/library/collections.html#collections.deque