# # 기본 for문
# arr = list(range(1,100))

# for i in arr:
#     print(f'{i:2.1f}')

# # 튜플로 for문
# arr2  = ('me', 'my', 'friend', 'jane')

# for item in arr2:
#     print(f'{item:>10}')    # 10자리로 우측정렬

# 합계 for문
# numbers = list(range(1,21,2))  # 1~ 20 에서 홀수만 계산

# res = 0
# for item in numbers:
#     res += item

# print(f'{numbers[-1]} 까지의 총 합은{res} 입니다.')

# 홀수짝수 구분
# numbers = list(range(1,21))  # 1~ 20까지

# for item in numbers:
#     if item % 2 == 0:
#         print(f'{item}은 짝수')

# numbers = list(range(1,21))  # 1~ 20까지

# for item in numbers:
#     if item % 2 == 1:     # if item % 2 != 0:
#         print(f'{item}은 홀수')

# 13이상이면 탈출break 또는 continue계속
from unittest import result


numbers = list(range(1,21))  # 1~ 20까지

# for item in numbers:
#     if item == 15:
#         continue
# for item in numbers:
#     if item > 12:
#         break
#     print(f'{item}은 탈출실패')

## 구구단
# print('**구구단 프로그램**')
# for i in range(2,10): # 2 ~ 9
#     if i == 8:
#         continue   # 8단 싫어,,,,
#     print(f'{i}단 시작')
#     for j in range(1,10): # 1 ~ 9
#          print(f'{i} x {j} ={i * j:2d}', end='       ')
#     print()    # == print('')

# inline for문
a = [1, 2, 3, 4]
result = [i * 3 for i in a]
print(result)

# 기존 for문
t = []
for i in a:
    t.append(i * 3)

print(t)

    

    