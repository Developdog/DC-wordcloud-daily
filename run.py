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
import random
# 랜덤용
from PIL import Image
from io import BytesIO
import win32clipboard
# 복사 붙여넣기 용
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# 단어 구름 사용 라이브러리
import pyautogui
# 마우스 이동 라이브러리
import traceback
# 오류 로그 출력 라이브러리

# ============================일반 변수============================

minor = 0
# 마이너 갤러리 = 0 정식 갤러리  = 1

f = open('./variable.txt', 'r', encoding='utf-8')
gid = f.readline().replace('\n', '')
id = f.readline().replace('\n', '')
pw = f.readline().replace('\n', '')
f.close()
# ex) gid = 'aoegame'
# 갤러리 아이디, 디시인사이드 아이디, 비밀번호 순
# 갤러리ID, 디시인사이드 아이디 및 비밀번호 입력

fontpath = 'font.otf'
# 폰트 입력

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

reupload_check = 5
reupload_num = 0
# 만약 갤러리에서 상위로 재업로드 하는 글이 있을 경우, 해당 글만 날짜 계산에서 제외하기 위해 올린다.
# check는 갤러리에서 자체적으로 재업로드 하는 과거글을 배제하기 위해 사용한다.
# 종료 날짜 이후의 값이 있을 경우 num을 카운트하고, check 개수와 같으면 갱신을 종료한다.

delaytime = 5
# selenium 사용 시 기본 time 대기 시간

taskdone = False
trial = 0
trialend = 10
# 작업이 실패한 횟수 설정, 작업 횟수(trial)가 trialend번 실패하면 종료.

count = 0
# 해당 날짜 범위 내에 작성된 글 개수를 기입합니다.

contents = []
# 전날 단어 데이터 배열
newword = []
# 새 키워드 상위 5개
rank = []
# 상위 5개 단어 순위 값
rank_c = []
# 상위 단어 등수 색깔 값
filename = "last_order.txt"
# 전날 단어 기록장

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36"
}
# 해더 설정

# ============================일반 변수 완료료============================

def midReturn(val, s, e):
    if s in val:
        val = val[val.find(s)+len(s):]
        if e in val: val = val[:val.find(e)]
    return val
# string val의 s와 e 사이의 값을 잘라내서 반환시킵니다.

print('갤러리 형식: ', end='')
r = requests.get(link, headers=headers).text
if 'location.replace' in r:
    link = link.replace('board/','mgallery/board/')
    print('마이너')
    minor = 0
else:
    print('정식')
    minor = 1
# 마이너 갤러리일 경우 (r의 내용의 값을 받지 못했다면 호출용 함수 location.replace가 그대로 text에 기록된다.)

print("갤러리 이름 : ", end='')
gallname = ''
r = requests.get(link, headers=headers).text
bs = BeautifulSoup(r, 'lxml')
posts = bs.find_all('div', class_='page_head clear')
for p in posts:
    gallname = midReturn(str(p.find('a')), "\">", "<div")
print(gallname)
# 갤러리 이름(한글) 가져오기

while not taskdone and trial < trialend:
    try:
        # 하루 전 날 구하기
        print(str(endday.strftime("%Y-%m-%d %H:%M:%S")) + ' ~ ' + str(startday.strftime("%Y-%m-%d %H:%M:%S")) +' 사이의 게시글을 수집합니다.')

        i = 0
        tdata = ''
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
                r = requests.get(link + '&page=' + str(i), headers=headers).text
                bs = BeautifulSoup(r, 'lxml')
                # requests를 통해 받은 텍스트를 lxml를 통해 HTML 형식으로 변경한다.i
                
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
                    print('게시글 크롤링 실패.',delaytime,'초 후 다시 시도해 봅니다.')
                    i -= 1
                    time.sleep(delaytime)

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
ran = random.randrange(0,3)
icon = Image.open("cover" + str(ran) + ".png")
# 마스크가 될 이미지 불러오기

mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon, icon)
mask = np.array(mask)
# 마스크 이미지를 만듭니다.

wc_title = WordCloud(font_path=fontpath, background_color='black', collocations=False, stopwords=stopwords, prefer_horizontal=1,
                     mask=mask).generate(tdata)
# 워드클라우드 폰트와 크기에 맞춰서 생성합니다.
# font_path 글꼴 기록, stopwords 글꼴 제거, prefer_horizontal 0은 수직, 1은 수평, 없앨 경우 랜덤

image_colors = ImageColorGenerator(mask)
image_colors.default_color = [0.6,0.6,0.6] # any value for RGB
wc_recolored = wc_title.recolor(color_func=image_colors)

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

        # 상위 단어 5개 순위를 출력합니다. 없을 경우에는 -를 출력합니다.
        # 전날 없었던 새로운 단어 상위 5개를 출력합니다.

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

try:
    shutil.copy(f'./{filename}', f'./lastorder/{startday_str} ~ {endday_str} {filename}')
except FileNotFoundError:
    print("lastorder로 옮길 단어 데이터 파일이 존재하지 않습니다. 계속 진행합니다.")

# wc_title.words_.items()는 딕셔너리의 값을 키 값, 쌍의 형태로 반환합니다.
# 이후 키 값 중, 값을 기준으로 내림차순으로 정렬하는 형태로 가장 많이 등장한 단어 순으로 정렬합니다.
# 이후 이 값의 첫번째 값부터 다섯번쨰 값 까지 반환합니다.

