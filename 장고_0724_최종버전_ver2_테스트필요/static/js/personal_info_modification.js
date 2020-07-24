function checkValidate2() {
    if (!checkChangePw(modify.password.value, modify.con_chpw.value)) {
        return false;
    } else if (!checkChangeMobile(modify.change_mobile.value)) {
        return false;
    } else if (!checkRePosition()) {
        return false;
    }
        return true, alert("회원정보 수정이 완료되었습니다!")
}

function checkExistData(value, dataName) { //공란 항목 체크
    if (value == "") {
        alert(dataName + " 입력해주세요!");
        return false;
    }
    return true;
}

function checkUserId(username) { //아이디 칸 입력 여부 확인하기
    if (!checkExistData(username, "'이메일'을"))
        return false;

    var usernameRegExp = /^[A-Za-z0-9_]+[A-Za-z0-9]*[@]{1}[k]{1}[o]{1}[r]{1}[e]{1}[a]{1}[.]{1}[a]{1}[c]{1}[.]{1}[k]{1}[r]{1}$/; // 이메일 유효성 확인 정규식
    if (!usernameRegExp.test(username)) {
      alert("이메일 형식이 올바르지 않습니다!");
      sign.username.value = "";
      sign.username.focus();
      return false;
    }
    return true; //확인이 완료되었을 때
}

function checkChangePw(password, con_chpw) { //비밀번호 및 비밀번호 확인 칸 입력 여부 확인하기
    if (!checkExistData(password, "'변경 비밀번호'를"))
        return false;
    if (!checkExistData(con_chpw, "'변경 비밀번호 확인'을"))
        return false;

    var chpwRegExp = /^[a-zA-z0-9]{4,12}$/; //비밀번호 유효성 검사 정규식
    if (!chpwRegExp.test(password)) {
        alert("비밀번호는 영문 대소문자와 숫자를 이용하여 4~12자리로 입력해야합니다!");
        sign.password.value = "";
        sign.password.focus();
        return false;
    }
    if (password != con_chpw) { // 비밀번호와 비밀번호 일치 여부 확인하기
        alert("비밀번호가 일치하지 않습니다.");
        sign.password.value = "";
        sign.con_chpw.value = "";
        sign.con_chpw.focus();
        return false;
    }
    return true;
}

function checkChangeMobile(change_mobile) {
    if (!checkExistData(change_mobile, "'변경된 휴대폰 번호'를"))
        return false;

    var chmobileRegExp = /^\d{3}-\d{3,4}-\d{4}$/; // 이메일 유효성 확인 정규식
    if (!chmobileRegExp.test(change_mobile)) {
      alert("휴대폰 번호 형식이 올바르지 않습니다!");
      sign.change_mobile.value = "";
      sign.change_mobile.focus();
      return false;
    }
    return true;
}

function checkRePosition() { // 관심분야 1개 이상 체크여부 확인하기
    var checkedRePosition = document.getElementsByName("re_position");

    for (var i = 0; i < checkedRePosition.length; i++) { //체크된 값이 하나라도 있을경우 바로 true
        if (checkedRePosition[i].checked == true) {
            return true;
        }
    }
    alert("선호 포지션을 1개 이상 체크해주세요!");
    return false;
}
