# 976. Largest Perimeter Triangle

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        # for i in range(1, len(nums)):
        #     # 마지막 3번째 건 어떻게 뽑지?
        #     if nums[i-1] + nums[i] > nums[-1]:
        #         # 3개 어떻게 더하지?
        #         return sum(nums)
        #     else:
        #         return 0
        
        for i, x in enumerate(nums[:-2]):
            if x < nums[i+1] + nums[i+2]:
                return x + nums[i+1] + nums[i+2]
            
        return 0
