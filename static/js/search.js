'use strict'

async function search_keyword(){
    const keyword = document.querySelector('#keyword').value    // 검색 키워드
    if (keyword != ''){
        const response = await fetch(`/scrap/wwr?keyword=`+keyword)
        const result   = await response.json()
        let content  = document.querySelector('#content')

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
    result.map((e)=>{   
            content.append(JSON.stringify(e))
        })
}

const btnSearch = document.querySelector('#btnSearch')
btnSearch.addEventListener('click', search_keyword)