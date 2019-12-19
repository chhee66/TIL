# 11399번 : ATM
# 20191219

N = int(input())
if N==0 :
    print('0')
else:
    P = list(map(int, input().split()))    # input().split()으로 받은 후 한 원소마다 int()로 바꾸지 말고, map()을 사용해서 한 줄로 해결!
    P.sort()
    Q = [P[0]]
    sum=P[0]
    for i in range(1, N):
        Q.append(Q[i-1]+P[i])
        sum = sum+Q[i]

    print(sum)
    
    
# Python에서 사라질 함수 : atoi() - 따라서 int('string'자료형 사용), float()를 사용
