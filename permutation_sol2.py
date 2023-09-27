#python
# -*- coding: utf-8 -*-
def permutation(s1:str, s2:str):
    if len(s1) != len(s2):
        return False
    
    letters = [0] * 128
    for c in s1:
        letters[ord(c)] += 1
    
    for c in s2:
        letters[ord(c)] -= 1
        if letters[ord(c)] < 0:
            return False
        
    return True

# test code

print(permutation("abc", "cba")) # True
print(permutation("abc", "cb")) # False
print(permutation("abc", "cbad")) # False
print(permutation("abc", "cbb")) # False
