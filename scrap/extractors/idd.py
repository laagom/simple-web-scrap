from requests import get
from bs4 import BeautifulSoup

def idd_jobs(keyword):
    # indeed 사이트 검색 url 
    base_url = 'https://kr.indeed.com/jobs?q='

    # 요청 후 응답 받기
    response = get(f"{base_url}{keyword}")

    # 응답 상태 코드에 따른 분기 처리
    if response.status_code != 200:
        print("Cant request pagge")
    else:
        result = []

        soup = BeautifulSoup(response.text, "html.parse")
        jobs_list = soup.find_all('ul', class_='jobsearch-ResultsList')
        
        # 현재 depth의 li요소만 찾기 위해 recursive=False
        jobs = jobs_list.find_all('li', recursive=False)
        
        for job in jobs:
            print(job)
            print('--------------------')

        return response.text


