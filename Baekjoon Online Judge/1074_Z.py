N, r, c = map(int, input().split())
result = 0

def save_points(start, side):
    points = [start, [start[0], start[1]+side], [start[0]+side, start[1]], [start[0]+side, start[1]+side]]
    return points
#print(save_points([0, 0], 2**N)) #[a, b], [a, b+x], [a+x, b], [a+x, b+x]

def Z(start, N, visit):
    points = save_points(start, 2**N)
    for p in points: #p:
        while N>=0:
            visit = Z(p, N-1, visit)
        visit.append(p)
    return visit

#visit에 방문한 순서대로 append()한다. #0부터 시작하니까 인덱스와 순서 동일함.
visit = Z([0, 0], N-1, [])
result = visit.index([r,c])
print(result)
