data = list(map(int, input().split()))
N = data[0]
M = data[1]
V = data[2]

table[M][M]

for i in range(0, M):
    value = list(map(int, input().split()))
    table[value[0]][value[1]]=1    
