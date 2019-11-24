# 04장 연습문제
'''
# 1
def is_odd(num) :
    if num%2 == 0 :
        print("짝수입니다.")
    else :
        print("홀수입니다.")
'''        
'''
# 2
list = []
while True:
    number = input("수를 입력해주세요 :")
    if not number :
        break;
    list.append(int(number))
sum=0
for i in range(0, len(list)) :
    sum+=list[i]

avg = sum/len(list)

print("평균은 %s입니다."%avg)
'''
'''
# 3

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)
'''
'''
# 4 | 답 : 3번

print("1번 :","you" "need" "python")
print("2번 :","you"+"need"+"python")
print("3번 :","you", "need", "python")
print("4번 :","".join(["you", "need", "python"]))
'''
'''
# 5
f1 = open("C:/Users/seondo/Desktop/박초희/ex4.txt", "w")
f1.write("Life is too short")
f1.close()  #'w'모드로 작성한 후 열린 파일 객체 f1을 닫아주었다.
f2 = open("C:/Users/seondo/Desktop/박초희/ex4.txt", "r")
print(f2.read())    #readlines를 안 붙여도 출력이 되었다. read()라는 함수도 출력으로 알아두자.
'''
'''
# 5-1
with open("C:/Users/seondo/Desktop/박초희/ex4.txt", "w") as f1:    #with문은 파일을 자동으로 닫아준다.
    f1.write("Life is too short")
with open("C:/Users/seondo/Desktop/박초희/ex4.txt", "r") as f2:
    print(f2.read())
'''
'''
# 6
f = open("C:/Users/seondo/Desktop/박초희/ex4.txt", "a")
data = input()
f.write(data)
f.close()    #사용한 파일은 꼭 닫아주는 것을 잊지 말자!
'''

# 7 | 'a'모드일 때 read가 불가능하다.
f = open("C:/Users/seondo/Desktop/박초희/test.txt", "r")
data = f.read()
print(data)
data = data.replace('java', 'python')   #바뀐 내용을 data에 저장해주어야한다.

f = open("C:/Users/seondo/Desktop/박초희/test.txt", "w")
f.write(data)
f.close()
