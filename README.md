Create word clouds and auto-post after crawling yesterday's posts

https://github.com/pdjdev/daily_dcwc/blob/master/run.py
pdjedv 님의 워드클라우드 봇 프로젝트를 참고했습니다.

Beautifulsoup4와 Selenium을 사용하고 있으며, 파이썬 환경은 3.10.4를 사용하고 있습니다.

사용 전 wordcloud, lxml, image, webdriver-manager 라이브러리를 필수로 설치 해야합니다.

기본 폰트는 네이버에서 제공하는 나무고딕 폰트를 사용하고 있습니다.
글꼴 변경을 원하시면 run.py의 45L fontpath에서 경로를 재 지정 해주시면 됩니다.

실행 방법은 run.py의 37L을 참고해 34L의 agent 값을 갱신하고, 40L에 들어가 직접 제외 키워드를 만들어서 link를 갱신해 준 뒤,
48L에 글 작성을 원하는 갤러리 url의 마지막 부분을 입력하고, 70 ~ 71에 워드 클라우드 작성 시 사용할 id, pw값을 입력하면 됩니다.
그렇게 해서 마지막으로 launcher.py을 실행시켜주시면 됩니다. 이후 해당 프로그램은 날짜가 바뀔때마다 하루에 한번씩 워드클라우드를 자동 작성합니다.

추후 수정 예정입니다.

