# SumMulNum.py
# 나의 풀이 (06-2. 3과 5의 배수 합하기) ==> 틀렸다! 3과 5의 공배수가 중복되었기 때문이다!!!!

import numpy as np

result=0
three = []
five = []

for i in range(3, 1000, 3):
    three.append(i)

for i in range(5, 1000, 5):
    if i in three :
        #print(i)
        #print(five)
        continue    # 3배수에 속하는 수는 제외해주었다. (pass가 아니라 continue)
    five.append(i)

#print(three)
#print(five)

#print(np.add(three,five))  #ERROR : ValueError: operands could not be broadcast together with shapes (333,) (199,)
# 두 개의 리스트의 길이가 달라서 add함수를 적용할 수 없다는 것 같다.

#print(len(three))   #333
#print(len(five))    #133

for i in range(0, 133):
    result += (three[i]+five[i])

for j in range(133, 333):
    result += three[j]

print(result)
