function modifyForm() {
    console.log('modifyForm() CALLED!!');

    let form = document.modify_form;

    let mPw = form.mPw.value.trim();
    let mMail = form.mMail.value.trim();
    let mPhone = form.mPhone.value.trim();



    if (mPw === '') {
        alert('Please input member PW!!');
        form.mPw.focus();

    } else if (mMail === '') {
        alert('Please input member MAIL!!');
        form.mMail.focus();

    } else if (mPhone === '') {
        alert('Please input member PHONE!!');
        form.mPhone.focus();

    } else {
        form.submit();
        
    }

}