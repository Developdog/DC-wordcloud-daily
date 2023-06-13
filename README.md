Create word clouds and auto-post after crawling yesterday's posts

https://github.com/pdjdev/daily_dcwc/blob/master/run.py
pdjedv 님의 워드클라우드 봇 프로젝트를 참고했습니다.

파이썬 환경은 3.10.4를 사용하고 있습니다.

## 설치 라이브러리
사용 전 Beautifulsoup4, selenium, wordcloud, lxml, image, webdriver-manager 라이브러리를 필수로 설치 해야합니다.

## 실행 방법
  1. run.py의 37L을 참고해 34L의 agent 값을 갱신합니다.
  2. 48L에 글 작성을 원하는 갤러리 url의 마지막 부분을 입력합니다.
  3. 70 ~ 71에 워드 클라우드 작성 시 사용할 id, pw값을 입력하면 됩니다.
  4. 마지막으로 launcher.py을 실행시켜주시면 됩니다.
 
이후 해당 프로그램은 날짜가 바뀔때마다 하루에 한번씩 워드클라우드를 자동 작성합니다.

## 옵션
제외 키워드가 필요 시에는 40L의 링크로 들어가 직접 제외 키워드를 만들어서 link를 갱신하실 수 있습니다.

기본 폰트는 네이버에서 제공하는 나무고딕 폰트를 사용하고 있습니다.<br>
글꼴 변경을 원하시면 run.py의 45L fontpath에서 경로를 재 지정 해주시면 됩니다.

현재 워드클라우드 마스크를 사용하고 있습니다. <br>
마스크를 변경하시려면 cover.jpg의 이미지를 바꿔주시거나, 216L의 wordcloud mask부분과 color_func 부분을 제거하시면 됩니다.

추후 수정 예정입니다.

