'use strict'
const btnExport = document.querySelector('#export')

btnExport.addEventListener('click', ()=>document_export())

function document_export(){
    let keyword = localStorage.getItem('keyword')

    const response = fetch(`/export?keyword=${keyword}`)
}