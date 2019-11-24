# GuGu2.py (ver.점프투파이썬)

# result = GuGu(2)

def GuGu(n):
    #print(n) 결과값이 잘 들어오는지 확인
    result = []
    i=1
    while i<10:
        result.append(n*i)
        i = i+1
    return result

print(GuGu(2))
