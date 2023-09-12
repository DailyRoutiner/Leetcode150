# 비정렬 연결리스트에서 중복 문자를 제거하는 코드를 작성하라
# 임시 버퍼가 허용되지 않는 상황에서 이 문제를 어떻게 해결할 수 있겠는가?

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicate(node):
    if not node:
        return node

    curr = node # current node to check duplicates from the next node to the end of the list
    while curr: # check duplicates for each node in the list until the end of the list is reached
        runner = curr # runner node to check duplicates from the next node to the end of the list for the current node in the list
        while runner.next: # check duplicates for each node in the list until the end of the list is reached for the current node in the list
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
while node:
    print(node.data)
    node = node.next

