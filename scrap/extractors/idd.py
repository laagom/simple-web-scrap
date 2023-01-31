from requests import get
from bs4 import BeautifulSoup
from scrap.decorator.browser_decorator import connection_idd_decorator

def get_page_count(keyword, browser):

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


@connection_idd_decorator
def jobs_idd(keyword, **kwards):
    # 페이징 페이지 수
    pages = get_page_count(keyword, kwards["browser"])

    soup     = BeautifulSoup(kwards["browser"].page_source, "html.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs     = job_list.find_all('li', recursive=False)

    results = []

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





