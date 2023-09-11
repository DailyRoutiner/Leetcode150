# 비정렬 연결리스트에서 중복 문자를 제거하는 코드를 작성하라
# 임시 버퍼가 허용되지 않는 상황에서 이 문제를 어떻게 해결할 수 있겠는가?

# Input: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
# Output: 1 -> 2 -> 3 -> 4 -> 5

# Input: 1 -> 1 -> 1 -> 2 -> 3
# Output: 1 -> 2 -> 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicate(node):
    if not node:
        return node

    curr = node
    while curr:
        runner = curr
        while runner.next:
            if runner.next.data == curr.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next
    return node
    

# test code
node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(3)
node.next.next.next.next = Node(4)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(5)

node = remove_duplicate(node)
while node is not None:
    print(node.data)
    node = node.next

