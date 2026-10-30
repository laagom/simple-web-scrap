# 문제 해결 기록

개발하면서 만난 문제와 해결 과정을 날짜순으로 정리했습니다. 프로젝트 개요는 [README](../README.md)를 참고하세요.

> ***1. [23-01-31] Indeed 사이트를 BeatifulSoup으로 접근 시 bot으로 판단하여 접근 차단***
> 
> - 해결방법 : 동적으로 접근할 수 있는 기능이 있는 Selenium을 사용하여 브라우저 접근 후 Indeed로 접속할 수 있게 개선

>

> ***2. [23-02-07] Selenium으로 사이트에 접근 시 운영체제에서 브라우저를 띄워 접근***
>
> - 해결방법 : option에 브라우저를 띄우지 않는 옵션 headless를 추가 후 특정 사이트에서는 headless까지 탐지하기 때문에 탐지 할 수 없게 user-agent 값을 변경하여 Chrome에서 접근한 것처럼 변경

>

> ***3. [23-02-09] Selenium 속도 개선 필요*** <br>
>
> - 처리방법
> 1. 드라이버를 Headless 옵션주기 (`Issue 2 처리 완료`)
> ```python
>   # 창 숨기는 옵션 추가
>    chrome_options.add_argument('--headless')
>    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
> ```
> 2. 그래픽 카드를 가속하지 않는 옵션 추가
> ```python
>   # 그래픽 카드를 가속하지 않는 옵션 추가
>   chrome_options.add_argument("--disable-gpu")
> ```
> 3. Chrome 브라우저에서 사용되고 있는 불필요한 다양한 옵션을 Disable 처리
> ```python
> # 옵션 해제(1: Enable, 2: Disable)
>    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'javascript' : 2
>                                                        , 'popups': 2, 'geolocation': 2, 'notifications' : 2
>                                                        , 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2
>                                                        , 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2
>                                                        , 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2
>                                                        , 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2
>                                                        , 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2
>                                                        , 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2
>                                                        }}   
>    chrome_options.add_experimental_option('prefs', prefs)
> ```

> 4. Pageload Strategy 설정 변경
> ```python
>   from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
>
>   # Pageload Strategy 설정 변경
>    caps = DesiredCapabilities().CHROME
>    caps["pageLoadStrategy"] = "none"
> ```

>

> ***4. [23-02-13] .csv파일로 생성 중 하나의 keyword애 해당하는 내용에에 ','가 포함***
> - ex) 아래와 같이 데이터 정제 중 Position, Company, Location등 해당하는 내용에 ','가 포함되어 순서가 어긋나는 경우 발생
![Alt text](../static/references/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-02-13%20%EC%98%A4%ED%9B%84%203.28.35.png)
>
> - 처리방법: 데이터 정제 과정에서 keyword(Position, Company, Location)의 ','가 되는 내용을 빈 string으로 대체
> ```python
> job_data = {
>                    'company' : company.string.replace(',', ' '),
>                    'location': region.string.replace(',', ' '),
>                    'position': title.string.replace(',', ' '),
>                    'url'     : link,
>                }
> ```

>

> ***5. [23-02-18] 채용공고 스크랩 시간이 오래걸려 동일한 검색 키워드를 입력해도 스크랩하는데 오랜 시간 소요***
>
> - 처리방법: 처음 검색 시 키워드(keyword)로 스크랩을 해오기 때문에 오래걸리는건 어쩔 수 없다. 하지만 keyword와 검색 리스트를 특정 storage에 저장해 둔 후 다음에 다시 조회 할때 시간이 오래 걸리지 않게 storage에서 정보를 가져와 데이터 처리
> 
> 1. input box에 입력되는 키워드(keyword)는 `localStorage`에 저장하여 다음에 접속 시 해당 키워드가 유지되게 설정
>
> 2. 한번 스크랩한 공고 내용을 server단의 `가상 db(global 변수)`에 저장하여 다음에 해당 키워드로 검색할 시 이전에 검색한 기록을 가져와 화면에 렌더링 처리 

>

> ***6. [23-02-20] 클라이언트와 서버 통신을 fetch에서 axios로 변경***
>
> - 변경사유
> 1. fetch로 서버통신 시 response를 받았을 때 JSON 타입으로 변경하는 코드가 추가 되지만 axios를 사용할 경우 response가 반드시 JSON 타입으로 자동 문자열 변환(stringify)하기 때문에 코드를 간소화 할 수 있음
>
> 2. Axios는 호환되는 브라우저를 고려할 필요가 없지만 ajax or fetch의 경우 모든 브라우저를 지원하지 않기 때문에 호환 되는 브라우저를 고려해야함(물론 브라우저에 호환되는 방법은 존재하지만 코드를 바꿔 고려사항을 없애는게 시간이 단축됨)

```javascript
// 화면 로딩 시 progress bar 진행률 보여주기 
const options = {
    responsType: 'blob',
    onDownloadProgress: function(progressEvnet) {
        const percentComplete = Math.floor((progressEvnet.loaded / progressEvnet.total)*100)
        fill.style.width = percentComplete+"%"
        text.textContent = percentComplete+"%"
    }
}

const response = await axios.get(`/scrap?keyword=`+keyword, options)
const results = await response.data

// 초기화 & 렌더링
removeElements(grids)  
results.map((res)=>{
    render_content(res['list'], res['site'])
})
```

>

