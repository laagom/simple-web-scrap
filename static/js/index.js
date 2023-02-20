import {initial} from './common.js';

'use strict'
const content = document.querySelector('#content')

async function search_keyword(){
    /* 검색(search)버튼 클릭 시 검색 키워드 채용공고 내용 스크랩 */
    const keyword = document.querySelector('#keyword').value    // 검색 키워드
    if(keyword != ''){
        const response = await fetch(`/scrap?keyword=`+keyword)
        const results = await response.json()
    
        // empty_content(content)  // 렌더링 영역 초기화
        results.map((res)=>{
            // render_content(res['list'], res['site'])
            render_contents(res['list'], res['site'])
        })

        // keyword가 변경때마다 파일출력 url 변경        
        const anchor = document.querySelector('#export')
        anchor.href = `/export?keyword=${keyword}`
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

function render_contents(result, site){
    const container = document.querySelector('.container')

    result.map((e, i)=>{

        const grid_div = document.createElement('div')
        grid_div.className = 'grid'
        container.appendChild(grid_div)

        const time_div = document.createElement('div')
        time_div.className = 'searched__item'
        grid_div.appendChild(time_div)

        const item_img = document.createElement('img')
        item_img.className = 'col-md-2 col-sm-1 searched__logo'
        time_div.appendChild(item_img)

        const detail_div = document.createElement('div')
        detail_div.className = 'col-md-6 col-sm-8 searched__detail'
        time_div.appendChild(detail_div)

        const detail_company = document.createElement('h4')
        detail_company.innerText = e.company
        detail_div.appendChild(detail_company)

        const detail_position = document.createElement('div')
        detail_position.innerText = e.position
        detail_div.appendChild(detail_position)

        const detail_site = document.createElement('div')
        detail_site.innerText = site
        detail_div.appendChild(detail_site)

        const site_img = document.createElement('img')
        site_img.className = 'col-md-2 searched__source'
        site_img.src = '/static/assets/logo/python.png'
        time_div.appendChild(site_img)
    })

    // <div class="grid">
    //     <div class="row searched__item">

    //         <img class="col-md-2 col-sm-1 searched__logo"
    //             src="https://remoteok.com/cdn-cgi/image/format=auto,fit=contain,width=100,height=100,quality=50/https://remoteok.com/assets/img/jobs/771700ecb3a12f9fe4da669bf6a0f1b21676790981.png?1676790981" />

    //         <div class="col-md-6 col-sm-8 searched__detail">
    //             <h4>NOBI</h4>
    //             <div>Software Engineer</div>
    //             <div>Worldwide</div>
    //         </div>

    //         <img class="col-md-2 searched__source" src="/static/images/rok_logo.png" />

    //         <div class="col-md-2 col-sm-2 searched__apply">
    //             <a class="btn btn-primary"
    //                 href="https://remoteok.com/remote-jobs/remote-software-engineer-nobi-196804"
    //                 role="button" target="_blank">Apply</a>
    //         </div>
    //     </div>
    // </div>
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
        url_a.innerText = 'Apply Now ➤'
        url_a.setAttribute('title', e.url)
        url_a.setAttribute('target', '_blank')
    })
}

const btnSearch = document.querySelector('#searchEmploy')
btnSearch.addEventListener('click', ()=>search_keyword())

const inputText =  document.querySelector('#keyword')
inputText.addEventListener('keypress', (event)=>enter_search(event))

// initial()로 초기 셋팅 후 search_keyword()로 자동 검색
initial()
search_keyword()