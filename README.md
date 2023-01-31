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
 
 > - chromedriver
 >  : selenium으로 크롭에 접근하기 위한 드라이버

 > - webdriver-manager==3.8.5
 >  : 크롭드라이버를 최신 버전으로 유지 하기 위한 패키지 

<br>

 ## Issue
> ***[23-01-31] Indeed 사이트를 BeatifulSoup으로 접근 시 bot으로 판단하여 접근 차단*** <br>
> 
> - 해결방법 : 동적으로 접근할 수 있는 기능이 있는 Selenium을 사용하여 브라우저 접근 후 Indeed로 접속할 수 있게 개선
