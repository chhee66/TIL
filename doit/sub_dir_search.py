# sub_dir_search.py
# 나의 풀이
# 오답 - '.py'가 파일명 중간에 들어있고 확장자가 '.txt'인 파일도 출력될 수 있다.
'''
import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames :
        if '.py' in filename:
            full_filename = dirname+filename
            print(full_filename)

search("C:/doit/")
'''
'''
# 점프투파이썬 풀이

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames :
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):    #만일 파일=디렉토리 라면
                search(full_filename)    # 재귀함수
            else:    # 파일!=디렉토리 라면          
                ext = os.path.splitext(full_filename)[-1]    # ['파일이름', '확장자']
                if ext == '.py':
                    print(full_filename)
    except PermissionError:    #os.listdir를 수행할 때 권한이 없는 디렉터리에 접근하더라도 프로그램이 오류로 종료되지 않고 그냥 수행되도록 하기 위함이다.
        pass

search("C:/doit/")

'''
# os.walk() 사용
import os

for (path, dir, files) in os.walk("C:/doit"):
    #print(path, dir, files)
    
    for filename in files:
        ext = os.path.splitext(filename)[-1]    # ['파일이름', '확장자']
        if ext == '.py':
            print("%s/%s"%(path,filename))

