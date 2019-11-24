# tabto4_sol2.py
# 06-5 탭을 4개의 공백으로 바꾸기
# 점프투파이썬 풀이

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)    #문자열 바꾸기 내장함

f = open(dst, 'w')
f.write(space_content)
f.close()
