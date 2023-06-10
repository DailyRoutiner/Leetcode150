def is_unique(string):
    checker = 0
    for char in string:
        #print(ord(char) , ord('a'), ord('ㄱ'))
        val = ord(char) - ord('a')      # 97 - 97
        if (checker & (val >> 1)) > 0:
            return False
        checker |= (val >> 1)
    return True


def test_is_unique():
    # 유일한 문자열
    assert is_unique("abcdefg") == True
    assert is_unique("hello") == False
    assert is_unique("world") == True
    assert is_unique("unique") == False
    assert is_unique("algorithm") == True
    assert is_unique("") == True  # 빈 문자열은 모든 문자가 유일하므로 True 반환

    # 특수문자와 숫자 포함
    assert is_unique("abc!defg") == True
    assert is_unique("h3ll0") == True
    assert is_unique("w0rld") == False
    assert is_unique("uniq#e") == False
    assert is_unique("@lgorithm") == True

    print("테스트 통과!")


test_is_unique()