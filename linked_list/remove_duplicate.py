# 2.1 비정렬 연결리스트에서 중복 문자를 제거하는 코드를 작성하라
# 임시 버퍼가 허용되지 않는 상황에서 이 문제를 어떻게 해결할 수 있겠는가?

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# def remove_duplicate(node:Node):
#     dic = {}          # 임시 버퍼
#     prev = None   
#     while node:
#         if node.data in dic.keys():
#             prev.next = node.next 
#         else:
#             dic[node.data] = True
#             prev = node

#         node = node.next

def remove_duplicate(node:Node):
    prev = None
    


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

