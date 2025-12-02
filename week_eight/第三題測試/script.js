"use strict";

const getData = async function () {
  let url = "http://127.0.0.1:8000/";
  const res = await fetch(url);
  const data = await res.json();
  console.log(data);
};

getData();
