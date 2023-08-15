
class Solution:
    def isMonotonic(self, nums: [int]) -> bool:
        if len(nums) <= 1:
            return True
        increase, decrease = True, True

        for n in range(1, len(nums)):
            increase = increase and nums[n] >= nums[n-1]
            decrease = decrease and nums[n] <= nums[n-1]

        return increase or decrease


if __name__ == '__main__':
    nums = [1, 2, 2, 3]
    output = True
    assert Solution().isMonotonic(nums) == output

    nums = [6, 5, 4, 4]
    output = True
    assert Solution().isMonotonic(nums) == output

    nums = [1, 3, 2]
    output = False
    assert Solution().isMonotonic(nums) == output

    print("Passed!")    

