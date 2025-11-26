"use strict";
const signUpName = document.getElementById("regist_user_name");
const signEmail = document.getElementById("regist_email");
const signPassword = document.getElementById("regist_password");
const butt = document.getElementById("butt");
const formSign = document.getElementById("regist_form");

const button_send = function (event) {
  event.preventDefault();
  if (
    signUpName.value.trim() === "" ||
    signEmail.value.trim() === "" ||
    signPassword.value.trim() === ""
  ) {
    alert("請填入姓名、電子郵件和密碼");
  } else {
    formSign.submit();
  }
};

butt.addEventListener("click", button_send);

const loginEmail = document.getElementById("email");
const loginPassword = document.getElementById("password");
const loginButton = document.getElementById("buttt");
const formLogin = document.getElementById("form");

const login_send = function (event) {
  event.preventDefault();
  if (loginEmail.value.trim() === "" || loginPassword.value.trim() === "") {
    alert("請填入電子郵件和密碼");
  } else {
    formLogin.submit();
  }
};

loginButton.addEventListener("click", login_send);