> ***7. [23-03-03] Selenium의 처리 속도 개선***<br>
> 문제점 : Selenium으로 채용공고 사이트에 접근하여 데이터를 가져오는데 너무 많은 시간 소요. <br>
> 
> 클라이언트와 서버를 체크한 결과 데이터를 화면에 렌더링하는데는 많은 시간이 소요되진 않고, 서버에서 채용 공고 사이트에 접근 후 가져온 url에 다시 한번 접근하는데 너무 오래 걸리는 문제가 있다. Selenium이 Requests보다 느려 시간이 더 많이 소요되지만 너무 오래 걸려 시간을 측정해 보니 아래와 같은 결과가 나왔다.
> ```bash
>   Function jobs_wwr('python',) {} Took 12.0941 seconds
>   https://kr.indeed.com/jobs?q=python&start=0
>   https://kr.indeed.com/jobs?q=python&start=0
>   .
>   .
>   .
>   Function jobs_idd('python',) {} Took 96.6218 seconds
> ```
> 'we work remotely'와 'Indeed'에서 스크랩하는 결과 12초 + 96초 총 108초가 소요되는 것이다. 'wwr'은 Requests를 사용하고 있고 'idd'는 Selenium을 사용하고 있다. 아무리 인터넷이나 브라우저가 문제가 있더라도 108초가 걸리는 것은 누구나 문제가 있다고 할 것이다. 누가 사이트 스크랩을 해오는데 100초나 기다리고 있겠는가...
>
> - 코드문제<br>
> Selenium을 사용하기 앞서 Selenium과 Browser의 초기 설정  
>```python
>def get_browser(keyword=None, page=0, url=None):
>    chrome_options = Options()
>    chrome_options.add_argument('--headless')
>    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
>
>    # 크롬드라이버를 최신으로 유지
>    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) 
>
>    base_url  = 'https://kr.indeed.com/jobs'
>    final_url = f"{base_url}?q={keyword}&start={page*10}"
>
>    browser.get(final_url if url == None else url)
>
>    return browser
>```
> 초기에 위의 코드와 같이 get_browser()함수에 keyword, page, url을 인자로 해서 설정해주고 있다. 여기서 문제는 페이지에 접근할때 마다 browser를 설정해 주는 것이 문제가 되었다.<br>
>
> 사이트를 접근하여 키워드에 대한 `공고 page갯수를 가져오는데 1번`, page 수마다 접근하는데 `+ page`, 접근한 page에 존재하는 채용공고 url에 다시 한번 접근하여 `채용 공고 기업에 대한 썸네일을 가져오는데 + 공고 수`, 결과적으로 `1+page+공고 수`만큼 초기 설정을 잡고 있던 것이다.
>
> - 코드개선<br>
> url을 변경하여 계속해서 접근해야하기 때문에 초기 설정으로 browser객체를 계속해서 받아 왔는데 이는 Selenium+browser설정과 url설정을 동일한 함수에 작성하여 생긴문제로 판단내렸다. 그래서 초기 설정과 url설정을 분리하여 코드를 개선을 한 후 다시 한번 시간을 측정하려고 한다.
>```python
> def get_browser():
>     # 옵션 생성
>     chrome_options = Options()
>     # chrome_options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지 코드
> 
>     # 창 숨기는 옵션 추가
>     chrome_options.add_argument('--headless')
>     chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
> 
>     # 그래픽 카드를 가속하지 않는 옵션 추가
>     chrome_options.add_argument("--disable-gpu")
> 
>     # 속도 향상을 위한 옵션 해제(1: Enable, 2: Disable)
>     # Chrome 브라우저에서 사용되고 있는 다양한 옵션을 사용하지 않게 Disable 처리
>     prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'javascript' : 2
>                                                         , 'popups': 2, 'geolocation': 2, 'notifications' : 2
>                                                         , 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2
>                                                         , 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2
>                                                         , 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2
>                                                         , 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2
>                                                         , 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2
>                                                         , 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2
>                                                         }}   
>     chrome_options.add_experimental_option('prefs', prefs)
>     chrome_options.add_argument("start-maximized")
>     chrome_options.add_argument("disable-infobars")
>     chrome_options.add_argument("--disable-extensions")
> 
>     # Pageload Strategy 설정 변경
>     caps = DesiredCapabilities().CHROME
>     caps["pageLoadStrategy"] = "none"
> 
>     # 크롬드라이버를 최신으로 유지
>     browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
>     print('Start selenium by Chrome Browser') 
>     return browser
> 
> def set_browser(browser, keyword=None, page=0, url=None):
>     base_url  = 'https://kr.indeed.com/jobs'
>     final_url = f"{base_url}?q={keyword}&start={page*10}"
> 
>     browser.get(final_url if url == None else url)
>     print(final_url if url == None else url)
> 
>     return browser
> ```
> 초기 설정과 url설정을 `get_browser()`와 `set_browser()`로 분리한 후 해당 이벤트 발생 시 `get_browser()`는 한번만 호출하여 초기 설정을 잡고 접근하려고 하는 url이 변경될 때마다 `set_browser()`를 호출하여 browser설정된 url을 변경하였다. 이렇게 코드 변경후 시간 측정한 결과는 아래와 같다.
>```python
>Function jobs_wwr('python',) {} Took 9.4401 seconds
>https://kr.indeed.com/jobs?q=python&start=0
>https://kr.indeed.com/rc/clk?jk=3cbd2f42de625fab&fccid=10d9fdf90a5a21a4&vjs=3
>.
>.
>.
>Function jobs_idd('python',) {} Took 16.3367 seconds
>```
> 초기 100초 넘게 걸리던 스크랩 이벤트가 9+16, 25초로 감축된 결과를 볼 수 있었다. selenium을 처음 사용해봐서 초기 Selenium설정과 Browser설정을 한 번만 잡아도 되는지 모르고 url 접근할 때마다 초기 설정을 반복해서 발생한 구조적 문제였다고 생각한다.
