import requests
# request는 HTTPS 요청을 보내고, 응답을 받는 라이브러리
from datetime import timedelta, datetime
# 날짜 시간 출력
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# 단어 구름 사용 라이브러리

# # ============================일반 변수============================

gid = ''
# ex) gid = 'aoegame'
# 갤러리ID

id = ''
pw = ''
# 디시인사이드 아이디 및 비밀번호 입력

fontpath = 'font.otf'
# 폰트 입력

xbutton = 1557
ybutton = 790
# 글쓰기 버튼을 누르기 위한 마우스 X, Y 좌표 (1920 : 1080) 기준입니다.

drange = 1
# 탐색 날짜 범위를 지정합니다.
# (ex. drange가 1이고, enddate의 값이 2023-07-28일 경우, 2023-07-28 00:00 부터 2023-07-27 00:00 까지의 게시글 값을 가져옵니다.)

nowday = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
# 종료날짜와 시작날짜를 활용하기 위해 오늘 날짜를 구해줍니다.

endday = nowday
# 종료 날짜는 오늘을 기준으로 합니다. 임의로 변경 가능합니다.

startday = (nowday - timedelta(days=drange))
# 시작 날짜는 종료 날짜에서 drange일 만큼 뺀 값을 기준으로 합니다. 임의로 변경 가능합니다.

startday_str = startday.strftime("%Y-%m-%d %H-%M-%S")
endday_str = nowday.strftime("%Y-%m-%d %H-%M-%S")
#파일명 입력을 위해 :를 제거한 값을 만들어줍니다.

stopwords = set(STOPWORDS)
link = 'https://pastebin.com/raw/fxm3CkKq' # 예시 메모장 링크입니다. 직접 만들어서 수정하셔도 됩니다.
r = requests.get(link).text
stopwords.update(r.split('\r\n'))
# PASTEBIN 사이트에서 raw 부분을 이용해 워드클라우드 제외 키워드를 추가로 입력받습니다.

link = 'https://gall.dcinside.com/board/lists/?id=' + gid
# 갤러리 링크

reupload_check = 10
reupload_num = 0
# 만약 갤러리에서 상위로 재업로드 하는 글이 있을 경우, 해당 글만 날짜 계산에서 제외하기 위해 올린다.
# check는 갤러리에서 자체적으로 재업로드 하는 과거글을 배제하기 위해 사용한다.
# 종료 날짜 이후의 값이 있을 경우 num을 카운트하고, check 개수와 같으면 갱신을 종료한다.

"""
client_id = ''
# imgur id 값
api_key = ''
# imgur api키 값을 입력합니다.
"""

delaytime = 5
# selenium 사용 시 기본 time 대기 시간

taskdone = False
trial = 0
trialend = 15
# 여기서 트릴은 작업이 실패한 횟수를 뜻합니다. 아래 내용에서는 하나의 작업이 15번 이상 실패하면 실행이 자동 종료되게 만들었습니다.

count = 0
# 해당 날짜 범위 내에 작성된 글 개수를 기입합니다.

r = requests.get('https://gall.dcinside.com/board/lists/?id=' + gid).text
print(r)
#마이너, 정식갤러리 판별

contents = []
# 전날 단어 데이터 배열
newword = []
# 새로 등장한 키워드 상위 5개
rank = []
# 상위 5개 단어 순위 값
rank_c = []
# 상위 단어 등수 색깔 값
filename = "last_order.txt"
# 전날 단어 기록장
