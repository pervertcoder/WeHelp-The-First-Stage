"use strict";
const path = window.location.pathname;
const parts = path.split("/");
const hotelnum = parseInt(parts[parts.length - 1]);
// console.log(hotelnum);

const hotelinfor = document.querySelector(".hotelinfor");
// hotelinfor.textContent = "";
fetch(`/hotel_data/${hotelnum}`)
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
    // hotelinfor.textContent = data.join("、");
    if (data["error"]) {
      hotelinfor.textContent = "查詢不到相關資料";
    } else {
      hotelinfor.textContent = data.join("、");
    }
  });
