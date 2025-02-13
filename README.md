Create word clouds and auto-post after crawling yesterday's posts

https://github.com/pdjdev/daily_dcwc/blob/master/run.py
pdjedv 님의 워드클라우드 봇 프로젝트를 참고했습니다.

파이썬 환경은 3.10.4를 사용하고 있습니다.

## 설치 라이브러리
' pip install shutil matplotlib beautifulsoup4 requests lxml wordcloud numpy scipy pillow pyautogui selenium pywin32 '

## 실행 방법
  1. variable.txt를 생성하여 ID, PW, 주소창의 갤러리 ID를 입력해줍니다.
  2. lastupd.txt를 어제 날짜로 변경합니다.
  3. launcher.py를 실행합니다.
 
이후 해당 프로그램은 날짜가 바뀔 때마다 하루에 한 번씩 워드클라우드를 자동으로 제작하여 작성합니다.
이전 날짜 워드클라우드 사진 및 기록 파일은 그대로 lastorder 파일에 저장됩니다.

## 옵션
제외 키워드를 추가하고 싶은 경우에는 variable.txt의 73L 링크로 들어가 직접 제외 키워드를 만들어서 link를 갱신하실 수 있습니다.<br>

variable.py의 25L drange를 통해 탐색할 날짜 범위를 지정할 수 있습니다. 만약 23-07-29를 기준으로 1을 설정하면 23-07-28에 게시된 게시글의 모든 제목을 워드클라우드화할 수 있습니다.

기본 폰트는 우아한 형제에서 제공하는 배달의민족 한나체를 폰트로 사용하고 있습니다.<br>
글꼴 변경을 원하시면 해당 글꼴체를 폴더로 가져와 variable.py의 18L인 fontpath에서 파일 이름을 변경해주시면 됩니다.

현재 워드클라우드 마스크를 사용하고 있습니다. <br>
마스크를 변경하시려면 cover1.jpg, cover2.jpg, cover3.jpg의 이미지를 변경해주시면 됩니다.
