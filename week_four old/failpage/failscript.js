"use strict";

const errorMassage = document.querySelector(".error-message");
const queryString = window.location.search;
const params = new URLSearchParams(queryString);
const msg = params.get("msg");
errorMassage.textContent = msg;
