# 20191212
# 1932_decimal triangle.py
# Baekjoon Online Judge
# No. 1932 : 정수 삼각형(decimal triangle)
# Code Review : 변수가 너무 많아서 헷갈린다.(too much variable)

################################ 변수 선언 ################################

level = int(input()) # 정수 삼각형의 층 개수
triangle = [-999] # 정수 삼각형의 원소 값의 모임    # 비어있는 리스트는 triangle = list()로 생성하는 방법도 있다.
space = [0, 1] #삼각형의 원소 개수 (1층일 땐 1개)
cnt = 2 #현재 레벨
################################ 입력 부분  ################################

for i in range(2, level+1):
    space.append(space[i-1]+i)

for j in range(0, level):
    n = input().split() # 띄어쓰기로 들어오는 문자열의 입력을 나누어서 리스트화
    '''
    if n == None: #입력이 없으면 중지(=그만 입력 받기)
        break # for 문을 탈출한다.
    '''
    for k in range(0, len(n)): # 분리된 입력 갯수 만큼 리스트(triangle)에 추가
        triangle.append(int(n[k]))
        
################################ 중간값을 최대값으로 설정하기 ################################

for m in range(2, space[level]+1):
    if m > space[cnt] :
        cnt = cnt+1 # 다음 레벨 (레벨 2부터 시작)
    
    # 레벨의 첫 번호이면 더할 수 있는 수가 하나이다.
    if m == space[cnt-1]+1 :  # 앞 조건에서 걸리면 뒤 조건도 검사하나?
        triangle[m] = triangle[m] + triangle[m-(cnt-1)]
    # 레벨의 끝 번호이면 더할 수 있는 수가 하나이다.
    elif m == space[cnt] :
        triangle[m] = triangle[m] + triangle[m-(cnt)]
    else :
        a = triangle[m] + triangle[m-(cnt)]
        b = triangle[m] + triangle[m-(cnt-1)]
    # 오른쪽 대각선과 왼쪽 대각선 중 더 큰 것을 선택한다.
        if a>=b :
            triangle[m]=a
        else :
            triangle[m]=b

################################ 최댓값 출력하기 ################################
max = triangle[space[cnt-1]+1] # 해당 레벨의 첫 요소가 최대값이라고 가정한다.
for q in range(space[cnt-1]+2, space[cnt]+1):
    if max < triangle[q] :
        max = triangle[q]

print(max)
