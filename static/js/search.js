'use strict'
const content = document.querySelector('#content')

function search_keyword(){
    const keyword = document.querySelector('#keyword').value    // 검색 키워드
    if (keyword != ''){
        const idd = fetch(`/scrap/idd?keyword=`+keyword).then(response => response.json())         
        const wwr = fetch(`/scrap/wwr?keyword=`+keyword).then(response => response.json())

        Promise.all([idd, wwr])
            .then(results=>{
                empty_content(content)  // 렌더링 영역 초기화
                
                results.map((result)=>{
                    render_content(result['list'], result['site'])
                })
            })
    }else{
        alert('검색어를 입력해 주세요.')
    }
}

function empty_content(element){
    element.childNodes.forEach((e, i)=>{
        element.removeChild(element.childNodes[i])
    })
}

function render_content(result, site){
    const thead = document.querySelector('#headContent')
    const tbody = document.querySelector('#bodyContent')

    // site 제목 렌더링
    const site_tr = document.createElement('tr')
    tbody.appendChild(site_tr)

    const site_td = document.createElement('td')
    console.log(thead.childNodes)
    site_td.colSpan = thead.querySelector('tr').querySelectorAll('th').length
    site_td.innerText = site
    site_td.className = 'center bg-black color-white'
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
        url_a.title = e.url
        url_a.innerText = e.url
        url_a.setAttribute('title', e.url)
        url_a.setAttribute('target', '_blank')
    })
}

const btnSearch = document.querySelector('#searchEmploy')

btnSearch.addEventListener('click', ()=>search_keyword())
