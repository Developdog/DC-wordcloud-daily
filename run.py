import shutil
# 파일 복사 붙여넣기를 위한 라이브러리
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
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# 단어 구름 사용 라이브러리
from base64 import b64encode
# base64는 데이터를 Base64 형식으로 인코딩 및 디코딩하는 함수를 제공하는 라이브러리입니다.
from datetime import datetime, timedelta
# 시간을 다루는 라이브러리 및 시간 차이를 계산하는 라이브러리
from PIL import Image
# 이미지 파일을 다루는 라이브러리
import numpy as np
# 다차원 배열 사용을 위한 라이브러리
from scipy.ndimage import gaussian_gradient_magnitude
# 워드클라우드 용
from variable import *

def midReturn(val, s, e):
    if s in val:
        val = val[val.find(s)+len(s):]
        if e in val: val = val[:val.find(e)]
    return val
# string val의 s와 e 사이의 값을 잘라내서 반환시킵니다.

"""
 def color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl({:d},{:d}%, {:d}%)".format(np.random.randint(25,52),np.random.randint(81,87),np.random.randint(63,88)))
 # 워드클라우드 색변경 함수입니다. 임의의 색깔을 출력할 수 있습니다. 현재는 커버 이미지의 색깔을 가져와서 출력하기 때문에 사용하지 않습니다.
"""

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
        # 하루 전 날 구하기
        print(str(endday.strftime("%Y-%m-%d %H:%M:%S")) + ' ~ ' + str(startday.strftime("%Y-%m-%d %H:%M:%S")) +' 사이의 게시글을 수집합니다.')

        i = 0
        tdata = ''
        #ndata = ''
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

                        # 만약 날짜 값이 찾는 날짜 사이에 있을 경우 tdata에 넣어줍니다.
                        if date >= startday and date <= endday:
                            tdata += title + '\n' #제목 값
                            #ndata += nick.text.strip() + '\n' #닉네임 값
                            count += 1
                            reupload_num = 0
                        # 만약 날짜값이 종료 날짜보다 클 경우에는 그냥 넘어갑니다.
                        elif date > endday :
                            print('------- 날짜값이 죵료 날짜보다 큽니다. 대기중입니다. -------')
                        # 전날 날짜보다 날짜값이 작을 경우, 기관 초과를 입력한 다음, fin에 true를 넣어 종료시킨다.
                        elif reupload_num == reupload_check :
                            print('-----------해당 항목은 제외됩니다.-------------')
                            print('시작 날짜값보다 작습니다. 출력을 종료합니다. :', date)
                            fin = True
                            break
                        else:
                            print('-----------해당 항목은 제외됩니다.-------------')
                            reupload_num += 1
                        
                if not titleok:
                    print('게시글 크롤링 실패. 15초 후 다시 시도해 봅니다.')
                    i -= 1
                    time.sleep(5)

        taskdone = True

    except Exception as e:
        print('문제가 있습니다. 곧 해당 명령을 재시작합니다.')
        print('오류 메시지:', str(e))
        print('시도 횟수:', str(trial))
        trial += 1
        time.sleep(5)
        continue
        # 예외 메세지 출력 후 다시 시도합니다.

    print()

# ============================워드클라우드 생성============================

print('워드클라우드 생성 중... [1/2]')

icon = Image.open("cover.png").convert("RGBA")
# 마스크가 될 이미지 불러오기

mask = Image.new("RGBA", icon.size, (255, 255, 255, 1))
x, y = icon.size
mask.paste(icon, (0, 0, x, y), icon)
mask = np.array(mask)
# 빈 검은색 이미지를 생성해서 해당 파일을 원본 파일에 붙어넣어 마스크 이미지를 만듭니다.

#wc_title = WordCloud(font_path=fontpath, background_color='white', collocations=False, stopwords=stopwords, mask=mask).generate(tdata)
wc_title = WordCloud(font_path=fontpath, background_color='black', collocations=False, stopwords=stopwords, prefer_horizontal=1,
                     mask=mask).generate(tdata)
