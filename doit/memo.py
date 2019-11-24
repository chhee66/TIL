# memo.py
# 06-4 간단한 메모장 만들기

import sys

option = sys.argv[1]

#print(option)
#print(memo)

if option=='-a':
    memo = sys.argv[2]
    f = open("memo.txt", "a")
    f.write(memo)
    f.write('\n')
    f.close()

elif option=='-v':
    f = open('memo.txt', 'r')
    memo = f.read()
    print(type(memo))
    print(memo)
    f.close()
    
'''    
elif option=='-v': # else if 가 아니라 elif
    f = open('memo.txt', 'r')
    memo = f.readlines()
    print(type(memo))
    for line in memo:
        print(line)
    f.close()
    #print(memo)
'''
