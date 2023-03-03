'use strict'
const inputBox = document.querySelector('#keyword')

function storageSet(){
    /* home 화면에서 입력한 검색 키워드(keyword) 셋팅 */
    localStorage.setItem('keyword', inputBox.value)
    
    /* input에서 입력 시 입력한 문구를 유지하기 위해 localStorage 저장 */
    inputBox.addEventListener('keyup', (e)=>{
        let id = inputBox.id
        let val = inputBox.value
    
        localStorage.setItem(id, val)
    })
}

function focusSet() {
    let len = inputBox.value.length

    // input 포커스(포커싱 위치 제일 뒤로)
    inputBox.focus()
    inputBox.setSelectionRange(len, len)
}

function initial(){
    focusSet()   // input 포커싱
    storageSet() // input 입력 시 storage 저장 이벤트
}

export {
    initial
};