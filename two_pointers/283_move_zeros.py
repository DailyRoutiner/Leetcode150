class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast] , nums[slow] # is it possible?

            if nums[slow] != 0:
                slow += 1


def test_moveZeroes():
    solution = Solution()

    # Test case 1
    nums1 = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0]

    # Test case 2
    nums2 = [0, 0, 0, 1, 2]
    solution.moveZeroes(nums2)
    assert nums2 == [1, 2, 0, 0, 0]

    # Test case 3
    nums3 = [1, 2, 3, 4, 0]
    solution.moveZeroes(nums3)
    assert nums3 == [1, 2, 3, 4, 0]

    # Test case 4
    nums4 = [0, 0, 0, 0, 0]
    solution.moveZeroes(nums4)
    assert nums4 == [0, 0, 0, 0, 0]

    # Test case 5
    nums5 = []
    solution.moveZeroes(nums5)
    assert nums5 == []

    print("All test cases passed!")

test_moveZeroes()