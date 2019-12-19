# 11047번 : 동전 0
# 20191206

data = input().split()     # input이 함수명이자 변수명이 되어서 Type Error : 'list' object is not callable. 이라는 오류가 발생하였다.
N = int(data[0])
K = int(data[1])
coins = list()  # 동전 값의 리스트
cnt = 0    # 동전의 갯수

for i in range(0, N):
    won = int(input())
    coins.append(won)

while K!=0 :
    for j in range(1, N+1):
        if coins[N-j]<K :
            #print('coins[%d]:'%(N-j), coins[N-j])
            val = int(K/coins[N-j])
            K = K - (coins[N-j]*val)
            #print('val:',val)
            cnt = cnt + val
            #print('cnt:', cnt)

print(int(cnt))
