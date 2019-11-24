# 정규 표현식을 사용

import re #regular의 re인가봄

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}") #앞엔 소괄호, 타이푼은 대괄호, 뒤엔 소괄호가 없다.
print(pat.sub("\g<1>-*******", data))
