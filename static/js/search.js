'use strict'
const content = document.querySelector('#content')

async function search_keyword(){
    /* 검색(search)버튼 클릭 시 검색 키워드 채용공고 내용 스크랩 */
    const keyword = document.querySelector('#keyword').value    // 검색 키워드
    if(keyword != ''){
        const response = await fetch(`/scrap?keyword=`+keyword)
        const results = await response.json()
    
        empty_content(content.querySelector('tbody'))  // 렌더링 영역 초기화
        results.map((res)=>{
            render_content(res['list'], res['site'])
        })
    }
}

function enter_search(event){
    /* input에서 enter시 검색(search) 트리거 */
    if(event.keyCode === 13){
        btnSearch.click()
    }
}

function empty_content(element){
    /* 요소 안의 내용을 모두 지우는 초기화 함수 */
    while(element.hasChildNodes()){
        element.removeChild(element.firstChild);
    }
}

function render_content(result, site){
    /* 스크랩한 공고 내용 렌더링 */
    const thead = document.querySelector('#headContent')
    const tbody = document.querySelector('#bodyContent')

    // site 제목 렌더링
    const site_tr = document.createElement('tr')
    tbody.appendChild(site_tr)

    const site_td = document.createElement('td')
    site_td.colSpan = thead.querySelector('tr').querySelectorAll('th').length
    site_td.innerText = site
    site_td.className = 'center bg-black color-white fs15'
    site_tr.appendChild(site_td)

    // site 스크랩 공고 렌더링
    result.map((e, i)=>{   
        const tr = document.createElement('tr')
        tbody.appendChild(tr)

        const num_td = document.createElement('td')
        tr.appendChild(num_td)
        num_td.className = 'center'
        num_td.innerText = i+1

        const position_td = document.createElement('td')
        tr.appendChild(position_td)
        position_td.innerText = e.position
        position_td.setAttribute('title', e.position)

        const company_td = document.createElement('td')
        tr.appendChild(company_td)
        company_td.innerText = e.company
        company_td.setAttribute('title', e.company)

        const location_td = document.createElement('td')
        tr.appendChild(location_td)
        location_td.innerText = e.location
        location_td.setAttribute('title', e.location)

        const url_td = document.createElement('td')
        tr.appendChild(url_td)

        const url_a = document.createElement('a')
        url_td.appendChild(url_a)
        url_a.href = e.url
        url_a.title = 'Apply Now'
        url_a.innerText = 'Apply Now'
        url_a.setAttribute('title', e.url)
        url_a.setAttribute('target', '_blank')
    })
}

const btnSearch = document.querySelector('#searchEmploy')
btnSearch.addEventListener('click', ()=>search_keyword())

const inputText =  document.querySelector('#keyword')
inputText.addEventListener('keypress', (event)=>enter_search(event))

search_keyword()