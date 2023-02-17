# 웹 스크래퍼

## Goal
여러가지 사이트를 스크랩해서 스크랩 내용을 엑셀로 정리할 수 있는 기능 구현
![Alt text](static/references/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-02-18%20%EC%98%A4%EC%A0%84%201.03.34.png) |![Alt text](static/references/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-02-18%20%EC%98%A4%EC%A0%84%204.33.44.png)
--- | --- | 
<br>

## List

- [x] 직업 공고사이트 

  > [weworkremotely](https://weworkremotely.com/)를 스크랩하여 공고 정보를 정리

  > [indeed](https://kr.indeed.com/?from=gnav-jobsearch--indeedmobile)를 스크랩하여 공고 정보 정리

<br>

## Pakages
 > - requests==2.28.2<br>
 >  : 원하는 사이트에 요청을 보내 응답을 받기위한 패키지
 
 > - beautifulsoup4==4.11.1<br>
 >  : 응답받은 웹사이트의 HTML을 키워드를 사용하여 데이터 가공을 위한 패키지

 > - selenium==4.8.0<br>
 >  : 브라우저에 동적이 자동화 기능을 넣기 위해 beautifulsoup 대체제
 
 > - chromedriver<br>
 >  : selenium으로 크롭에 접근하기 위한 드라이버

 > - webdriver-manager==3.8.5<br>
 >  : 크롭드라이버를 최신 버전으로 유지 하기 위한 패키지 

<br>

## Libraries
> - [Pico css](https://picocss.com/docs/)<br>
>   : css을 간편하게 적용시켜주기 위한 라이브러리<br>
>   : 기본적인 css코드만 작성한 후 불필요한 코드의 양을 늘리지 않기 위해 사용한다.  

![Alt text](static/references/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-02-17%20%EC%98%A4%ED%9B%84%208.53.11.png) |![Alt text](static/references/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-02-17%20%EC%98%A4%ED%9B%84%208.54.34.png)
--- | --- | 

<br>

 ## Issue
> ***1. [23-01-31] Indeed 사이트를 BeatifulSoup으로 접근 시 bot으로 판단하여 접근 차단*** <br>
> 
> - 해결방법 : 동적으로 접근할 수 있는 기능이 있는 Selenium을 사용하여 브라우저 접근 후 Indeed로 접속할 수 있게 개선

>

> ***2. [23-02-07] Selenium으로 사이트에 접근 시 운영체제에서 브라우저를 띄워 접근*** <br>
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

>

> ***4. [23-02-13] .csv파일로 생성 중 하나의 keyword애 해당하는 내용에에 ','가 포함***<br>
> - ex) 아래와 같이 데이터 정제 중 Position, Company, Location등 해당하는 내용에 ','가 포함되어 순서가 어긋나는 경우 발생
![Alt text](static/references/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-02-13%20%EC%98%A4%ED%9B%84%203.28.35.png)
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

> ***5. [23-02-18] 채용공고 스크랩 시간이 오래걸려 동일한 검색 키워드를 입력해도 스크랩하는데 오랜 시간 소요***<br>
>
> - 처리방법: 처음 검색 시 키워드(keyword)로 스크랩을 해오기 때문에 오래걸리는건 어쩔 수 없다. 하지만 keyword와 검색 리스트를 특정 storage에 저장해 둔 후 다음에 다시 조회 할때 시간이 오래 걸리지 않게 storage에서 정보를 가져와 데이터 처리
> 
> 1. input box에 입력되는 키워드(keyword)는 `localStorage`에 저장하여 다음에 접속 시 해당 키워드가 유지되게 설정
> 2. 한번 스크랩한 공고 내용을 server단의 `가상 db(global 변수)`에 저장하여 다음에 해당 키워드로 검색할 시 이전에 검색한 기록을 가져와 화면에 렌더링 처리 
