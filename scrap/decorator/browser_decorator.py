from functools import wraps
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

def connection_idd(func):
    """_summary_
        크롬 브라우저 접속 및 링크 연결
    """
    @wraps(func)
    def exec_func(keyword):   
        # Issue Indeed 403 Fix
        # ------------------------------------------------------
        # 내용    : 초기 indeed사이트 접근시 bot인지 구분 없이 접근 허용
        #          현재 bot으로 접근하는 경우 차단되어 403 상태 코드 발생
        # ------------------------------------------------------
        # 해결방법 : BeautifulSoup 대체제로 Selenuium 사용
        #        : Selenium은 코드를 사용해서 브라우저를 자동화 할 수 있음
        #        : 크롬으로 접근 후 indeed로 접근시켜 indeed가 bot으로 인지하지 못하게 함

        chrome_options = Options()
        # chrome_options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지 코드

        # 크롬드라이버를 최신으로 유지해줍니다.
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) 
        browser.get(f"https://kr.indeed.com/jobs?q={keyword}")

        return func(keyword, browser=browser)
    return exec_func
