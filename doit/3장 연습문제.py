# 3장 연습문제

'''
# 2
a=1
sum=0

while a<=1000 :
    if a%3 ==0 :
        sum+=a
    a+=1

print("sum =",sum)


# 3
a=1
while a<=5 :
    print('*'*a)
    a+=1

# 4
for num in range(1, 101):
    print(num)

# 5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
avg=0

for i in A :
    sum+=i

avg = sum/len(A)
print("평균은 ", avg, "입니다.")
'''

# 6
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)
