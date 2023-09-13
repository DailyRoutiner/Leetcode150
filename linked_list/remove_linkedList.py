# 문제3. 단방향 연결 리스트의 중간에 있는 노드 하나를 삭제하는 알고리즘을 구현하라. 삭제할 노드에 대한 접근만 가능하다는 것에 유의하라.

def delete_middle_node(node):
    if not node or not node.next:
        return False

    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next
    return True

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

delete_middle_node(node.next.next.next)
node.print()

