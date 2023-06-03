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