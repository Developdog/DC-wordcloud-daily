import time, os
from datetime import datetime

# 대기 시간 : 초 기준
waittime = 120

# 날짜 파일이 없을 경우 새로 생성
if not os.path.isfile('lastupd.txt'): open('lastupd.txt', 'w').write(datetime.now().strftime('%Y-%m-%d'))

while (True):
    # 날짜 파일 내부의 값이 오늘 날짜값과 다르다면 게시글 작업 시작
    if datetime.strptime(open('lastupd.txt', 'r').read(), '%Y-%m-%d').date() < datetime.now().date():

        # 스크립트 실행
        #os.system("lxterminal --command=\"python3 run.py\"")
        #Windows:
        #os.system("python3 run.py")

        with open("run.py", "r", encoding="UTF-8") as file:
            code = file.read()
            exec(code)
        # open을 이용해 해당 파이썬 파일을 열고, read를 이용해 해당 문서를 읽는다.
        # 이후 exec를 사용해 해당 코드를 읽는다.

        open('lastupd.txt', 'w').write(str(datetime.now().date()))
        # 모든 작업이 끝나면 날짜 파일의 날짜를 오늘로 갱신한다.

    print('[' + time.strftime('%Y-%m-%d %H:%M:%S') + ']' + '대기중... (' + str(waittime) + ')')
    time.sleep(waittime)