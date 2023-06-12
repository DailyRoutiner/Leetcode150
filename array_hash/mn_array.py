# 이미지를 표현하는 M * N 행렬이 있다. 이미지의 각 픽셀은 4바이트로 표현된다. 
# 이때 이미지를 90도 회전 시키는 메서드를 작성하라 부가적인 행렬을 사용하지 않고서도 할 수 있겠는가?


def rotate(matrix):
     # 원본 이미지의 너비와 높이 계산
    origin_height = len(matrix)
    origin_width = len(matrix[0])

    rotated_image = [[0] * origin_height for _ in range(origin_width)]

    for i in range(origin_height):
        for j in range(origin_width):
            rotated_image[j][origin_height - i - 1] = matrix[i][j]

    return rotated_image

image = [
    [1, 2, 3 , 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# 이미지 회전
rotated_image = rotate(image)

# 회전된 이미지 출력
for row in rotated_image:
    print(row)   