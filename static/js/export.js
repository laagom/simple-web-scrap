let content     = document.querySelector('#keyword')
const btnExport = document.querySelector('#exportExcel')

btnExport.addEventListener('click',()=>{
    let keyword = content.value
    if (keyword != ''){
        const response = fetch(`/export/excel?keyword=${keyword}`)
    }else{
        alert('검색어를 입력해 주세요.')
    }
})
