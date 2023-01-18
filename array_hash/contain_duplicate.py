
class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        obj = set()

        for i in nums:
            obj.add(i)

        if len(obj) == len(nums):
            return False
        else:
            return True


sol = Solution().containsDuplicate([1,2,3,4])
print(sol)
