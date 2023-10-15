# bisect.py
import bisect

# bisect 모듈은 이진 검색 알고리즘을 이용하여 시퀀스를 검색하고, 정렬된 시퀀스에 값을 삽입하는 기능을 제공한다.
# 60, 70, 80, 90점 별로 등급이 있다고 가정하자. A B C D E F 등급을 매기려면 어떻게 해야할까?


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 99, 67, 70, 89, 90, 100]])


# 다시 연습
result = []

for score in [33,99,67,70,89,90,100]:
    pos = bisect.bisect([60, 70, 80, 90], score)
    grades = 'FDCBA'[pos]
    result.append(grades)

print(f"what is your grade? {result}")



# 추가 다른 함수
# bisect 모듈은 bisect_left()와 bisect_right() 함수를 제공한다.
# bisect_left()는 시퀀스 내에서 needle과 같은 항목이 들어갈 수 있는 가장 왼쪽 인덱스를 반환한다.

print(bisect.bisect_left([1,2,3,4,5], 3))  # 2

# bisect_right()는 시퀀스 내에서 needle과 같은 항목이 들어갈 수 있는 가장 오른쪽 인덱스를 반환한다.

print(bisect.bisect_right([1,2,3,4,5], 3))  # 3

# bisect.insort()는 정렬된 시퀀스 안에 항목을 삽입한다.

a = [1,2,3,4,5]
bisect.insort(a, 3) # 3을 insert 하고 오름차순 정렬
print(a)  # [1, 2, 3, 3, 4, 5]
