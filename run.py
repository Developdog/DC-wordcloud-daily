import matplotlib.pyplot as plt
# 파이썬 데이터 시각화를 위한 라이브러리
from bs4 import BeautifulSoup
# 웹페이지의 HTML 혹은 XML에서 데이터를 추출하는 피싱 라이브러리
import requests, lxml, os, time, json
# request는 HTTPS 요청을 보내고, 응답을 받는 라이브러리
# lxml은 XML과 HTML을 처리하는 라이브러리
# os는 운영 체제와 상호 작용하는 함수를 제공하는 라이브러리
# time은 시간 제공 라이브러리
# json은 json 데이터 형식을 다루는 라이브러리
from wordcloud import WordCloud, STOPWORDS
# 단어 구름 사용 라이브러리
from base64 import b64encode
# base64는 데이터를 Base64 형식으로 인코딩 및 디코딩하는 함수를 제공하는 라이브러리입니다.
from datetime import datetime, timedelta
# 시간을 다루는 라이브러리 및 시간 차이를 계산하는 라이브러리
from PIL import Image
# 이미지 파일을 다루는 라이브러리
import numpy as np
# 다차원 배열 사용을 위한 라이브러리

def midReturn(val, s, e):
    if s in val:
        val = val[val.find(s)+len(s):]
        if e in val: val = val[:val.find(e)]
    return val
# string val의 s와 e 사이의 값을 잘라내서 반환시킵니다.

def color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl({:d},{:d}%, {:d}%)".format(np.random.randint(25,52),np.random.randint(81,87),np.random.randint(63,88)))
# 워드클라우드 색변경 함수입니다.


agent = 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
headers = {'User-Agent': agent}
# user agent 값 입력
# https://www.whatismybrowser.com/detect/what-is-my-user-agent/ 해당 사이트에서 가져올 수 있음

stopwords = set(STOPWORDS)
link = 'https://pastebin.com/raw/fxm3CkKq' # 예시용
r = requests.get(link, headers=headers).text
stopwords.update(r.split('\r\n'))
# PASTEBIN 사이트에서 raw 부분을 이용해 제외 키워드를 입력받는다.

fontpath='NanumGothic.otf'
# 폰트 입력

#gid = ''
# 갤러리ID (수정 필요)

link = 'https://gall.dcinside.com/board/lists/?id=' + gid
# 갤러리 링크

# reupload = ['']
reupload_check = 2
reupload_num = 0
# 만약 갤러리에서 옛날 글이라도 꾸준히 업로드 되는 글이 있을 경우, 해당 글만 날짜 계산에서 제외하기 위해 올린다.
# check는 갤러리에서 자체적으로 재업로드 하는 과거글을 배제하기 위해 사용한다. check 개수와 같으면 갱신을 종료한다.

drange = 1
# 탐색 날짜 범위 (ex. days=1 : 측정 날짜부터 1일 이내, 0:측정 날짜만)
# 설정 날짜의 딱 자정으로 설정됩니다 (ex. 8.18 1:45AM -> 8.18 00:00AM)

client_id = ''
# imgur id 값
api_key = ''
# imgur api키 값을 입력합니다.

id = ''
pw = ''
# 디시인사이드 아이디 및 비밀번호 입력

delaytime = 5
# selenium 사용 시 기본 time 대기 시간

minor = 0
# 마이너 갤러리 = 0 정식 갤러리  = 1

taskdone = False
trial = 0
trialend = 15
# 여기서 트릴은 작업이 실패한 횟수를 뜻합니다. 아래 내용에서는 하나의 작업이 5번 이상 실패하면 실행이 자동 종료되게 만들었습니다.

count = 0
# 해당 날짜 범위 내에 작성된 글 개수를 기입합니다.

r = requests.get('https://gall.dcinside.com/board/lists/?id=' + gid, headers = headers).text
# 해당 갤러리 내용을 텍스트로 입력받는다.
print('갤러리 형식: ')
#마이너, 정식갤러리 판별

contents = []
# 전날 받아온 단어 배열
newword = []
# 새로 등장한 키워드 상위 5개
rank = []
# 상위 5개 단어 순위 값
rank_c = []
# 랭크 색깔 값
filename = "yesterday_order.txt"
# 전날 단어 기록장

