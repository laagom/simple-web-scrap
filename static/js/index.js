import {initial} from './common.js';

'use strict'
async function search_keyword(){
    /* 검색(search)버튼 클릭 시 검색 키워드 채용공고 내용 스크랩 */
    const keyword = document.querySelector('#keyword').value    // 검색 키워드
    const grids = document.querySelectorAll('.grid') 

    if(keyword != ''){
        const response = await fetch(`/scrap?keyword=`+keyword)
        const results = await response.json()
        // console.log(grids)
        removeElements(grids)  // 렌더링 영역 초기화
        results.map((res)=>{
            render_content(res['list'], res['site'])
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

function removeElements(args) {
    /* 요소 제거 함수 */
    if(args.length != 0){
        args.forEach((e)=>{
            e.remove()
        })
    }
}

function render_content(result, site){
    const container = document.querySelector('.container')

    result.map((e, i)=>{

        const grid_div = document.createElement('div')
        grid_div.className = 'grid'
        container.appendChild(grid_div)

        const time_div = document.createElement('div')
        time_div.className = 'searched_item'
        grid_div.appendChild(time_div)

        const item_img = document.createElement('img')
        item_img.className = 'col-md-2 col-sm-1 searched_logo'
        time_div.appendChild(item_img)

        const detail_div = document.createElement('div')
        detail_div.className = 'col-md-6 col-sm-8 searched_detail'
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
        site_img.className = 'col-md-2 searched_source'
        site_img.src = site == 'Indeed'? '/static/assets/logo/idd.png' : '/static/assets/logo/wwr.jpeg'
        time_div.appendChild(site_img)

        const apply_div = document.createElement('div')
        apply_div.className = 'col-md-2 col-sm-2 searched_apply'
        time_div.appendChild(apply_div)

        const apply_a = document.createElement('a')
        apply_a.className = 'btn btn-primary'
        apply_a.href = e.url
        apply_a.setAttribute('role', 'button')
        apply_a.setAttribute('target', '_blank')
        apply_a.innerText = 'Apply'
        apply_div.appendChild(apply_a)
    })
}

const btnSearch = document.querySelector('#searchEmploy')
btnSearch.addEventListener('click', ()=>search_keyword())

const inputText =  document.querySelector('#keyword')
inputText.addEventListener('keypress', (event)=>enter_search(event))

// initial()로 초기 셋팅 후 search_keyword()로 자동 검색
initial()
search_keyword()