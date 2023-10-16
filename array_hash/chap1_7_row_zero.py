from pprint import pprint

# M * N 행렬을 순회하면서 0인 원소를 발견하면, 
# 해당 원소가 속한 행과 열의 모든 원소를 0으로 설정하는 알고리즘을 작성하라. 

def set_zeroes1(matrix:[[]]):
    row = [False] * len(matrix)
    col = [False] * len(matrix[0])

    for i in range(len(matrix)):            # row
        for j in range(len(matrix[0])):     # col
            if matrix[i][j] == 0:
                row[i]= True
                col[j]= True

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row[i] or col[j]:
                matrix[i][j] = 0


# def set_zeroes(matrix):
#     rows = set()  # 0이 있는 행의 인덱스를 저장하는 집합
#     cols = set()  # 0이 있는 열의 인덱스를 저장하는 집합
    
#     # 0이 있는 행과 열의 인덱스를 찾음
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 0:
#                 rows.add(i)
#                 cols.add(j)
    
#     # 0이 있는 행의 모든 원소를 0으로 설정
#     for row in rows:
#         for j in range(len(matrix[0])):
#             matrix[row][j] = 0
    
#     # 0이 있는 열의 모든 원소를 0으로 설정
#     for col in cols:
#         for i in range(len(matrix)):
#             matrix[i][col] = 0

matrix = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]
#set_zeroes(matrix)
set_zeroes1(matrix)
pprint(matrix)
# Output:
# [[1, 0, 1],
#  [0, 0, 0],
#  [1, 0, 1]]

# 테스트 케이스 2
matrix = [[0, 1, 2, 0],
          [3, 4, 5, 2],
          [1, 3, 1, 5]]
set_zeroes(matrix)
print(matrix)
# Output:
# [[0, 0, 0, 0],
#  [0, 4, 5, 0],
#  [0, 3, 1, 0]]