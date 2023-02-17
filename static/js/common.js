const inputBox = document.querySelector('#keyword')

function storageSet(){
    /* input에서 입력 시 입력한 문구를 유지하기 위해 localStorage 저장 */
    inputBox.addEventListener('keyup', (e)=>{
        let id = inputBox.id
        let val = inputBox.value
    
        localStorage.setItem(id, val)
    })
}

function setInputVal(){
    /* 이전에 입력한 localStorage에 저장된 문구를 input에 셋팅 */
    const inputVal = localStorage.getItem(inputBox.id)
    if(inputVal){
        inputBox.value = inputVal
    }
}

function initial(){
    inputBox.focus()    // input 포커스
    setInputVal()       // 이전에 입력했던 input 값 넣기
    storageSet()        // input 입력 시 storage 저장 이벤트
}

initial()  // 초기 셋팅 