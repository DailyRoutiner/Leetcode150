class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix:
            return []
        
        row_start, row_end = 0, len(matrix)-1
        col_start, col_end = 0, len(matrix[0])-1
        
        spiral = []
        while row_start <= row_end and col_start <= col_end:
            for col in range(col_start, col_end+1):
                spiral.append(matrix[row_start][col])
            row_start += 1
            
            for row in range(row_start, row_end+1):
                spiral.append(matrix[row][col_end])
            col_end -= 1
            
            if row_start <= row_end:
                for col in range(col_end, col_start-1, -1):
                    spiral.append(matrix[row_end][col])
            row_end -= 1
            
            if col_start <= col_end:
                for row in range(row_end, row_start-1, -1):
                    spiral.append(matrix[row][col_start])
            col_start += 1
            
        return spiral

# test code
solution = Solution()
print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(solution.spiralOrder([[1,2,3,4,5],[6,7,8,9,10]]))
print(solution.spiralOrder([[1,2],[3,4],[5,6],[7,8],[9,10]]))
