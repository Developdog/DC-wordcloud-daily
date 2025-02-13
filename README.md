Create word clouds and auto-post after crawling yesterday's posts

https://github.com/pdjdev/daily_dcwc/
pdjedv 님의 워드클라우드 봇 프로젝트를 참고했습니다.

파이썬 환경은 3.10.11를 사용하고 있습니다.

## 설치 라이브러리
```
pip install shutil matplotlib beautifulsoup4 requests lxml wordcloud numpy scipy pillow pyautogui selenium pywin32
```

## 실행 방법
  1. 폴더에 variable.txt를 생성하여 ID, PW, 주소창의 갤러리 ID를 한줄씩 입력해줍니다.
  2. lastupd.txt를 어제 날짜로 변경합니다.
  3. launcher.py를 실행합니다.
 
이후 해당 프로그램은 날짜가 바뀔 때마다 하루에 한 번씩 게시글들을 읽어와 워드클라우드로 제작하여 게시글을 작성합니다.<br>
이전 날짜 워드클라우드 사진 및 기록 파일은 그대로 lastorder 파일에 저장됩니다.

## 기타
제외 키워드를 추가하고 싶은 경우에는 https://pastebin.com/ 링크로 들어가 직접 제외 키워드를 만들어서 link를 갱신하실 수 있습니다.

run.py의 drange를 통해 탐색할 날짜 범위를 지정할 수 있습니다.<br>
예를 들어 23-07-29 일을 기준으로 1을 설정하면 23-07-28에 게시된 게시글의 모든 제목을 워드클라우드화할 수 있습니다.
