# 단어 값 정렬 및 순서 정렬

"""
import os
from datetime import datetime

filename = "yesterday_order.txt"
# 전날 단어 기록장
yesterday = ["가재", "우럭", "전복", "해삼", "말미잘", "멍게"]
today = ["우럭", "가재", "해삼", "말미잘", "전복", "멍게"]

contents = []
# 전날 받아온 단어 배열
newword = []
# 새로 등장한 키워드 상위 5개
rank = []
# 상위 5개 단어 순위 값

if os.path.exists(filename) :
    print("파일이 존재합니다.")
    with open(filename, "r", encoding="utf-8") as file:
        for line in file :
            contents.append(line.strip())
        # 메모장에서 전날 단어 기록 읽어오기

        if contents[0] < datetime.now().strftime("%Y-%m-%d") :
            f = open(filename, 'w', encoding="utf-8")
            f.write(datetime.now().strftime("%Y-%m-%d"))
            f.write("\n")
            for temp in today:
                f.write(temp + "\n")
            # 만약 메모장에 적힌 날짜가 지금 시간보다 작다면
            # 메모장을 금일 단어로 새롭게 갱신한다.

        for num in range(1, 6) :
            try :
                index = contents.index(today[num])
                rank.append(index - num)
                # 전날에서 오늘날을 빼서 순위를 알아보기
            except ValueError :
                rank.append("New")

        # 가장 상위 단어 5개 순위 정하는 법

        for num in range(1, len(today)) :
            if today[num] not in contents :
                newword.append(today[num])
            if len(newword) == 5 :
                break
            if num == len(today) - 1 and len(newword) < 5 :
                for i in range(0, 5 - len(today)) :
                    today.append("X")

        # 전날 없었던 새로운 단어 상위 5개 출력시키기
        # 만약 상위 5개의 단어가 존재하지 않는다면, X를 강제로 입력시키기

else :
    print("파일이 존재하지 않습니다.")
    f = open(filename, 'w', encoding="utf-8")
    f.write(datetime.now().strftime("%Y-%m-%d"))
    f.write("\n")
    for temp in today :
        f.write(temp + "\n")

    f.close()
"""

# 파일 입출력 저장

"""
import shutil
from datetime import datetime, timedelta

drange = 1

nowday = datetime.now().replace(hour=0, minute=0, second=0)
startday = (nowday - timedelta(days=drange))

print(datetime.now().date())
print(startday)
print(nowday)

# 파일 이름에는 :가 들어갈 수 없기 때문에 값을 -로 변경해줍니다.
startday_str = startday.strftime("%Y-%m-%d %H-%M-%S")
endday_str = nowday.strftime("%Y-%m-%d %H-%M-%S")

filename = "last_order.txt"

shutil.copy(f'./{filename}', f'./lastorder/{startday_str} ~ {endday_str} {filename}')

try:
    shutil.copy('./title.png', f'./lastorder/{startday_str} ~ {endday_str} title.png')
except FileNotFoundError:
    print("lastorder로 옮길 워드클라우드 파일이 존재하지 않습니다. 계속 진행합니다.")

try:
    shutil.copy('./page.txt', f'./lastorder/{startday_str} ~ {endday_str} page.txt')
except FileNotFoundError:
    print("lastorder로 옮길 게시글 html 파일이 존재하지 않습니다. 계속 진행합니다.")

try:
    shutil.copy(f'./{filename}', f'./lastorder/{startday_str} ~ {endday_str} {filename}')
except FileNotFoundError:
    print("lastorder로 옮길 단어 데이터 파일이 존재하지 않습니다. 계속 진행합니다.")
"""

# chrome 드라이버 테스트

"""
url = "https://gall.dcinside.com/"
agent = 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 크롬 환경 변수
print('환경 변수 설정...')
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920x1080')
options.add_argument("--lang=ko_KR")
options.add_argument("--user-agent=" + agent)
print("User-agent 정보 : " + agent)

# 크롬 드라이버 로드
print('chromedriver 로드...')
driver = webdriver.Chrome(service=Service())
# 시스템에 이미 설치된 기본 ChromeDriver를 사용합니다.

driver.maximize_window()
driver.get(url)
time.sleep(10)

#driver.execute_script("window.scrollTo(0, 1000)")
element = driver.find_element(By.XPATH, '//button[@class="btn_blue btn_svc write"]')
driver.execute_script("arguments[0].scrollIntoView();", element)
pyautogui.moveTo(1557, 790)
time.sleep(5)
pyautogui.leftClick()
postion = pyautogui.position()
print(pyautogui.size())
print(postion)
"""

"""
from wordcloud import WordCloud
fontpath = 'Ramche.ttf'
tdata = '아시오? 나는 유쾌하오. 이런 때 연애까지가 유쾌하오. 육신이 흐느적흐느적하도록 피로했을 때만 정신이 은화처럼 맑소. 니코틴이 내 횟배 앓는 뱃속으로 스미면'
wc_title = WordCloud(font_path=fontpath, background_color='black', collocations=False, prefer_horizontal=1,).generate(tdata)
wc_title.to_file('testtitle.png')
"""