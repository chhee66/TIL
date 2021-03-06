﻿# Today I Learned

MARKDOWN 설명 링크 : https://gist.github.com/ihoneymon/652be052a0727ad59601

## 20191123
### T-academy
* https://tacademy.skplanet.com/live/player/onlineLectureDetail.action?seq=130
* "Git과 GitHub로 내 커리어 만들기" 강의를 수강하며 프로필을 꾸민 후, 이 TIL(Today I Learned) Repository를 만들었다. 일일커밋을 이룰 수 있도록 이 Repository에 배운 내용을 적을 계획이다.

## 20191124
### GitHub Tutorial
* https://milooy.wordpress.com/2017/06/21/working-together-with-github-tutorial/
1. 바탕화면에 ```git init``` 후 Repository와 같은 이름의 폴더가 바탕화면에 생성되었다.
2.  해당 TIL 폴더에 JumpToPython 실습 파일이 담겨있는 *doit*폴더를 옮겼다.
3. ```cd```를 통해 해당 폴더로 이동한 후 ```git add .```
4. ```git commit -m "[UPLOAD] JumpToPython ex files from doit folder"```
5. ```git push -u origin master```

## 20200616
### 1260_DFS and BFS (Baekjoon Online Judge)
*  
* Pycharm 단축키
  - Shift + F10 : (RUN shorcut 옆에 선택된) 파일 실행하기
  - Alt + Shift + F10 : 실행할 파일을 선택하여 실행하기
  - F8 : (디버깅시) 한 줄씩
  - F7 : (디버깅시) 함수 내로 들어가기
  - tab : indent multiple lines in pycharm
  - Shift + tab : unindent multiple lines in pycharm
* SVN : subversion (version control system in eclipse)
* Python 개념
  - Python은 이차원배열을 지원하지 않는다. 따라서 이중리스트로 구현해야한다.
```
Matrix = [[0]*N for i in range(N)] # N*N
```

## 20200722
### 1753_최단거리(Shortest Path_Dijkstra) (Baekjoon Online Judge)
* Pycharm 단축키
  - Ctrl+Shift+F10 : 실행(Run)
  - F8 : (디버깅시) 한 줄씩 실행 (=Step Over)
  - F7 : (디버깅시) 함수 안쪽으로 실행 (=Step Into)
  - Ctrl + / : 주석 생성 또는 제거
  - tab : -> (들여쓰기, indent)
  - Shift+tab : <- (내어쓰기, unindent)
 
* Eclipse 단축키
  - F11 : 실행(Run)
  - F6 : (디버깅시) 한 줄씩 실행 (=Step Over)
  - F5 : (디버깅시) 함수 안쪽으로 실행 (=Step Into)
 
* Dynamic arrays
  - JAVA's ArrayList = Python's List

## 20200914
### GitHub 이용에 관하여 조언
* 절댓값 absolute value = abs(x)
* 제목이 제일 중요. 타입을 달아라. feat, fix, docs, style 등...
* 첫 단어는 동사원형(관습적!)+대문자+어느 부분이 어떻게 변했는지 적어주자.
* 가급적이면 영어로 적는 것이 좋다. (나는 한글+영어 둘 다 적자!)_이렇게 영어 실력을 키우는 것도 좋다. 영어 일기도 좋고..
* 본문에는  소스코드를 보지 않아도 어느 부분을 어떻게 수정했는지 알 수 있어야 한다.
* 꼬리말
"이슈" 트래커ID를 추가한다.(중요!)
어떤 부분을 어떻게 고쳤는지 이력 추적이 가능하게!
* 지금부터라도 습관을 기르자~
프로젝트 소개 글 작성하기 (readme.md)
* 레포트, 레시피 쓰듯이 작성해라.
* awesome-readme에 가면 우수한 예시가 있으니, 똑같은 구조로 작성해보자.
* 초심자가 내 프로젝트를 돌려볼 수 있도록 해보자.
* Motivation에 학교 과제 제출용이라고 적어도 괜찮다.
* 뱃지를 달 수도 있다.
* 면접관이 코드를 직접 실행해보는 경우는 드물기 때문에, screenshot에 imove로 찍고 gif로 만든 움짤같은 동영상(?)을 넣자!
* Tech/framework used : 어떤 언어, 어떤 프레임워크 사용
* Features : 기능
* Code Example
플러그인이나, 어떻게 실행하면 좋은지 적어주기
* Installation : 로컬에 설치 방법 (중요!)
* git clone하는 방법도.
초보자도 할 수 있도록!
* Tests : 어떻게 테스트하는지
* Contribute : 당신들이 이 프로젝트에 어떻게 기여할 수 있는지
* fork를 떠서 git clone해주세요 등등.. 상세하게!!! 남겨주세요.
* Credits : 누구와 함께 했다. 누가 도움을 줘서 고맙다. (깃허브나 그 분의 프로필 링크)
* License : gitignore 등등.. 이걸 어떤 용도로 사용할 수 있습니다 등 / 이게 있어야 오픈소스다!
* 내가 관심있는 분야나, 프레임워크가 있으면 
* Watch : 소식을 받고싶다. - 최신기술은 업데이트가 활발하다!
* "번역하기"에 활발히 참여하는 것을 추천!