if 'location.replace' in r:
    link = link.replace('board/','mgallery/board/')    
    print('마이너')
    minor = 0
else:
    print('정식')
    minor = 1
#마이너 갤러리일 경우 (r의 내용의 값을 받지 못했다면 호출용 함수 location.replace가 그대로 text에 기록된다.)

print("갤러리 이름 : ")
gallname = ''
r = requests.get(link, headers=headers).text
bs = BeautifulSoup(r, 'lxml')
posts = bs.find_all('div', class_='page_head clear')
for p in posts:
    gallname = midReturn(str(p.find('a')), "\">", "<div")
print(gallname)
# 갤러리 이름 가져오기

while not taskdone and trial < trialend:
    try:
        ystday = (datetime.now() - timedelta(days=drange)).replace(hour=0, minute=0, second=0, microsecond=0)
        # 하루 전 날 구하기
        print(ystday, '이후의 게시글을 수집합니다.')

        i = 0
        tdata = ''
        ndata = ''
        fin = False
        r = None
        # 데이터 전부 비우기 및 초기 시작 상태 만들어주기

        while not fin:
            # 만약 읽기가 전부 종료되지 않았을 경우
            
            i += 1
            print('페이지 읽는 중... [{}번째...]'.format(i))
            titleok = False
            # 페이지를 1 부터 읽어옵니다.

            while not titleok:
                r = requests.get(link + '&page=' + str(i), headers = headers).text
                bs = BeautifulSoup(r, 'lxml')
                # requests를 통해 받은 텍스트를 lxml를 통해 HTML 형식으로 변경한다.
                
                posts = bs.find_all('tr', class_='ub-content us-post')
                # bs 내부에서 <tr> 요소가 class = 'ub-content us-post'를 가지는 값을 모두 찾습니다.
                # 해당 부분 확인은 페이지에서 개발자 도구를 사용해서 확인이 가능합니다.

                for p in posts:
                    title = p.find('td', class_='gall_tit ub-word')
                    # 마찬가지로 <td> 중 gall_tit ub-word 클래스를 가지는 타이틀을 찾습니다.
                    # 단 all 과는 다르게 첫번째 요소만 반환합니다.

                    #공지 제외 (볼드태그 찾을때 str 처리 해줘야 찾기가능)
                    if not '<b>' in str(title):
                        titleok = True
                        title = midReturn(str(title), '</em>', '</a>')
                        # 중간 제목 값만 가져옵니다.
                        nick = p.find("td", {"class", "gall_writer ub-writer"})
                        # 닉네임을 가져옵니다. (해당 방법으로도 위의 find와 같은 결과를 보일 수 있습니다.)
                        date = datetime.strptime(p.find('td', class_='gall_date').get('title'), "%Y-%m-%d %H:%M:%S")
                        # 찾은 문자값을 해당 날짜값으로 바꿉니다.
                        print(title + '     ' + str(date))
                        # 제목을 출력합니다.

                        # 초 단위까지는 안 가도록 합니다.
                        # 만약 전날보다 날짜값이 클 경우 string에 넣어줍니다.
                        if date >= ystday:
                            tdata += title + '\n' #제목 값
                            ndata += nick.text.strip() + '\n' #닉네임 값
                            count += 1
                            reupload_num = 0
                        # 전날 날짜보다 날짜값이 작을 경우, 기관 초과를 입력한 다음, fin에 true를 넣어 종료시킨다.
                        elif reupload_num == reupload_check :
                            print('-----------해당 항목은 제외됩니다.-------------')
                            print('기간 초과:', date)
                            fin = True
                            date = ystday
                            break
                        else:
                            print('-----------해당 항목은 제외됩니다.-------------')
                            reupload_num += 1
                        
                if not titleok:
                    print('게시글 크롤링 실패. 15초 후 다시 시도해 봅니다.')
                    i -= 1
                    time.sleep(15)

        taskdone = True

    except Exception as e:
        print('문제가 있습니다. 곧 해당 명령을 재시작합니다.')
        print('오류 메시지:', str(e))
        print('시도 횟수:', str(trial))
        trial += 1
        time.sleep(5)
        continue
        # 예외 메세지 입력 후 다시 시도합니다.

    print()
    print('워드클라우드 생성 중... [1/2]')

    icon = Image.open("cover.jpg").convert("RGBA")
    # 마스크가 될 이미지 불러오기

    mask = Image.new("RGBA", icon.size, (255, 255, 255, 1))
    x, y = icon.size
    mask.paste(icon, (0, 0, x, y), icon)
    mask = np.array(mask)
    # 빈 검은색 이미지를 생성해서 해당 파일을 원본 파일에 붙어넣어 마스크 이미지를 만듭니다.

    #wc_title = WordCloud(font_path=fontpath, background_color='white', collocations=False, stopwords=stopwords, mask=mask).generate(tdata)
    wc_title = WordCloud(font_path=fontpath, background_color='black', collocations=False, stopwords=stopwords,
                         mask=mask, color_func= color_func).generate(tdata)
    # 워드클라우드 폰트와 크기에 맞춰서 생성합니다.
    # 현재 임의로 색 변경을 한 값입니다.

    print('이미지 저장 중...')
    wc_title.to_file('title.png')
    #이미지를 해당 파일로 생성합니다.

    hotkey = sorted(wc_title.words_.items(), key=(lambda x: x[1]), reverse = True)

    if os.path.exists(filename):
        print('파일이 존재합니다.')
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                contents.append(line.strip())
            # 메모장에서 전날 단어 기록 읽어오기

            if contents[0] < datetime.now().strftime("%Y-%m-%d"):
                f = open(filename, 'w', encoding="utf-8")
                f.write(datetime.now().strftime("%Y-%m-%d"))
                f.write("\n")
                for i in range(0, len(hotkey)) :
                    f.write(hotkey[i][0] + "\n")
                    
                # 만약 메모장에 적힌 날짜가 지금 시간보다 작다면
                # 메모장을 금일 단어로 새롭게 갱신합니다.

                f.close()

            for num in range(0, 5):
                try:
                    index = contents.index(hotkey[num][0]) - 1
                    index = index - num
                    index_s = ''
                    if index > 0 :
                            rank_c.append("red")
                            index_s = "△" + str(index)
                    elif index  < 0:
                            rank_c.append("blue")
                            index_s = "▽" + str(abs(index))
                    elif index  == 0:
                            rank_c.append("black")
                            index_s = "-"

                    # 전날 키워드 리스트 위치에서 오늘날 키워드 위치를 빼서 순위 변동 사항을 확인합니다.

                    rank.append(index_s)
                except ValueError:
                    rank.append("NEW")
                    rank_c.append("orange")

            # 가장 상위 단어 5개 순위를 출력합니다.

            for num in range(1, len(hotkey)):
                if hotkey[num][0] not in contents:
                    newword.append(hotkey[num][0])
                if len(newword) == 5:
                    break

            # 전날 없었던 새로운 단어 상위 5개 출력합니다.

    else:
        print("파일이 존재하지 않습니다.")
        f = open(filename, 'w', encoding="utf-8")
        f.write(datetime.now().strftime("%Y-%m-%d"))
        f.write("\n")
        for i in range(0, len(hotkey)):
            f.write(hotkey[i][0] + "\n")

        f.close()

        for i in range(0, 5) :
            rank.append("NEW")
            rank_c.append("orange")

    # wc_title.words_.items()는 딕셔너리의 값을 키 값, 쌍의 형태로 반환합니다.
    # 이후 키 값 중, 값을 기준으로 내림차순으로 정렬하는 형태로 가장 많이 등장한 단어 순으로 정렬합니다.
    # 이후 이 값의 첫번째 값부터 다섯번쨰 값 까지 반환합니다.

    if len(newword) < 5:
        for num in range(0, 5 - len(hotkey)):
            newword.append("X")
    # 새 단어가 없을 경우 "X"값을 추가

    print('\n저장 완료')
    # 작업 완료 값을 넣어줍니다.


