# 대박! 나 혼자 풀었는데, 전보다 더 빠르게 풀었다!
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x].append(y)
    matrix[y].append(x)
for j in range(1, n+1):
    matrix[j].sort()

visit = []
def DFS(start, visit):
    visit.append(start)
    for i in matrix[start]:
        if i not in visit:
            visit = DFS(i, visit)
    return visit


def BFS(start) :    # matrix 정렬 필요
    visit = []
    q = deque()
    q.append(start)
    visit.append(start)
    while len(q)!=0 :
        z = q.popleft()
        for e in matrix[z]:
            if e not in visit :
                q.append(e)
                visit.append(e)
    return visit

print(*DFS(v, visit))
print(*BFS(v))
