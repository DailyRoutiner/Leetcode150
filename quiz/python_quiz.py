# Quiz1
def changeString(s):
    
    arr = s.split(':')    
    res = "#".join(arr)

    return res

# test code:
s = 'a:b:c:d'
print(changeString(s))


# Quiz 2
a = {'A': 90, 'B': 80}
print(a.get('C', 70))


# Quiz 3
a = [1, 2, 3]
a = a + [4, 5] # new list
print(a)
a.extend([6, 7]) # extend list
print(a)

# Quiz 4
a = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
res = 0
for i in a:
    if i >= 50:
        res += i
print(res)

res1 = sum([ v for v in a if v >= 50 ])
print(res1)

# Quiz 5
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

for i in range(10):
    print(fibonacci(i), end=' ')

# Quiz 6
t = input().split(',')
print(sum(map(int, t)))

