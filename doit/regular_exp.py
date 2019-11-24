# regular_exp.py
# 07-1 : 정규표현식 살펴보기

data = """
park 800905-1049118
kim  700905-1059119
"""

l = data.split()

for i in range(0, len(l)):
    num = l[i].split('-')

    if len(num)==2 :
        if len(num[0])==6 and len(num[1])==7 :
            num[1]='*'*7
            l[i] = num[0]+'-'+num[1]

print(l)
    
# for문에서 l의 원소값을 바꾼 것이 반복문을 벗어나도 저장이 되어있을 것인지 헷갈린다.
