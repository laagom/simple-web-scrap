# 웹 스크래퍼

Django로 만든 **채용공고 스크래퍼**입니다. 키워드로 We Work Remotely와 Indeed의 공고를 수집해 화면에 보여 주고, CSV 파일로 내려받을 수 있습니다.

## 기술 스택

Python · Django 3.2 · requests · BeautifulSoup4 · Selenium (webdriver-manager)

## 구조

```text
config/                 Django 설정, 루트 URL
scrap/
├─ views.py             홈, 검색, 스크랩, CSV 내보내기 뷰
├─ extractors/          사이트별 스크랩 (wwr.py, idd.py)
├─ file.py              스크랩 결과를 CSV로 저장
└─ decorator/           실행 시간 측정 데코레이터
templates/              home.html, index.html
files/                  스크랩 결과 CSV 예시
```

## 주요 경로

| 경로 | 설명 |
|---|---|
| `/` | 홈 화면 |
| `/search/` | 키워드 검색 화면 |
| `/scrap/` | 스크랩 실행 (JSON 응답) |
| `/export/` | 스크랩 결과를 CSV로 다운로드 |

## 실행 방법

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
mkdir .secrets && echo '{"SECRET_KEY": "임의의 문자열"}' > .secrets/secret.json
python manage.py runserver
```

브라우저에서 http://127.0.0.1:8000/ 에 접속합니다. 스크랩에는 Chrome이 필요합니다.

## 주요 기능

- 키워드로 We Work Remotely, Indeed의 채용공고 스크랩
- 입력한 키워드를 `localStorage`에 저장해 재접속 시 자동 입력
- 홈 화면의 아이콘을 눌러 자주 쓰는 키워드로 바로 검색
- 스크랩과 화면 렌더링 중 로딩 표시
- 공고 URL에 한 번 더 접근해 기업 로고 이미지를 함께 표시
- Selenium으로 스크랩 속도 개선
- 스크랩 결과를 CSV 파일로 다운로드

## 화면

![조회 화면](static/references/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-03-03%20%EC%98%A4%ED%9B%84%207.40.00.png)

## 문서

- [개발 기록 (1~3차 구현)](docs/development-log.md) — 단계별 기능, 화면, 개선 사항
- [문제 해결 기록](docs/troubleshooting.md) — 개발 중 만난 문제 7건과 해결 과정 (봇 차단, 속도 개선 등)
- [사용 패키지](docs/packages.md) — 스크랩 대상 사이트와 패키지·라이브러리 설명
