# make test cases
# 1. sort the array
# 2. find the difference between the first two elements
# 3. loop through the array and check if the difference between the current element and the next element is the same as the difference between the first two elements
# 4. if it is, return True
# 5. if it isn't, return False

class Solution:
    def canMakeArithmeticProgression(self, arr: [int]) -> bool:
        arr.sort(reverse=True)

        diff = arr[1] - arr[0]

        for n in range(len(arr)-2):
            if arr[n+2] - arr[n+1] != diff:
                return False

        return True
    

Solution().canMakeArithmeticProgression([3,5,1])
Solution().canMakeArithmeticProgression([1,2,4])
Solution().canMakeArithmeticProgression([1,2])
Solution().canMakeArithmeticProgression([1,2,3,4,5,6,7,8,9,10])