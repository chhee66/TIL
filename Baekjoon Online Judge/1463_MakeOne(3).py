# MakeOne3.py
# Sol-3.
N = int(input("choose a number : "))
dict = {0:9999999, 1:0}

for i in range(2, N+1):
    min = 1
    cnt=0
    can = [0, 0, 0, 0]

    can[1]=i-1
    if i%2==0:
        can[2]=int(i/2)
    if i%3==0:
        can[3]=int(i/3)

    key=1
    for k in range(2, 4):
        if dict[can[key]] > dict[can[k]]:
            key=k

    if (i-1)==can[key]:
        cnt = cnt+1
        dict[i]= cnt+dict[can[key]]
    elif (i/2)==can[key]:
        cnt = cnt+1
        dict[i]= cnt+dict[can[key]]
    elif (i/3)==can[key]:
        cnt = cnt+1
        dict[i]= cnt+dict[can[key]]

print(dict[N])
