# SumMulNum2.py
# 점프투파이썬의 풀이

result = 0
for n in range(1, 1000):
    if n%3==0 or n%5==0:
        result+=n

print(result)
