class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        remain_value = 0
        obj = {}

        for i, n in enumerate(nums):
            remain_value = target - n
            if remain_value in obj:
                return [obj[remain_value], i]
            obj[n] = i
        return




sol = Solution().twoSum([3,2,4], 6)
print(sol)