if len(newword) < 5:
    for num in range(0, 5 - len(hotkey)):
        newword.append("X")
# 새 단어가 없을 경우 "X"값을 추가

print("단어 파일 생성 완료")

# ================ 게시글 전용 html 파일 출력 ================

if taskdone == True:
    taskdone = False
    trial = 0

    while not taskdone and trial < trialend:
        
        try:
            page_source = open('orgpage.txt', 'r', encoding='utf-8').read()
            page_source = page_source.replace('[gallid]', gallname)

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
            print('html 양식 생성 완료.')
            print()
  
        except Exception as e:
            taskdone = False
            print('html 생성 실패, 재시작 중...')
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
    while True :
        try :
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.common.action_chains import ActionChains

            # 디시인사이드 자료
            url = 'https://www.dcinside.com/'
            if minor == 0 :
                gall = 'https://gall.dcinside.com/mgallery/board/write/?id=' + gid
            else :
                gall = 'https://gall.dcinside.com/board/write/?id=' + gid
            title = str(startday.month) + '월 ' + str(startday.day) + '일 ' + gallname + ' 땃지 키워드'

            content = []
            file = open('page.txt', 'r', encoding="utf8")
            content = file.readlines()
            file.close()

            #크롬 드라이버 로드
            print('chromedriver 로드...')
            options = Options()
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option('useAutomationExtension', False)
            # 매크로 회피용

            driver = webdriver.Chrome(options=options)
            # 시스템에 이미 설치된 기본 ChromeDriver를 사용.

            action = ActionChains(driver)

            # 디시인사이드 로그인 페이지 로드
            print('dcinside 로그인 작업 중...')
            driver.get(url)
            driver.maximize_window()

            # 아이디
            driver.find_element(By.NAME, 'user_id').send_keys(id)
            driver.find_element(By.NAME, 'pw').send_keys(pw)
            driver.find_element(By.ID, 'login_ok').click()
            time.sleep(delaytime)

            # 글을 쓰고자 하는 갤러리로 이동
            print('갤러리 글쓰기 페이지 접속...')
            driver.get(gall)
            time.sleep(delaytime)

            # 제목 입력
            print('글 제목 입력중...')
            driver.find_element(By.XPATH, '//*[@id="subject"]').send_keys(title)
            time.sleep(delaytime)
            pyautogui.moveTo(100, 200)

            # 이미지 복사하기
            print('이미지 복사 중...')
            image = Image.open("./title.png") # 수정
            
            # 이미지 데이터를 BMP 형식으로 변환
            output = BytesIO()
            image.convert("RGB").save(output, "BMP")
            bmp_data = output.getvalue()[14:]  # BMP 헤더 제거
            output.close()

            # 클립보드에 이미지 복사
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, bmp_data)
            win32clipboard.CloseClipboard()
            print('이미지 복사 완료...')

            # 글쓰기 창 선택 (말머리 유무 확인 //*[@id="write"]/div[4]/div[3]/div[2])
            #driver.find_element(By.XPATH, '//*[@id="write"]/div[4]/div[4]/div[2]').click()
            driver.find_element(By.CLASS_NAME, 'note-editable').click()
            time.sleep(delaytime)
            
            # pyautogui.hotkey('ctrl', 'v')
            action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            pyautogui.moveTo(300, 400)
            time.sleep(delaytime)

            # HTML으로 쓰기 방식 변경
            print('HTML 글쓰기 방식 변경...')
            driver.find_element(By.XPATH, '//*[@id="chk_html"]').click()
            pyautogui.moveTo(500, 600)

            #본문 입력
            print('본문 입력중...')

            # 라즈베리파이 전용
            # for i in content :
            #     i = i.strip()
            #     if i.find('/') != -1 :
            #         driver.find_element(By.XPATH, '//*[@id="write"]/div[3]/div[3]/textarea').send_keys(Keys.ALT + i)
            #     else :
            #         driver.find_element(By.XPATH, '//*[@id="write"]/div[3]/div[3]/textarea').send_keys(i)
            driver.find_element(By.XPATH, '//*[@id="write"]/div[4]/div[3]/textarea').send_keys(content)
            time.sleep(delaytime)

            # 다시 바깥 창 선택.
            driver.switch_to.default_content()
            
            # 모든 값 입력 이후 다시 chk_html을 해제 (생략할 경우 글쓰기 버튼 미활성)
            driver.find_element(By.XPATH, '//*[@id="chk_html"]').click()
            pyautogui.moveTo(700, 800)


            #글쓰기 저장
            print('저장 후 전송중...')

            # 해당 요소를 찾아 자동스크롤 및 마우스 이동, 글쓰기 클릭
            element = driver.find_element(By.XPATH, '//button[@class="btn_blue btn_svc write"]')
            driver.execute_script("arguments[0].scrollIntoView();", element)
            driver.find_element(By.XPATH, '//button[@class="btn_blue btn_svc write"]').click()
            time.sleep(delaytime)

            # 목차로 되돌아가여 확인
            temper = driver.current_url
            print('마지막 페이지 : ' + temper)

            #웹페이지 닫기
            time.sleep(delaytime)
            print('작업 마무리중...')
            break
        except Exception as e : 
            print(e)
            ff = open('Errorlog.txt', 'a+', encoding='utf-8')
            ff.write('\n\n' + str(time.localtime()) + '\n' + str(e) + '\n' + str(traceback.format_exc()))
            ff.closed
            continue
        finally :
            driver.quit()
