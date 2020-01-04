# 1149번 : RGB거리
# 20200103

def find_neighbor(i, j):    # 함수를 사용하기 전에 정의되어있어야한다. (메인소스코드의 하단 말고 상단에 위치시키기!)
    min = 1001
    
    for k in range(0, 3):
        
        if k==j :
            continue
        else :
            if min>price[i-1][k]:
                min = price[i-1][k]
    return min


N = int(input())
price = []
for i in range(0, N):
    data = list(map(int, input().split()))
    price.append(data)

for i in range(1, N) :
    for j in range(0, 3):
        price[i][j] = price[i][j] + find_neighbor(i, j)

price[N-1].sort()
print(price[N-1][0])
