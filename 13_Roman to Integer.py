ROMAN = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        s = s.replace('IV', 'IIII').replace('IX', 'IIIIV')
        s = s.replace('XL', 'XXXX').replace('XC', 'XXXXL')
        s = s.replace('CD', 'CCCC').replace('CM', 'CCCCD')

        for cha in s:
            res += ROMAN[cha]
        
        return res

# make test cases code:
if __name__ == "__main__":
    input1 = "III"
    expect1 = 3
    input2 = "IV"
    expect2 = 4
    input3 = "IX"
    expect3 = 9
    input4 = "LVIII"
    expect4 = 58
    input5 = "MCMXCIV"
    expect5 = 1994
    # fail "MCDLXXVI"

    s = Solution()
    assert s.romanToInt(input1) == expect1
    assert s.romanToInt(input2) == expect2
    assert s.romanToInt(input3) == expect3
    assert s.romanToInt(input4) == expect4
    assert s.romanToInt(input5) == expect5
    print("test cases passed")