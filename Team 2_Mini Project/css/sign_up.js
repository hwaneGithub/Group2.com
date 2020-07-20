var finish_flag = 0;


function start_alert(){
  alert("KUMATCH는 학교 구성원들로만 이루어진 커뮤니티 입니다.")
}


function pw_check() {   //비밀번호, 비밀번호 확인 비교 함수
  var pw = document.getElementById("pw").value;
  var repw = document.getElementById("repw").value;

  if (pw == "" || repw == "") //두 입력칸 중 비어있는 것이 존재할 때
  {
    alert("비밀번호를 입력해주세요."); //메시지 출력

  } else if (pw != repw) {
    alert("비밀번호가 일치하지 않습니다."); //일치 메시지 출력
  } else {
    alert("비밀번호가 일치합니다."); //일치 메시지 출력
    finish_flag = 1;   //전체 검사 flag 1로 set
  }

}
