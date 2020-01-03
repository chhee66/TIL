# 1149번 : RGB거리
# 20200103

N = int(input())
price = []
for i in range(0, N):
    data = list(map(int, input().split()))
    price.append(data)

b = price[:]
for j in range(0, N):
    b[j].sort()
b.sort()
min = b[0][0]

for k in range(0, N):
    idx=-1
    try:
        idx = price[k].index(min)
    except IndexError :
        continue
    finally:
        if idx is not -1:
            break
    
price[k][idx]=-1    
