
# 3.1 하나의 배열을 사용해 세개의 스택을 구현하는 방법을 설명하라
# solution 1 고정 크기 스택 할당
stack_size = 10
buffer_array = [None] * stack_size * 3
stack_pointer = [-1, -1, -1]

def abs_top_of_stack(stack_num):
    global stack_size
    global stack_pointer
    return abs(stack_num * stack_size + stack_pointer[stack_num])

def push(stack_num, value):
    # 여유 공간이 있는지 검사
    if stack_pointer[stack_num] + 1 >= stack_size:
        print("Out of space")
        return
    # 스택 포인터를 증가시키고 가장 꼭대기에 값을 추가한다
    stack_pointer[stack_num] += 1
    buffer_array[abs_top_of_stack(stack_num)] = value

def pop(stack_num):

    if stack_pointer[stack_num] == -1:
        print("Trying to pop an empty stack")
        return
    value = buffer_array[abs_top_of_stack(stack_num)]   # 꼭대기 값을 가져온다
    buffer_array[abs_top_of_stack(stack_num)] = None    # Clear index
    stack_pointer[stack_num] -= 1                       # 스택 포인터를 감소시킨다
    return value

def peek(stack_num):
    index = abs_top_of_stack(stack_num)
    return buffer_array[index]

def is_empty(stack_num):
    return stack_pointer[stack_num] == -1

# test code
push(0, 1)
push(0, 2)
push(0, 3)
push(0, 4)
push(0, 5)
push(1, 6)
push(1, 7)
push(1, 8)
push(1, 9)
push(1, 10)
push(2, 11)
push(2, 12)
push(2, 13)
push(2, 14)
push(2, 15)
push(2, 16)
print(buffer_array)
print(stack_pointer)
print(pop(0))
print(pop(0))
print(pop(0))
print(pop(0))
print(pop(0))
print(pop(1))
print(pop(1))
print(pop(1))
print(pop(1))
print(pop(1))
print(pop(1))
print(pop(2))
print(pop(2))
print(pop(2))
print(pop(2))
print(pop(2))
print(buffer_array)
print(stack_pointer)
print(peek(0))
print(peek(1))
print(peek(2))
print(is_empty(0))
print(is_empty(1))
print(is_empty(2))

# solution 2 가변 크기 스택 할당
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def append(self, value):
        if self.is_full():
            return False
        self.array[self.size] = value
        self.size += 1
        return True

    def pop(self):
        if self.is_empty():
            return None
        self.size -= 1
        return self.array[self.size]

    def peek(self):
        if self.is_empty():
            return None
        return self.array[self.size - 1]