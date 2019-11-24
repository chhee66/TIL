# writedata.py

f = open("C:/Users/seondo/Desktop/new.txt", "w")

for i in range(1, 11):
    data = "%d번째 줄입니다."%i
    f.write(data)

f.close()
