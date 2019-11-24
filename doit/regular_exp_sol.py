# regular_exp_sol.py
# 점프투파이썬 풀이
data = """
park 800905-1049118
kim  700905-1059119
"""

result = [] # 뒷자리가 *로 바뀐 결과 전체를 저장할 리스트
for line in data.split("\n") :  # 한 단어씩이 아니라 줄씩 나눔
    word_result = []    # 한 줄 안에 있는 단어에 대한 리스트
    for word in line.split(" "):    # 한 줄 안에서 단어를 나눔
        if len(word)==14 and word[:6].isdigit() and word[7:].isdigit(): # 주민등록번호길이=14(타이푼'-' 포함) / 타이푼'-' 앞뒤로 정수인지 확인 (6, 7자리인지는 당연스럽게 알 수 있음)   #나는 정수인지 확인 안함ㅜㅜ
            word = word[:6]+"-"+"*******"
        word_result.append(word)
    result.append(" ".join(word_result))
    
print("\n".join(result))
