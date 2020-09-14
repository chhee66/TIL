import sys

n = int(sys.stdin.readline())

def find_Prime(n):
    Prime = []  # 소수 리스트 O
    for i in range(2, n+1):   # math.sqrt(n)까지? or n까지?
        is_prime = True
        if len(Prime)==0:   # 소수 리스트에 아무것도 없으면,
            Prime.append(i) # i를 추가한다.
        else:
            for p in Prime:
                if (i%p) == 0:
                    is_prime = False
                    break
            if is_prime==True:
                Prime.append(i)
    return Prime    # 소수 리스트를 반환

def primeFactorization(n):
    prime = find_Prime(n)
    for p in prime:
        while (n%p)==0 :
            if(n==1):
                return
            print(p)
            n = int(n/p)

primeFactorization(n)