# 워드클라우드 폰트와 크기에 맞춰서 생성합니다.
# font_path 글꼴 기록, stopwords 글꼴 제거, prefer_horizontal 0은 수직, 1은 수평, 없앨 경우 랜덤

# 배경과 같은 색 입히기
image_colors = ImageColorGenerator(mask)
plt.imshow(wc_title.recolor(color_func=image_colors), interpolation="bilinear")

print('이미지 저장 중...')
wc_title.to_file('title.png')
#이미지를 해당 파일로 생성합니다.

hotkey = sorted(wc_title.words_.items(), key=(lambda x: x[1]), reverse = True)

try:
    shutil.copy('./title.png', f'./lastorder/{startday_str} ~ {endday_str} title.png')
except FileNotFoundError:
    print("lastorder로 옮길 워드클라우드 파일이 존재하지 않습니다. 계속 진행합니다.")


# ================ 단어 데이터 파일을 저장힙니다. =================

if os.path.exists(filename):
    print('단어 데이터 파일이 존재합니다.')
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            contents.append(line.strip())

        # 메모장에서 죵료 날짜 단어를 읽어와 메모장의 날짜와 비교하고, 종료 날짜가 더 크면 메모장의 내용을 바굽니다.
        if datetime.strptime(contents[0], '%Y-%m-%d') < endday :
            print('단어 데이터 파일이 날짜가 종료 날짜보다 작습니다. 데이터 파일 갱신을 시작합니다.')
            print('데이터 날짜 값 : ' + contents[0] + ' 종료 날짜 값' + str(endday))

            try:
                shutil.copy(f'./{filename}', f'./lastorder/{startday_str} ~ {endday_str} {filename}')
            except FileNotFoundError:
                print("lastorder로 옮길 단어 데이터 파일이 존재하지 않습니다. 계속 진행합니다.")

            # 만약 메모장에 적힌 날짜가 지금 시간보다 작다면
            # 메모장을 금일 단어로 새롭게 갱신합니다.

        # ============== 전날 단어 데이터 값과 금일 단어 데이터 값을 비교하여 순위를 매깁니다. =============

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
                rank.append(index_s)
            except ValueError:
                rank.append("NEW")
                rank_c.append("orange")

            # 전날 키워드 리스트 위치에서 오늘날 키워드 위치를 빼서 순위 변동 사항을 확인합니다.

        for num in range(1, len(hotkey)):
            if hotkey[num][0] not in contents:
                newword.append(hotkey[num][0])
            if len(newword) == 5:
                break
            if num == len(hotkey)-1 :
                for temp in range(0, 5 - len(newword)) :
                    newword.append("-")

        # 가장 상위 단어 5개 순위를 출력합니다. 없을 경우에는 -를 출력합니다.
        # 전날 없었던 새로운 단어 상위 5개 출력합니다.

else:
    print("단어 데이터 파일이 존재하지 않습니다.")

    for i in range(0, 5) :
        rank.append("NEW")
        rank_c.append("orange")
        newword.append("-")

    # 단어 데이터 파일이 없을 경우에는 전부 NEW를 출력한다.

f = open(filename, 'w', encoding="utf-8")
f.write(endday.strftime("%Y-%m-%d"))
f.write("\n")
for i in range(0, len(hotkey)):
    f.write(hotkey[i][0] + "\n")

f.close()

# wc_title.words_.items()는 딕셔너리의 값을 키 값, 쌍의 형태로 반환합니다.
# 이후 키 값 중, 값을 기준으로 내림차순으로 정렬하는 형태로 가장 많이 등장한 단어 순으로 정렬합니다.
# 이후 이 값의 첫번째 값부터 다섯번쨰 값 까지 반환합니다.

if len(newword) < 5:
    for num in range(0, 5 - len(hotkey)):
        newword.append("X")