if taskdone == True:
    taskdone = False
    trial = 0

    while not taskdone and trial < trialend:
        
        try:
            #이미지 업로드 (해당 코드 사용하면 모바일 유저는 확인 불가능)
            """
            headers = {"Authorization": "Client-ID " + client_id}

            url = "https://api.imgur.com/3/upload.json"
            t_img = ''
            # 만들어진 이미지 정보를 입력합니다.

            print('이미지 업로드 중...')
            r = requests.post(
                url, 
                headers = headers,
                data = {
                    'key': api_key, 
                    'image': b64encode(open('title.png', 'rb').read()),
                    'type': 'base64',
                    'name': 'title.png',
                    'title': gid + ' ' + str(ystday) + ' posts WC'
                }
            )
            # imgur 해당 이미지 업로드를 요청합니다.
            # https://stackoverflow.com/questions/16244183/uploading-a-file-to-imgur-via-python

            t_img = json.loads(r.text)['data']['link']
            # JSON.loads는 r의 JSON 형식 데이터를 파이썬 객체로 변환하는 함수입니다.
            # HTTP 응답의 JSON 데이터에서 'data' 객체의 'link' 값을 추출하여 t_img 변수에 저장하는 역할을 합니다.
            """

            page_source = open('orgpage.txt', 'r', encoding='utf-8').read()
            page_source = page_source.replace('[gallid]', gallname)
            #page_source = page_source.replace('[title_image]', t_img)
            # 이미지 사용 안함.

            print('\n오늘의 핵심 키워드:')

            for i in range(0, 5) :
                page_source = page_source.replace('[hotkey' + str(i+1) + ']', hotkey[i][0])
                print(hotkey[i][0])

            print('\n오늘의 순위 변동:')

            for i in range(0, 5):
                page_source = page_source.replace('[rank' + str(i+1) + ']', rank[i])
                page_source = page_source.replace('[rank' + str(i+1) + 'c]', rank_c[i])
                print(rank[i])
                print(rank_c[i])

            print('\n새로운 키워드 목록')

            for i in range(0, len(newword)):
                page_source = page_source.replace('[newword' + str(i+1) +']', newword[i])
                print(newword[i] + " " + str(i))

            page_source = page_source.replace('[count]', str(count))
            page_source = page_source.replace('[word_count]', str(len(hotkey)))

            open('page.txt', 'w', encoding='utf-8').write(page_source)
            
            # 기존에 기록되어 있던 게시글 값을 받아와 오늘 올릴 게시글을 위해 값을 변경한 텍스트 문서를 만듭니다.

            taskdone = True
            print('작업이 모두 성공하였습니다.')
            print()
  
        except Exception as e:
            taskdone = False
            print('문제가 있습니다. 곧 해당 명령을 재시작합니다.')
            print('오류 메시지:', str(e))
            print('시도 횟수:', str(trial))
            trial += 1
            time.sleep(5)

