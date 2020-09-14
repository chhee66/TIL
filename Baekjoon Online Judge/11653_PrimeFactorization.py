import sys
import math

n = int(sys.stdin.readline())

def find_Prime(n):
    Prime = []  # 소수 리스트 O
    non_Prime = []  # 소수 리스트 X (비소수 리스트)
    for i in range(2, n+1):   # math.sqrt(n)까지? or n까지?
        if len(Prime)==0:   # 소수 리스트에 아무것도 없으면,
            Prime.append(i) # i를 추가한다.
        elif i in non_Prime:    # i가 비소수 리스트에 들어있다면,
            continue    # 넘어간다
        else:
            result = is_Prime(i, Prime)
            if result==0:   # i가 소수가 아니면,
                non_Prime.append(i)
            else:   # i가 소수이면,
                Prime = result
    return Prime

def is_Prime(i, Prime): # 서로 다른 자료형 리턴 가능?
    for p in Prime:
        if (i%p) == 0:
            return 0    # 소수가 아니면 0을 반환
    Prime.append(i)
    return Prime    # 소수이면 소수 리스트를 반환

def primeFactorization(n):
    prime = find_Prime(n)
    for p in prime:
        while (n%p)==0 :
            if(n==0):
                return
            print(p)
            n = int(n/p)

primeFactorization(n)
