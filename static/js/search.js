'use strict'
const content = document.querySelector('#content')

async function search_keyword(type){
    const keyword = document.querySelector('#keyword').value    // 검색 키워드
    if (keyword != ''){
        const response = await fetch(`/scrap/${type}?keyword=`+keyword)
        const result   = await response.json()

        empty_content(content)  // 렌더링 영역 초기화
        render_content(result)  // 결과 값 렌더링
    }else{
        alert('검색어를 입력해 주세요.')
    }
}

function empty_content(element){
    element.childNodes.forEach((e, i)=>{
        element.removeChild(element.childNodes[i])
    })
}

function render_content(result){
    const tbody = document.querySelector('#bodyContent')

    result.map((e, i)=>{   
        const tr = document.createElement('tr')
        tbody.appendChild(tr)

        const num_td = document.createElement('td')
        tr.appendChild(num_td)
        num_td.className = 'center'
        num_td.innerText = i

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
    })
}

const btnIdd = document.querySelector('#searchIdd')
const btnWwr = document.querySelector('#searchWwr')

btnIdd.addEventListener('click', ()=>search_keyword('idd'))
btnWwr.addEventListener('click', ()=>search_keyword('wwr'))