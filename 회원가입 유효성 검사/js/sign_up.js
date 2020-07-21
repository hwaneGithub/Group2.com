function checkValidate() {
    if (!checkUserId(sign.username.value)) {
        return false;
    } else if (!checkPassword(sign.username.value, sign.password.value, sign.con_pw.value)) {
        return false;
    } else if (!checkLastName(sign.last_name.value)) {
        return false;
    } else if (!checkFirstName(sign.first_name.value)) {
        return false;
    } else if (!checkMobileNum(sign.mobile_num.value)) {
        return false;
    /* } else if (!checkPosition()) {
        return false; */
    } else if (!checkIdNum(sign.id_num.value)) {
        return false;
    }
        return true;
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

    /* var userIdRegExp = /^[a-zA-z0-9]{4,12}$/; //아이디 유효성 검사 정규식
    if (!userIdRegExp.test(userId)) {
        alert("아이디는 영문 대소문자와 숫자를 이용하여 4~12자리로 입력해야합니다!");
        sign.userId.value = "";
        sign.userId.focus();
        return false;
    } */
    return true; //확인이 완료되었을 때
}

function checkPassword(username, password, con_pw) { //비밀번호 및 비밀번호 확인 칸 입력 여부 확인하기
    if (!checkExistData(password, "'비밀번호'를"))
        return false;
    if (!checkExistData(con_pw, "'비밀번호 확인'을"))
        return false;

    var pwRegExp = /^[a-zA-z0-9]{4,12}$/; //비밀번호 유효성 검사 정규식
    if (!pwRegExp.test(pw)) {
        alert("비밀번호는 영문 대소문자와 숫자를 이용하여 4~12자리로 입력해야합니다!");
        sign.password.value = "";
        sign.password.focus();
        return false;
    }
    if (password != con_pw) { // 비밀번호와 비밀번호 일치 여부 확인하기
        alert("비밀번호가 일치하지 않습니다.");
        sign.password.value = "";
        sign.con_pw.value = "";
        sign.con_pw.focus();
        return false;
    }

    if (username == password) { // 아이디와 비밀번호 동일 여부 확인하기
        alert("아이디와 비밀번호는 동일할 수 없습니다!");
        sign.password.value = "";
        sign.con_pw.value = "";
        sign.con_pw.focus();
        return false;
    }
    return true; //확인이 완료되었을 때
}

function checkLastName(last_name) { // 이름 칸 입력 여부 확인하기
    if (!checkExistData(last_name, "'성'을"))
        return false;

        var last_nameRegExp = /^[가-힣]{1,3}$/; // 이름 유효성 확인 정규식
    if (!last_nameRegExp.test(last_name)) {
        alert("올바르지 않은 성 형식 입니다.");
        return false;
    }
    return true; //확인이 완료되었을 때
}

function checkFirstName(first_name) { // 이름 칸 입력 여부 확인하기
    if (!checkExistData(first_name, "'이름'을"))
        return false;

        var first_nameRegExp = /^[가-힣]{1,5}$/; // 이름 유효성 확인 정규식
    if (!first_nameRegExp.test(first_name)) {
        alert("올바르지 않은 이름 형식 입니다.");
        return false;
    }
    return true; //확인이 완료되었을 때
}

function checkMobileNum(mobile_num) {
    if (!checkExistData(mobile_num, "'휴대폰 번호'를"))
        return false;

        var mobileRegExp = /^\d{3}-\d{3,4}-\d{4}$/;; // 이메일 유효성 확인 정규식
    if (!mobileRegExp.test(mobile_num)) {
      alert("휴대폰 번호 형식이 올바르지 않습니다!");
      sign.mobile_num.value = "";
      sign.mobile_num.focus();
      return false;
    }
}

/* function checkPosition() { // 관심분야 1개 이상 체크여부 확인하기
    var checkedPosition = document.getElementsByName("position");

    for (var i = 0; i < checkedPosition.length; i++) { //체크된 값이 하나라도 있을경우 바로 true
        if (checkedPosition[i].checked == true) {
            return true;
        }
    }
    alert("선호 포지션을 체크해주세요!");
    return false;
} */

function checkIdNum(id_num) {
    if (!checkExistData(id_num, "'휴대폰 번호'를"))
        return false;

        var idnumRegExp = /^[0-9]{10}$/;; // 이메일 유효성 확인 정규식
    if (!idnumRegExp.test(id_num)) {
      alert("학번 형식이 올바르지 않습니다!");
      sign.id_num.value = "";
      sign.id_num.focus();
      return false;
    }
}
