# find kth node from the end of a singly linked list

# 문제2. 단방향 연결리스트가 주어진 경우, 뒤에서 k번째 원소를 찾는 알고리즘을 구하라.

# 예제
# 입력: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
# 출력: 8

# 힌트
# 1. 연결리스트의 길이를 알고 있다면, 뒤에서 k번째 원소는 전체 길이에서 k만큼 뺀 위치에 있는 원소가 된다.
def find_kth_node(node, k):
    if not node:
        return node

    curr = node
    length = 0
    while curr:
        length += 1
        curr = curr.next

    curr = node
    for i in range(length - k):
        curr = curr.next

    return curr

# 2. 연결리스트의 길이를 모른다면, 두 개의 포인터를 사용해 보자.
def find_node_two_pointers(node, k):
    if not node:
        return node

    p1 = node
    p2 = node
    for i in range(k):
        p1 = p1.next

    while p1:
        p1 = p1.next
        p2 = p2.next

    return p2

# test code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def append(self, data):
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = Node(data)
        
    def print(self):
        curr = self
        while curr:
            print(curr.data)
            curr = curr.next

node = Node(1)
node.append(2)
node.append(3)
node.append(4)
node.append(5)
node.append(6)
node.append(7)
node.append(8)
node.append(9)
node.append(10)

print(find_kth_node(node, 3).data)

print(find_node_two_pointers(node, 4).data)