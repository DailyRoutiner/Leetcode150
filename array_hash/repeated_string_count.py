# repeated_string_count
# 같은 문자가 연속으로 반복될 경우, 그 횟수를 사용해 문자영을 압축하는 메서드를 구현하라. 가령 압축해야 할 문자열이 aabccccccaaa라면 a2b1c5a3 과 같이 압축되어야 한다. 압축 결과로 만들어지는 문자열이 원래 문자열보다 짧아지지 않는 경우, 이 메서드는 원래 문자열을 그대로 반환해야 한다.

# 접근법: 문자열을 순회하면서 새로운 문자열에 문자들을 복사해 넣고 반복되는 카운트를 넣는다

a1 = "aabccccccaaa"

def compress_string(string):
    compressed = ""
    count = 0
    
    for i in range(len(string)):
        count += 1
        print(i , len(string))
        if i+1 >= len(string) or string[i] != string[i+1]:
            compressed += string[i] + str(count)
            print(compressed)
            count=0

    # 압축 결과 문자열이 원래 문자열보다 길 경우 원래 문자열 반환
    if len(compressed) >= len(string):
        return string
    
    return compressed



# 내 버전
def compress_string1(str1):
   
   str_dict = character_string(str1)
   compress_str = [ f"{k}{v}" for k, v in str_dict.items()]
   print("".join(compress_str))


def character_string(s1:str) -> dict:
    last = ''
    str_dict = {}
    for c in s1: 
        if c in str_dict and c == last: # 여기에 문제가 있음... 딕셔너리에 넣으면 안되네..
            str_dict[c] += 1
        else:
            last = c
            str_dict[c] = 1
    return str_dict


print(compress_string(a1))




