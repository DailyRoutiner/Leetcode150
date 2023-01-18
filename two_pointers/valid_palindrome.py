import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # data = re.sub(r'[^0-9a-z]','', s.lower())
        # return data == data[::-1]
        pass


sol = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(sol)