"use strict";

const getData = async function () {
  let url = "http://127.0.0.1:8000/";
  const res = await fetch(url);

  const data = await res.json();
  console.log(data);
};

getData();

const outsideContent = document.querySelector(".content__div--outside");

const getContent = async function () {
  let url = "http://127.0.0.1:8000/content";
  const res = await fetch(url);
  const data = await res.json();
  console.log(data);

  for (const i of data) {
    const insideContent = document.createElement("div");
    insideContent.setAttribute("class", "content__div--inside");
    outsideContent.appendChild(insideContent);

    const rightContent = document.createElement("p");
    rightContent.setAttribute("class", "content__p--right");
    rightContent.textContent = i[1];
    const leftContent = document.createElement("p");
    leftContent.setAttribute("class", "content__p--left");
    leftContent.textContent = i[0];
    insideContent.appendChild(leftContent);
    insideContent.appendChild(rightContent);
  }
};

// getContent();