# 새 단어가 없을 경우 "X"값을 추가

print('\n저장 완료')
# 작업 완료 값을 넣어줍니다.

# ================ 게시글 전용 html 파일 출력 ================

if taskdone == True:
    taskdone = False
    trial = 0

    while not taskdone and trial < trialend:
        
        try:
            #이미지 업로드 (해당 코드를 사용하면 모바일 유저가 워드클라우드 이미지 확인이 불가능하기 때문에 폐기)
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
                    'title': gid + ' ' + str(endday) + ' ~ ' + str(startday) + ' posts WC'
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

        try:
            shutil.copy('./page.txt', f'./lastorder/{startday_str} ~ {endday_str} page.txt')
        except FileNotFoundError:
            print("lastorder로 옮길 게시글 html 파일이 존재하지 않습니다. 계속 진행합니다.")

print('업로드 스크립트 끝.')

#============================글쓰기 시작============================

if taskdone:
    import pyautogui
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
    title = str(startday.month) + '월 ' + str(startday.day) + '일 ' + gallname + ' 워드클라우드'
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
    driver = webdriver.Chrome(service=Service())
    # 시스템에 이미 설치된 기본 ChromeDriver를 사용합니다.


    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # 웹드라이버 불러오기 - Windows의 경우 웹드라이버를 받은 후 같은 디렉토리에 넣는다.
    # 주의) 해당 기능을 사용하면 크롬드라이버 버전이 업데이트 될 때마다 재설치해야하는 부작용이 생깁니다.
    #service = Service('.\\chromedriver')
    #driver = webdriver.Chrome(service=service, options=options)
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

    # 사진에 방해되지 않게 줄을 처음으로 옮긴 후 다시 페이지 선택
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
    driver.switch_to.default_content()
    time.sleep(delaytime)

    # 사진 칸 클릭
    print('사진 첨부 중...')
    driver.find_element(By.XPATH, '//a[@title="사진"]').send_keys(Keys.ENTER)
    time.sleep(delaytime)

    # 사진 올리는 팝업창으로 이동
    main = driver.window_handles
    driver.switch_to.window(main[1])
    time.sleep(delaytime)

    # 현재 위치 경로 받아오기
    working_directory = os.getcwd()

    # 팝업창에서 사진 올리기 클릭 후 그 사진 선택
    uploader = driver.find_element(By.XPATH, '//input[@type="file"]')
    uploader.send_keys( working_directory + '\\title.png' )
    time.sleep(delaytime)

    # 사진 업로드 후 다시 메인 페이지로 복귀
    # 사진 올리는 예제 : https://uipath.tistory.com/197
    driver.find_element(By.XPATH, '//button[@class="btn_apply"]').send_keys(Keys.ENTER)
    time.sleep(delaytime)
    driver.switch_to.window(main[0])
    driver.maximize_window()
    time.sleep(delaytime)

    #글쓰기 저장
    print('저장 후 전송중...')
    #driver.execute_script("window.scrollTo(0, 1000)")

    # 해당 요소를 찾아 자동스크롤 및 마우스 이동, 글쓰기 클릭
    element = driver.find_element(By.XPATH, '//button[@class="btn_blue btn_svc write"]')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    pyautogui.moveTo(xbutton, ybutton)
    time.sleep(delaytime)
    pyautogui.leftClick()
    #driver.switch_to.default_content()
    #driver.find_element(By.XPATH, '//button[@class="btn_blue btn_svc write"]').send_keys(Keys.ENTER)
    time.sleep(delaytime)

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
    # 경고창 확인(매크로 한번 탐지되면 계속 듬)
    
    """

    #글 작성이 완료되었는지 확인하기 위해 목차로 되돌아감
    temper = driver.current_url
    print('마지막 페이지 : ' + temper)

    #웹페이지 닫기
    print('작업 마무리중...')
    time.sleep(delaytime)
    driver.quit()

    #display.sendstop()
    #display.stop()