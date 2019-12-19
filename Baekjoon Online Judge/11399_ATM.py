# 11399번 : ATM
# 20191219

N = int(input())
P = input().split()     # Python에서 사라질 함수 : atoi() - 따라서 int('string'자료형 사용), float()를 사용
P.sort()
Q = [int(P[0])]
sum=int(P[0])
for i in range(1, N):
    Q.append(Q[i-1]+int(P[i]))
    sum = sum+Q[i]

print(sum)
