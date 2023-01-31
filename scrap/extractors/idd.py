from requests import get
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

def get_browser(keyword, page=0):
    """ Issue Indeed 403 Fix
        ------------------------------------------------------
        내용    : 초기 indeed사이트 접근시 bot인지 구분 없이 접근 허용
                 현재 bot으로 접근하는 경우 차단되어 403 상태 코드 발생
        ------------------------------------------------------
        해결방법 : BeautifulSoup 대체제로 Selenuium 사용
               : Selenium은 코드를 사용해서 브라우저를 자동화 할 수 있음
               : 크롬으로 접근 후 indeed로 접근시켜 indeed가 bot으로 인지하지 못하게 함
    """
    
    chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지 코드

    # 크롬드라이버를 최신으로 유지해줍니다.
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) 
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}&start={page*10}")
    print(f'Requesting https://kr.indeed.com/jobs?q={keyword}&start={page*10}')
    return browser


def get_page_count(keyword):
    """ 접속 페이지의 paging 개수
    """
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
                    'company'  : company.string,
                    'region'   : location.string,
                    'position' : title,
                    'url'      : f'https://kr.indeed.com{link}'
                }
                results.append(job_data)

    return results





