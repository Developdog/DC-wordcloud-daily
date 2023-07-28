Create word clouds and auto-post after crawling yesterday's posts

https://github.com/pdjdev/daily_dcwc/blob/master/run.py
pdjedv 님의 워드클라우드 봇 프로젝트를 참고했습니다.

파이썬 환경은 3.10.4를 사용하고 있습니다.

## 설치 라이브러리
사용 전 Beautifulsoup4, selenium, wordcloud, lxml, image, webdriver-manager, pyautogui 라이브러리를 필수로 설치 해야합니다.

## 실행 방법
  1. variable.py의 10L, 14L, 15L에 각각 갤러리 아이디, 이름, 비밀번호를 입력합니다.
  2. checkmyagent.py를 이용해 variable.py의 42L을 갱신합니다.
  5. 마지막으로 launcher.py을 실행시켜주시면 됩니다.
 
이후 해당 프로그램은 날짜가 바뀔때마다 하루에 한번씩 워드클라우드를 자동으로 제작하여 작성합니다.
이전 날짜 워드클라우드 사진 및 기록 파일은 그대로 lastorder 파일에 저장됩니다.

## 옵션
제외 키워드를 추가하고 싶은 경우에는 variable.py의 48L 링크로 들어가 직접 제외 키워드를 만들어서 link를 갱신하실 수 있습니다.

기본 폰트는 우아한 형제에서 제공하는 배달의민족 한나체를 폰트로 사용하고 있습니다.<br>
글꼴 변경을 원하시면 variable.py의 18L fontpath에서 파일 이름을 변경해주시면 됩니다.

현재 워드클라우드 마스크를 사용하고 있습니다. <br>
마스크를 변경하시려면 cover.jpg의 이미지를 바꿔주시면 됩니다.

디시인사이드 글쓰기 페이지에 들어가 가장 아래로 스크롤을 내린 뒤 글쓰기 마우스 포인터 위치를 기록하여
variable.py의 21L, 22L에 입력해주시면 됩니다.
매크로 감지를 피하기 위한 방법이며, 해당 방법은 추후에 수정할 예정입니다.
