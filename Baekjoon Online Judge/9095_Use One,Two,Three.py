# 20191207
# Baekjoon Oneline Judge No.9095
# 1, 2, 3 더하기

nums = {1:1, 2:2, 3:4}

for i in range(4, 11+1):
    nums[i]=nums[i-1]+nums[i-2]+nums[i-3]

n = int(input()) #테스트 케이스 수

for j in range(0, n):
    key = int(input())
    print(nums[key])
