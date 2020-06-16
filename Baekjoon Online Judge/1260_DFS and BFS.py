data1 = list(map(int, input().split()))
N = data1[0]
M = data1[1]
V = data1[2]

DFS = {}
BFS = {}
# 연결성 여부를 확인하는 Matrix
# 모든 원소가 0인 (N+1)x(N+1)리스트 생성, 0부터 시작하여 N+1개(1부터 시작하는 노드 번호를 위해서),
Matrix = [[0]*(N+1) for i in range(N+1)] #Python은 이차원배열 대신 이중리스트를 사용한다.

for i in range(1, N + 1):
    DFS[i] = list()
    BFS[i] = list()

for j in range(0, M):
    data2 = list(map(int, input().split()))
    DFS[data2[0]].append(data2[1])
    DFS[data2[1]].append(data2[0])
    BFS[data2[0]].append(data2[1])
    BFS[data2[1]].append(data2[0])
    Matrix[data2[0]][data2[1]] = 1
    Matrix[data2[1]][data2[0]] = 1

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
    for i in range(1, N + 1):
        if num in list_name[i]:
            list_name[i].remove(num)


# 공통 함수_2
def search_exist_list(num):
    for i in range(1, N+1):
        if i in result:
            continue
        else:
            if Matrix[num][i] == 1:
                return i
            else:
                return 0


def check_relation(num):
    for i in range(1, N + 1):
        if Matrix[num][i]==1 :
            return "OK"
    return 0


############### DFS ###############
def DFS_(first):
    if (first == 0):
        quit
    main_key = first
    delete_from_list(DFS, main_key)
    if check_relation(main_key) == "OK":
        if DFS[main_key]:
            return min(DFS[first])
        else:
            return search_exist_list(main_key)
    else:
        return 0


key = V
result = [key]
for i in range(N):
    key = DFS_(key)
    if key == None: #'None'(=문자열) 아님. None으로 입력해야 한다.
        break
    elif key != 0:
        result.append(key)

print(*result, sep=" ")
print('\n')
'''
############### BFS ###############
def BFS_(first):
    result.append(first)
    delete_from_list(BFS, first)
    if BFS[first]:
        while (BFS[first]) :
            minimum = min(BFS[first])
            print(minimum, end=' ')5
            delete_from_list(BFS, minimum)
            BFS[minimum] = list()
    return search_exist_list(BFS)
    
key=V
result = [key] #need?
while (key != 0):
    key = BFS_(key)
print(result)
'''
