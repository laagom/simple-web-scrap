from requests import get
from bs4 import BeautifulSoup

def jobs_wwr(keyword):
    
    # we work remotely 사이트 검색 url
    base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="

    # 요청 후 응답 받기
    response = get(f"{base_url}{keyword}")

    # 응답 상태 코드에 따른 분기 처리
    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []

        # html 파싱
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")

        for job_section in jobs:
            job_posts = job_section.find_all('li')

            # 마지막 view-all을 클래스를 가진 li 제거
            job_posts.pop(-1)

            for post in job_posts:
                anchors = post.find_all('a')
                anchor  = anchors[1]
                title   = anchor.find('span', class_='title')
                link    = f'https://weworkremotely.com{anchor["href"]}'

                # company 키워드로 탐색한 3개의 요소를 각각 할당
                company, kind, region = anchor.find_all('span', class_='company')

                job_data = {
                    'company' : company.string,
                    'region'  : region.string,
                    'position': title.string,
                    # 'kind'    : kind.string,
                    'url'     : link,
                }
                results.append(job_data)
                
    return results