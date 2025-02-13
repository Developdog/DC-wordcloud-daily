import requests
# import base64
# import json
from PIL import Image
from io import BytesIO
import win32clipboard
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pyautogui
import requests
import traceback

try :
    raise ValueError("this is error")
except Exception as e :
    print(e)
    f = open('Errorlog.txt', 'a+', encoding='utf-8')
    f.write('\n\n' + str(e) + '\n' + str(traceback.format_exc()))
    f.closed


# driver = webdriver.Chrome()
# driver.get('https://gall.dcinside.com/mgallery/board/write/?id=guardiantales')

# action = ActionChains(driver)

# print('글 제목 입력중...')
# driver.find_element(By.XPATH, '//*[@id="subject"]').send_keys('hi~~')
# time.sleep(5)

# driver.find_element(By.CLASS_NAME, 'note-editable').click()
# # element = driver.find_element(By.XPATH, '//*[@id="write"]/div[4]/div[3]/div[2]/p[1]/img') 
# # if element : 
# #     print("있습니다.")  
# # else : 
# #     pyautogui.hotkey('ctrl', 'v')
# #     print("없습니다.") 
# # pyautogui.moveTo(300, 400)
# # print('창 선택 완료...')
# action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# time.sleep(5)

# 단어 값 정렬 및 순서 정렬

# for i in range(3):
#     try:
#         print(f"TRY 블록 실행 (i={i})")
#         if i == 1:
#             raise ValueError("예외 발생!")  # 강제로 예외 발생

#     except ValueError as e:
#         print(f"EXCEPT 블록 실행 (i={i}): {e}")
#         continue  # 반복문 계속 진행 (현재 루프 스킵)

#     finally:
#         print(f"FINALLY 블록 실행 (i={i})")  # 항상 실행됨

# content = []
# file = open('page.txt', 'r', encoding="utf8")
# content = file.readlines()

# print('HTML 글쓰기 방식 변경...')
# driver.find_element(By.XPATH, '//*[@id="chk_html"]').click()
# pyautogui.moveTo(400, 300)
# time.sleep(5)

# driver.find_element(By.XPATH, '//*[@id="write"]/div[3]/div[3]/textarea').send_keys(content)
# time.sleep(20)

    # 제목 입력

# pyautogui.hotkey('ctrl', 'v')
# time.sleep(10)

# # requests 라이브러리에서 기본으로 사용하는 User-Agent 문자열을 출력
# default_ua = requests.utils.default_user_agent()
# print("Default User-Agent:", default_ua)

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/115.0.0.0 Safari/537.36"
# }

# r = requests.get('https://gall.dcinside.com/mgallery/board/lists/?id=XXX', headers=headers).text
# print(r)

# image = Image.open("C:\\Users\\user\\Desktop\\Python\\DC-wordcloud-daily\\title.png")

# # 이미지 데이터를 BMP 형식으로 변환
# output = BytesIO()
# image.convert("RGB").save(output, "BMP")
# bmp_data = output.getvalue()[14:]  # BMP 헤더 제거
# output.close()

# # 클립보드에 이미지 복사
# win32clipboard.OpenClipboard()
# win32clipboard.EmptyClipboard()
# win32clipboard.SetClipboardData(win32clipboard.CF_DIB, bmp_data)
# win32clipboard.CloseClipboard()

# # 단어 값 정렬 및 순서 정렬

# driver = webdriver.Chrome()
# driver.get("https://www.editpad.org/")
# driver.find_element(By.XPATH, '//*[@id="contentSec"]/button/img').click()
# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="textform"]/div/div[5]/label/span').click()
# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="editorTextarea"]/div[2]/div[2]').click()
# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="editorTextarea"]/div[2]/div[2]').send_keys(Keys.CONTROL + 'v')
# time.sleep(5)



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


# 워드클라우드 블로그
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# from PIL import Image
# import numpy as np
# from wordcloud import ImageColorGenerator

# tdata = ''

# filename = './lastorder/2025-02-08 00-00-00 ~ 2025-02-09 00-00-00 last_order.txt'
# with open(filename, 'r', encoding="utf-8") as file:
#         for line in file:
#             tdata += (line.strip()) + ' '

# icon = Image.open('./cover0.png')
# mask = Image.new("RGB", icon.size, (255,255,255))
# mask.paste(icon, icon)
# mask=np.array(mask)

# # stopwords=stopwords
# # font_path=fontpath,
# wc_title = WordCloud(background_color='black', collocations=False, prefer_horizontal=1,
#                      mask=mask).generate(tdata)
# # 워드클라우드 폰트와 크기에 맞춰서 생성합니다.
# # font_path 글꼴 기록, stopwords 글꼴 제거, prefer_horizontal 0은 수직, 1은 수평, 없앨 경우 랜덤

# image_colors = ImageColorGenerator(mask)
# image_colors.default_color = [0.6,0.6,0.6] # any value for RGB
# wc_recolored = wc_title.recolor(color_func=image_colors)

# wc_title.to_file('test_title.png')


"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Headless 모드를 사용하기 위해 Xvfb 실행 (리눅스 전용)
#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(1920, 1080))
#display.start()

# Chrome WebDriver 옵션 설정
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Chrome WebDriver 실행
driver = webdriver.Chrome(options=options)

# User-Agent 가져오기
driver.get("https://www.example.com")
user_agent = driver.execute_script("return navigator.userAgent;")
print(user_agent)

# WebDriver 종료
driver.quit()

# Xvfb 종료 (리눅스 전용)
#display.stop()

"""