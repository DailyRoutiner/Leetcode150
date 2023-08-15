# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.



class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        digits[-1] += 1
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                else:
                    digits[i-1] += 1
            else:
                break
        print(digits)
        return digits

Solution().plusOne([9])
Solution().plusOne([9])