print('업로드 스크립트 끝.')

#============================글쓰기 시작============================

if taskdone:
    taskdone = False
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    #from selenium_recaptcha_solver import RecaptchaSolver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from pyvirtualdisplay import Display

    # 디시인사이드 자료
    url = 'https://www.dcinside.com/'
    if minor == 0 :
        gall = 'https://gall.dcinside.com/mgallery/board/write/?id=' + gid
    else :
        gall = 'https://gall.dcinside.com/board/write/?id=' + gid
    title = str(ystday.month) + '월 ' + str(ystday.day) + '일 ' + gallname + ' 워드클라우드'
    content = open('page.txt', 'r', encoding="utf8").read()

    """
    # 리눅스를 위한 가상 디스플레이 드라이버 로드 
    display = Display(visible=0, size=(1920, 1080))  
    display.start()
    print('디스플레이 드라이버 로드...')
    """

    # 크롬 환경 변수
    print('환경 변수 설정...')
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920x1080')
    options.add_argument("--lang=ko_KR")
    options.add_argument("--user-agent=" + agent)
    print("User-agent 정보 : " + agent)

    #크롬 드라이버 로드
    print('chromedriver 로드...')
    #웹드라이버 불러오기 - Windows의 경우 웹드라이버를 받은 후 같은 디렉토리에 넣는다.
    service = Service('.\\chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    #driver = webdriver.Chrome('.\\chromedriver',options=options)
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # 아무런 경고가 없다면 이상 없이 작동되는 것입니다.

    # 디시인사이드 로그인 페이지 로드
    print('dcinside 로그인 작업 중...')
    driver.get(url)

    # 아이디
    time.sleep(delaytime)
    driver.find_element(By.NAME, 'user_id').send_keys(id)

    # 패스워드
    time.sleep(delaytime)
    driver.find_element(By.NAME, 'pw').send_keys(pw)

    # 로그인
    time.sleep(delaytime)
    driver.find_element(By.ID, 'login_ok').click()
    time.sleep(delaytime)

    #접속되었는지 닉네임 확인
    name = driver.find_element(By.XPATH, '//*[@id="login_box"]/div[1]/div[1]/div[1]/a/strong')
    print(name.text)
    driver.implicitly_wait(10)

    # 글을 쓰고자 하는 갤러리로 이동
    print('갤러리 글쓰기 페이지 접속...')
    driver.get(gall)
    time.sleep(delaytime)

    # 제목 입력
    print('글 제목 입력중...')
    driver.find_element(By.NAME, 'subject').send_keys(title)
    time.sleep(delaytime)

    # HTML으로 쓰기 방식 변경
    print('HTML 글쓰기 방식 변경...')
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'chk_html').send_keys(Keys.ENTER)
    time.sleep(delaytime)

    # 글쓰기 폼으로 진입
    print('글쓰기 폼으로 프레임 전환...')
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='tx_canvas_wysiwyg']"))
    time.sleep(delaytime)

    #본문 입력
    print('본문 입력중...')
    driver.find_element(By.TAG_NAME, 'body').send_keys(content)
    time.sleep(delaytime)

    # 다시 바깥 창 선택.
    driver.switch_to.default_content()
    driver.find_element(By.ID, 'chk_html').send_keys(Keys.ENTER)
    # 모든 값 입력 이후 다시 chk_html을 해제한다. (아니면 등록 안됨...)
    time.sleep(delaytime)
    
    # 글쓰기 폼으로 다시 프레임 전환
    print('글쓰기 폼으로 프레임 재전환...')
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='tx_canvas_wysiwyg']"))
    time.sleep(delaytime)

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
    driver.switch_to.default_content()
    time.sleep(delaytime)
    # 사진에 방해되지 않게 줄을 처음으로 옮긴 후 다시 페이지 선택

    print('사진 첨부 중...')
    driver.find_element(By.XPATH, '//a[@title="사진"]').send_keys(Keys.ENTER)
    time.sleep(delaytime)
    # 사진 칸 클릭
    
    main = driver.window_handles
    driver.switch_to.window(main[1])
    time.sleep(delaytime)
    # 사진 올리는 팝업창으로 이동

    working_directory = os.getcwd()
    #현재 위치 경로 받아오기

    uploader = driver.find_element(By.XPATH, '//input[@type="file"]')
    uploader.send_keys( working_directory + '\\title.png' )
    time.sleep(delaytime)
    # 팝업창에서 사진 올리기 클릭 후 그 사진 선택

    driver.find_element(By.XPATH, '//button[@class="btn_apply"]').send_keys(Keys.ENTER)
    time.sleep(delaytime)
    driver.switch_to.window(main[0])
    time.sleep(delaytime)
    # 사진 업로드 후 다시 메인 페이지로 복귀
    # 사진 올리는 예제 : https://uipath.tistory.com/197

    #글쓰기 저장

    print('저장 후 전송중...')
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(delaytime)
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, '//button[@class="btn_blue btn_svc write"]').send_keys(Keys.ENTER)
    time.sleep(delaytime)
    #저장 딜레이

    """
    try :
        solver = RecaptchaSolver(driver=driver)
        recaptcha_div = driver.find_element(By.XPATH, '//*[@id="captcha_wrapper"]/div/div/iframe')
        solver.click_recaptcha_v2(iframe=recaptcha_div)
        time.sleep(delaytime)
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, '//button[@class="btn_blue btn_svc write"]').send_keys(Keys.ENTER)
    except :
        print("리캡차가 존재하지 않습니다.")
    # 리캡차 확인 (상위 버전의 리캡처면 작동 안될 가능성이 높음)
    """

    try :
        result = driver.switch_to_alert()
        print(result.text)
        result.accept()
        result.dismiss()
        time.sleep(30)
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, '//button[@class="btn_blue btn_svc write"]').send_keys(Keys.ENTER)
    except :
        print("경고창이 존재하지 않습니다.")
    # 경고창 확인

    #글 잘 썼는지 확인
    temper = driver.current_url
    print('마지막 페이지 : ' + temper)

    #웹페이지 닫기
    print('작업 마무리중...')
    time.sleep(delaytime)
    driver.quit()

    #display.sendstop()
    #display.stop()