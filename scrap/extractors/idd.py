from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

from scrap.decorator.common_decorators import timeit

def get_browser():
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

    # 속도 향상을 위한 옵션 해제(1: Enable, 2: Disable)
    # Chrome 브라우저에서 사용되고 있는 다양한 옵션을 사용하지 않게 Disable 처리
    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'javascript' : 2
                                                        , 'popups': 2, 'geolocation': 2, 'notifications' : 2
                                                        , 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2
                                                        , 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2
                                                        , 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2
                                                        , 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2
                                                        , 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2
                                                        , 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2
                                                        }}   
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    # Pageload Strategy 설정 변경
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"

    # 크롬드라이버를 최신으로 유지
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    print('Start selenium by Chrome Browser') 
    return browser

def set_browser(browser, keyword=None, page=0, url=None):
    '''
        ### browser : 초기에 옵션 설정한 broswer를 인자로 전달받아 url만 변경
    '''
    base_url  = 'https://kr.indeed.com/jobs'
    final_url = f"{base_url}?q={keyword}&start={page*10}"

    browser.get(final_url if url == None else url)
    print(final_url if url == None else url)

    return browser

def get_page_count(browser, keyword):
    """ #### 접속 페이지의 paging 개수 #### """
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
    browser_obj = get_browser()

    # 페이징 페이지 수
    pages = get_page_count(browser_obj, keyword)
    
    results = {'site':'Indeed'}
    list = []

    for page in range(pages):
        browser = set_browser(browser_obj, keyword, page)
        
        soup     = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs     = job_list.find_all('li', recursive=False)

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor   = job.select_one("h2 a")
                title    = anchor['aria-label']
                link     = anchor['href']
                url      = f'https://kr.indeed.com{link}'
                company  = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")

                browser_item = set_browser(browser_obj, url=url)
                soup_item = BeautifulSoup(browser_item.page_source, "html.parser")
                thumbnail_img = soup_item.find('img', class_='jobsearch-JobInfoHeader-logo')
                thumbnail = thumbnail_img['src'] if thumbnail_img != None else None

                job_data = {
                    'company'  : company.string.replace(',', ' '),
                    'location' : location.string.replace(',', ' '),
                    'position' : title.replace(',', ' '),
                    'url'      : url,
                    'thumbnail': thumbnail
                }
                list.append(job_data)

    results['list'] = list
    browser.quit()
    
    return [results]