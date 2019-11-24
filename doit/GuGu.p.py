# GuGu.py

number = int(input("구구단의 수를 입력하세요 : "))
line = []

for i in range(1, 10):
    gugu = number*i
    line.append(gugu)

print(line)
