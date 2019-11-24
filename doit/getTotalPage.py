# getTotalPage.py
# 06-3 게시판 페이징하기 (나의 풀이_한 번에 성공!)
# divmod를 사용해서 몫과 나머지를 한 번에 구했다는 점,
# 그리고 그 결과는 튜플이라 리스트처럼 인덱싱했다는 점!

result = 0 # 총 페이지 (output) 
m = 0 # 게시물의 총 건수 (input)
n = 0 # 한 페이지에 보여줄 게시물 수 (input)

def getTotalPage(m, n):
    page = divmod(m, n)
    if not page[1]==0:
        result = page[0]+1
    else:
        result = page[0]
        
    return result

print(getTotalPage(30, 10))
