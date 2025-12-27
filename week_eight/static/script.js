"use strict";

const getData = async function () {
  let url = "http://127.0.0.1:8000/";
  const res = await fetch(url);
  const data1 = await res.json();
  console.log(data1);
};

// getData();

const outsideContent = document.querySelector(".content__div--outside");

const getContent = async function () {
  let url = "http://127.0.0.1:8000/content";
  const res = await fetch(url);
  const data = await res.json();
  // console.log(data);

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

const getContentV2 = async function () {
  let url = "http://127.0.0.1:8000/content";
  const res = await fetch(url);
  const data = await res.json();
  // console.log(data);
  let state = 0;

  for (let i = 0; i < data.length; i++) {
    const insideContent = document.createElement("div");
    insideContent.setAttribute("class", "content__div--inside");
    outsideContent.appendChild(insideContent);

    const insideContentP = document.createElement("p");
    insideContentP.setAttribute("class", "content__p--inside");
    insideContent.appendChild(insideContentP);
    insideContentP.dataset.id = i;
    insideContentP.textContent = data[i][0];

    const buttonD = document.createElement("div");
    buttonD.setAttribute("class", "btnD");
    insideContent.appendChild(buttonD);

    const switchBtn1 = document.createElement("button");
    switchBtn1.classList.add("btn1");
    buttonD.appendChild(switchBtn1);
    switchBtn1.textContent = "文言文";
    switchBtn1.addEventListener("click", () => {
      if (state === 1) {
        insideContentP.textContent = data[i][0];
        state = 0;
      }
    });

    const switchBtn2 = document.createElement("button");
    switchBtn2.classList.add("btn2");
    buttonD.appendChild(switchBtn2);
    switchBtn2.textContent = "白話文";
    switchBtn2.addEventListener("click", () => {
      if (state === 0) {
        insideContentP.textContent = data[i][1];
        state = 1;
      }
    });
  }
};

let stat = 0;
getContent();

const switchBt = document.getElementById("switch");
const stateP = document.querySelector(".stateP");

switchBt.addEventListener("click", () => {
  outsideContent.innerHTML = "";
  if (stat === 0) {
    getContentV2();
    stateP.textContent = "分離模式";
    stat = 1;
    console.log("切換成分離模式");
  } else {
    getContent();
    stateP.textContent = "全覽模式";
    stat = 0;
    console.log("切換成全覽模式");
  }
});
