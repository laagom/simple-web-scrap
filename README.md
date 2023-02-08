# 웹 스크래퍼

## Goal
여러가지 사이트를 스크랩해서 스크랩 내용을 엑셀로 정리할 수 있는 기능 구현

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

 ## Issue
> ***[23-01-31] Indeed 사이트를 BeatifulSoup으로 접근 시 bot으로 판단하여 접근 차단*** <br>
> 
> - 해결방법 : 동적으로 접근할 수 있는 기능이 있는 Selenium을 사용하여 브라우저 접근 후 Indeed로 접속할 수 있게 개선

>

> ***[23-02-07] Selenium으로 사이트에 접근 시 운영체제에서 브라우저를 띄워 접근*** <br>
>
> - 해결방법 : option에 브라우저를 띄우지 않는 옵션 headless를 추가 후 특정 사이트에서는 headless까지 탐지하기 때문에 탐지 할 수 없게 user-agent 값을 변경하여 Chrome에서 접근한 것처럼 변경


