// "HTML(밑그림) 다 로딩될 때까지 기다렸다가, 그다음 자바스크립트 실행하는 명령어
// 그림도 없는데 자바스크립트가 먼저 나대다가 에러(Error) 나는 것을 막아주는 안전장치
//                  리스너                    콜백함수/ 핸들러
document.addEventListener('DOMContentLoaded', function(){
    console.log('DOCUMENT.READY')

    init();
});

function init() {
    console.log('init() CALLED!!')
    initViews();
    addEvents();
}

function addEvents() {
    console.log('addEvents() CALLED!!')

    let signUpMenuBtn = document.querySelector('div.menu_wrap a.sign_up');
    signUpMenuBtn.addEventListener('click', function() {
        console.log('signUpMenuBtn CALLED!!')
        
        showSelectedView(SIGN_UP_VIEWS);
    });

    let signInMenuBtn = document.querySelector('div.menu_wrap a.sign_in');
    signInMenuBtn.addEventListener('click', function() {
        console.log('signInMenuBtn CALLED!!')

        showSelectedView(SIGN_IN_VIEWS);
    });

    let signOutMenuBtn = document.querySelector('div.menu_wrap a.sign_out');
    signOutMenuBtn.addEventListener('click', function() {
        console.log('signOutMenuBtn CALLED!!')

        showSelectedView(SIGN_OUT_VIEWS);
    });
    
    let writeMenuBtn = document.querySelector('div.menu_wrap a.write');
    writeMenuBtn.addEventListener('click', function() {
        console.log('writeMenuBtn CALLED!!')

        showSelectedView(DIARTY_WRITE_VIEWS);
    });

    let listMenuBtn = document.querySelector('div.menu_wrap a.list');
    listMenuBtn.addEventListener('click', function() {
        console.log('listMenuBtn CALLED!!')

        showSelectedView(DIARTY_LIST_VIEWS);
    });

    let signUpBtn =  document.querySelector('div.sign_up_wrap input[type="button"]')
    signUpBtn.addEventListener('click', function(){
        console.log('signUpBtn CALLED!!');

        let u_id = document.querySelector('div.sign_up_wrap input[name="u_id"]').value;
        let u_pw = document.querySelector('div.sign_up_wrap input[name="u_pw"]').value;
        let u_mail = document.querySelector('div.sign_up_wrap input[name="u_mail"]').value;

        addMember(u_id, u_pw, u_mail);

        alert('회원가입 축하드립니다!!');

        document.querySelector('div.sign_up_wrap input[name="u_id"]').value = '';
        document.querySelector('div.sign_up_wrap input[name="u_pw"]').value = '';
        document.querySelector('div.sign_up_wrap input[name="u_mail"]').value = '';

    });
}