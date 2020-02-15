data1 = list(map(int, input().split()))
N = data1[0]
M = data1[1]
V = data1[2]

dict = {}

for i in range(1, N+1):
    dict[i] = list()
    
for j in range(0, M):
    data2 = list(map(int, input().split()))
    dict[data2[0]].append(data2[1])
    dict[data2[1]].append(data2[0])

# print(dict) #COMPLETE

# DFS = BFS = dict # 모두 같은 id를 가지는 복사 방법. 하나를 변경하면 모두 똑같이 적용됨.

# dictionary를 다른 id로 복사하는 방법
DFS = {}
BFS = {}
for k, v in dict.items():
    DFS[k]=v
    BFS[k]=v

'''
############### DFS ###############
# 재귀함수? 반복문(모든 딕셔너리의 원소가 -1이 참일 때까지)?
key=V
print(key, end='')
for k in range(0, N-1):
    for l in range(1, N+1):
        if key in DFS[l]:
            DFS[l].remove(key)
    
    key=min(DFS[key])
    print(' '+str(key), end='')  # 한 줄로 출력하기 end='' 는 띄어쓰기 1번 / end=' ' 는 띄어쓰기 2번
                            # print()에서 ','는 띄어쓰기 자동추가, '+'는 띄어쓰기 없이 출력한다
# Q1. 마지막으로 출력되는 원소가 리스트에 남는다. 모두 빈 리스트인 상태로 종료하고싶다면 어떻게 해야할까?

print()
'''
############### BFS ###############

def delete_from_list(key, value):
    for l in range(1, N+1):
        if l==key:
            BFS[l] = list()
        elif value in BFS[l]:
            BFS[l].remove(value)
        


key=V
print(key, end=' ')
delete_from_list(key, key)
while(1):
    if BFS[key] :
        for n in range(0, len(BFS[key])):
            print(min(BFS[key]), end=' ')
            delete_from_list(key, min(BFS[key]))
    else:
        for m in range(1, N+1):
            if BFS[m] :
                key = m
                print(str(key), end=' ')
                delete_from_list(key, key)
            else:
                exit()
