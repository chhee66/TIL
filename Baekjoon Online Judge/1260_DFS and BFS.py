data1 = list(map(int, input().split()))
N = data1[0]
M = data1[1]
V = data1[2]

DFS = {}
BFS = {}

for i in range(1, N+1):
    DFS[i] = list()
    BFS[i] = list()
    
for j in range(0, M):
    data2 = list(map(int, input().split()))
    DFS[data2[0]].append(data2[1])
    DFS[data2[1]].append(data2[0])
    BFS[data2[0]].append(data2[1])
    BFS[data2[1]].append(data2[0])

# DFS = BFS = dict # 모두 같은 id를 가지는 복사 방법. 하나를 변경하면 모두 똑같이 적용됨.
'''
# dictionary를 다른 id로 복사하는 방법
# (+) 다른 id로 복사했는데도 서로 영향을 미친다.
DFS = {}
BFS = {}
for k, v in dict.items():
    DFS[k]=v
    BFS[k]=v
'''

# 공통 함수_1
def delete_from_list(list_name, num):
    for i in range(1, N+1):
        if num in list_name[i]:
            list_name[i].remove(num)

# 공통 함수_2
def search_exist_list(list_name):
    count = 0
    for i in range(1, N+1):
        if list_name[i]:
            return i
        else :
            count = count+1
    if count==N :
        return 0 #전체 종료
            
def check_relation(list_name, num):
    for i in range(1, N+1):
        if num in list_name[i]:
            return "OK"
    return "NO"
    
############### DFS ###############
def DFS_(first):
    if(first==0):
       quit
    main_key = first
    print('\nDFS:',DFS)
    if check_relation(DFS, main_key) == "OK":
        delete_from_list(DFS, main_key)
        if DFS[main_key]:
            return min(DFS[first])
        else :
            return search_exist_list(DFS)
    else :
        return 0


key=V
print(key, end=' ')
while (DFS_(key)) :   # key로 바꿔보자.
    key = DFS_(key)
    if key!=0 :
        print(key, end=' ')

print()
'''
############### BFS ###############

def BFS_(first):
    print(first, end=' ')
    delete_from_list(BFS, first)
    if BFS[first]:
        while (BFS[first]) :
            minimum = min(BFS[first])
            print(minimum, end=' ')
            delete_from_list(BFS, minimum)
            BFS[minimum] = list()
    return search_exist_list(BFS)

key=V
while (key != 0):
    key = BFS_(key)
'''
