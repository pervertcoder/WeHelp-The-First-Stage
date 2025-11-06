"use strict";

const agree = document.getElementById("agree");
const butt = document.getElementById("butt");
const form = document.querySelector("#form");

const clickSent = function (event) {
  event.preventDefault();
  if (!agree.checked) {
    alert("請勾選同意條款");
  } else {
    form.submit();
  }
};
butt.addEventListener("click", clickSent);

const buttonHotel = document.querySelector("#button");
const hotelForm = document.querySelector("#hotelForm");
const order = document.querySelector("#order");

const clickHotelSent = function (event) {
  event.preventDefault();
  window.location.href = `/hotel/${order.value}`;
};

buttonHotel.addEventListener("click", clickHotelSent);
