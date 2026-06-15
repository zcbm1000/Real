const SIGN_UP_VIEWS         = 1;
const SIGN_IN_VIEWS         = 2;
const SIGN_OUT_VIEWS        = 3;
const DIARTY_WRITE_VIEWS    = 4;
const DIARTY_LIST_VIEWS     = 5;

signUpWrap = '';
signInWrap = '';
writeWrap = '';
listWrap = '';

function initViews() {
    console.log('initViews() CALLED!!')
    
    signUpWrap =  document.querySelector('div.sign_up_wrap');
    signInWrap =  document.querySelector('div.sign_in_wrap');
    writeWrap =  document.querySelector('div.write_wrap');
    listWrap =  document.querySelector('div.list_wrap');

}

// 사용자 원하는 뷰를 보이게 하는 함수
function showSelectedView(viewNo){
    console.log('showSelectedView() CALLED')
    switch(viewNo) {
        case SIGN_UP_VIEWS:
            // 회원가입 화면
            signUpWrap.style.display = 'block';
            signInWrap.style.display = 'none';
            writeWrap.style.display = 'none';
            listWrap.style.display = 'none';
            break;

        case SIGN_IN_VIEWS:
            // 로그인 화면
            signUpWrap.style.display = 'none';
            signInWrap.style.display = 'block';
            writeWrap.style.display = 'none';
            listWrap.style.display = 'none';
            break;

        case SIGN_OUT_VIEWS:
            // 로그인 아웃

            break;

        case DIARTY_WRITE_VIEWS:
            // 일기 작성 화면
            signUpWrap.style.display = 'none';
            signInWrap.style.display = 'none';
            writeWrap.style.display = 'block';
            listWrap.style.display = 'none';
            break;

        case DIARTY_LIST_VIEWS:
            // 일기 리스트 화면
            signUpWrap.style.display = 'none';
            signInWrap.style.display = 'none';
            writeWrap.style.display = 'none';
            listWrap.style.display = 'block';
            break;
    }

}