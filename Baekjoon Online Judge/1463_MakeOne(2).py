# MakeOne2.py
# 백준 1463번

# Sol-2.
'''
N = int(input("choose a number : "))
dict = {1:0}

for i in range(2, N+1):
    min = 1
    cnt=0
    for j in range(1, i):
        #print('pass')
        # 여기부터 막힘
        if j==1 :
            dict[j]
        if dict[min]>dict[j]:
            print(min, j)
            min=j
            
            if i/3=j:
                i = i/3
                cnt = cnt+1
            elif i/2==j:
                i = i/2
                cnt = cnt+1
            else:
                i = i-1
                cnt = cnt+1
        dict[i]=cnt+dict[j]

print(dict[N])

#    i +{smt} = j
'''
