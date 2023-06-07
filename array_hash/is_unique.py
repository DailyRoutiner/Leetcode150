def is_unique(string):
    checker = 0
    for char in string:
        val = ord(char) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
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