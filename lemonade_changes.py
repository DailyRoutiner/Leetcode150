class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:
        five = ten = 0
        
        for bill in bills:
            if bill == 5: # $5
                five += 1
            elif bill == 10: # $10
                if not five: return False
                five -= 1
                ten += 1
            else: # $20
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True

# test code
sol = Solution()
print(sol.lemonadeChange([5,5,5,10,20])) # True
print(sol.lemonadeChange([5,5,10])) # True
print(sol.lemonadeChange([10,10])) # False
print(sol.lemonadeChange([5,5,10,10,20])) # False
print(sol.lemonadeChange([5,5,5,5,20,20,5,5,20,5])) # False
print("what", sol.lemonadeChange([5,5,5,5,10,5,10,10,10,20])) # True
print(sol.lemonadeChange([5,5,5,5,5,5,5,5,5,20])) # True
print(sol.lemonadeChange([5,5,5,5,5,5,5,5,5,5])) # True
