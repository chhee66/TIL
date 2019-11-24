# 8장 종합문제-1.py
data = 'a:b:c:d'
result = data.split(':')
str=''
for i in result:
    str+=i
print(str)
result = '#'.join(str)  # 문자열객체.join('삽입할 문자') 가 아니라, 반대다.
print(result)
