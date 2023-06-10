# permutation.py
# 문자열 두개를 입력으로 받아 그 중 하나가 다른 하나의 순열인지를 판별하는 메소드를 작성하라

# 풀이1 ... 정렬해서 푸는 문제.. 대소문자를 구별해야되는가? 공백도?
# god dog 
a1 = 'god'
b1 = 'dog'

print(a1.replace(" ", ""))


def anagram_string( s1, s2) -> bool:
    

    if len(s1) != len(s2):
        return False

    return character_count(s1) == character_count(s2)


def character_count(str1) -> dict: 
    ana = {}

    for i in str1:
        if i not in ana:
            ana[i] = 1
        else:
            ana[i] += 1 
    print(ana)
    return ana    



print(anagram_count(a1, b1))
