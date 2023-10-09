# repeated_string_count
# 같은 문자가 연속으로 반복될 경우, 그 횟수를 사용해 문자영을 압축하는 메서드를 구현하라. 가령 압축해야 할 문자열이 aabccccccaaa라면 a2b1c5a3 과 같이 압축되어야 한다. 압축 결과로 만들어지는 문자열이 원래 문자열보다 짧아지지 않는 경우, 이 메서드는 원래 문자열을 그대로 반환해야 한다.

# 접근법: 문자열을 순회하면서 새로운 문자열에 문자들을 복사해 넣고 반복되는 카운트를 넣는다

a1 = "aabccccccaaa"

def compress_string(string):
    compressed = ""
    count = 0
    
    for i in range(len(string)):
        count += 1
        #print(i , len(string))
        if i+1 >= len(string) or string[i] != string[i+1]:
            compressed += string[i] + str(count)    # immutable string 으로 인해 새로운 문자열이 계속 생성됨
            #print(compressed)
            count=0

    # 압축 결과 문자열이 원래 문자열보다 길 경우 원래 문자열 반환
    if len(compressed) >= len(string):
        return string
    
    return compressed



# 내 버전
def compress_string1(s1):
    size = countCompression(s1)
    if size >= len(s1):
        return s1
    
    arr = [0] * size
    last = s1[0]
    count = 1
    index = 0
    
    for i in range(1, len(s1)):
        if s1[i] == last:
            count += 1
        else:
            index = setChar(arr, last, index, count)
            last = s1[i]
            count = 1
        
    index = setChar(arr, last, index, count)
    return ''.join(arr)

def setChar(arr, c, index, count):
    arr[index] = c
    index += 1
    
    for i in range(len(str(count))):
        arr[index] = str(count)[i]
        index += 1
    
    return index

def countCompression(s1):
    if not s1: return 0
    last = s1[0]
    size = 0
    count = 0

    for i in range(len(s1)):
        count += 1
        if last != s1[i]:
            last = s1[i]
            size += 1 + len(str(count))
            count = 0
    
    size += 1 + len(str(count))
    return size

# test code
print(compress_string(a1)) # a2b1c5a3
print(compress_string("abc")) # abc
print(compress_string("aabbcc")) # aabbcc
print(compress_string("aabccccccaaa")) # a2b1c5a3

print(compress_string1(a1)) # a2b1c5a3
print(compress_string1("abc")) # abc
print(compress_string1("aabbcc")) # aabbcc
print(compress_string1("aabccccccaaa")) # a2b1c5a3


