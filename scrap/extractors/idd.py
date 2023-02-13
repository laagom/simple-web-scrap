from functools import wraps
from requests import get
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def get_browser(keyword, page=0):
    ''' #### Selenium 브라우저 접근 #### '''

    """ Issue Indeed 403 Fix
        ------------------------------------------------------
        내용    : 초기 indeed사이트 접근시 bot인지 구분 없이 접근 허용
               : 현재 bot으로 접근하는 경우 차단되어 403 상태 코드 발생
        ------------------------------------------------------
        해결방법 : BeautifulSoup 대체제로 Selenuium 사용
               : Selenium은 코드를 사용해서 브라우저를 자동화 할 수 있음
               : 크롬으로 접근 후 indeed로 접근시켜 indeed가 bot으로 인지하지 못하게 함
    """

    """ Issue headless 옵션 추가
        ------------------------------------------------------
        내용    : Selenium으로 사이트 접근 시 설정한 브라우저가 켜지는 현상
        ------------------------------------------------------
        해결방법 : option에 --headless 추가
               : 특정 사이트는 headless탐지하여 막고있기 때문에 user-agent설정을 
               : 일반적인 Chrome에서 접근한 것 처럼 설정 값 변경
    """
    
    # 옵션 생성
    chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지 코드

    # 창 숨기는 옵션 추가
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

    # 그래픽 카드를 가속하지 않는 옵션 추가
    chrome_options.add_argument("--disable-gpu")

    # 크롬드라이버를 최신으로 유지
    base_url  = 'https://kr.indeed.com/jobs'
    final_url = f"{base_url}?q={keyword}&start={page*10}"

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) 
    browser.get(final_url)
    print(final_url)

    return browser


def get_page_count(keyword):
    """ #### 접속 페이지의 paging 개수 #### """
    browser = get_browser(keyword)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", attrs={"aria-label": "pagination"})

    if pagination == None:
        return 1

    # 자식 요소까지 접근하지 않게 recursive=False
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)

    if count >= 5:
        return 5
    else:
        return count

@timeit
def jobs_idd(keyword):
    # 페이징 페이지 수
    pages = get_page_count(keyword)
    
    results = []
    for page in range(pages):
        browser = get_browser(keyword, page)
        
        soup     = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs     = job_list.find_all('li', recursive=False)

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor   = job.select_one("h2 a")
                title    = anchor['aria-label']
                link     = anchor['href']
                company  = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")

                job_data = {
                    'company'  : company.string.replace(',', ' '),
                    'location' : location.string.replace(',', ' '),
                    'position' : title.replace(',', ' '),
                    'url'      : f'https://kr.indeed.com{link}'
                }
                results.append(job_data)
    
    browser.quit()
    return results