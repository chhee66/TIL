import sys
n = int(sys.stdin.readline())
prime = []

def isPrime(a):
    if a<2: # 0, 1은 소수가 아니다.
        return False
    for i in range(2, a): # a=2일때 동작x, 따라서 2는 True
        if a%i == 0:
            return False
    return True

for i in range(n+1): # 0~100
    if n==1:
        break
    result = isPrime(i)
    if result:
        while (n!=1) and (n % i) == 0:
            print(i)
            n = int(n / i)
