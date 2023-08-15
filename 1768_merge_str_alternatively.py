class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:        
        res =''
        
        for i in range(min(len(word1), len(word2))):
            res += word1[i] + word2[i]
        
        return res + word1[i+1:] +word2[i+1:]
    

# test code
if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeAlternately('abc', 'pqr'))
    print(solution.mergeAlternately('ab', 'pqrs'))
    print(solution.mergeAlternately('abcd', 'pq'))