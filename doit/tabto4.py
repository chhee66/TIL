# tabto4.py
# 06-5 탭을 4개의 공백으로 바꾸기
# 나의 풀이
'''
def TabTo4(file):
    a = open(file, 'r')
    b = open("b.txt", "a")
    lines = a.readlines()
    
    for line in lines:
        print(line)
        line = list(line)
        print(line)
        print('len=', len(line))
        for i in range(0, len(line)):
            print('before', 'line[', i, '] :', line[i])
            if line[i]=='\t':
                line[i] = '    '   #문자열은 부분 값 변환이 불가능하다. list처럼 되는 줄 알았다.
            print('after', 'line[', i, '] :', line[i])
            print('before', line)
            line = str(line)
            print('after', line)
        b.write(line)

    a.close()
    b.close()
    
TabTo4("C:/Users/seondo/Desktop/박초희/doit/a.txt")

'''
def TabTo4(file):
    a = open(file, 'r')
    b = open("b.txt", "a")
    lines = a.readlines()
    print(lines)
    for line in lines:
        line = list(line)
        for i in range(0, len(line)):
            if line[i] == '\t':
                line[i]='    '
            b.write(line[i])
            
    a.close()
    b.close()

TabTo4("C:/Users/seondo/Desktop/박초희/doit/a.txt")

