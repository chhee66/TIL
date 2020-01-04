# 2217번 : Rope
# 20200103

N = int(input())
w = list()
result = list()
max = 0

for i in range(0, N):
    data = int(input())
    w.append(data)
w.sort()

for j in range(0, N):
    sum=w[j]*(N-j)
    if max<sum:
        max = sum

print(max)
