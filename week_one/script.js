const hamburger = document.getElementById("hamburger");
const menu = document.getElementById("menu");
const icon = document.getElementById("hamburger-icon");

let isMenuOpen = false;

hamburger.addEventListener("click", () => {
  isMenuOpen = !isMenuOpen;
  menu.classList.toggle("show");

  if (isMenuOpen) {
    icon.src = "image/close.png";
    icon.alt = "關閉選單";
  } else {
    icon.src = "image/4781852_burger_line_list_menu_nav_icon.png";
    icon.alt = "開啟選單";
  }
});

const rowStringDestruction = function (picsStr) {
  if (!picsStr) return []; // 空值保護

  // 把整個字串拆成段
  var segments = picsStr.split("/");

  var result = [];
  var currentPath = "";

  for (var i = 0; i < segments.length; i++) {
    if (!segments[i]) continue; // 忽略空字串

    currentPath += "/" + segments[i];

    // 如果段尾是圖片檔案，存起來，並清空 currentPath
    if (segments[i].match(/\.(jpg|jpeg|png)$/i)) {
      result.push(currentPath);
      currentPath = "";
    }
  }

  return result;
};

async function getData() {
  // 文字資源
  const res = await fetch("https://cwpeng.github.io/test/assignment-3-1");
  const data = await res.json();
  console.log(data);

  const rows = data.rows;

  const wordElement = document.querySelector(".word p");
  wordElement.textContent = rows[0]["sname"];

  const wordOneElement = document.querySelector(".word_1 p");
  wordOneElement.textContent = rows[0]["sname"];

  const word2Element = document.querySelector(".word2 p");
  word2Element.textContent = rows[1]["sname"];

  const wordtwoElement = document.querySelector(".word_2 p");
  wordtwoElement.textContent = rows[1]["sname"];

  const word3Element = document.querySelector(".word3 p");
  word3Element.textContent = rows[2]["sname"];

  const wordthreeElement = document.querySelector(".word_3 p");
  wordthreeElement.textContent = rows[2]["sname"];

  const transparentBarElement1 = document.querySelector(".transparent_bar1 p");
  transparentBarElement1.textContent = rows[3]["sname"];

  const transparentBarElement2 = document.querySelector(".transparent_bar2 p");
  transparentBarElement2.textContent = rows[4]["sname"];

  const transparentBarElement3 = document.querySelector(".transparent_bar3 p");
  transparentBarElement3.textContent = rows[5]["sname"];

  const transparentBarElement4 = document.querySelector(".transparent_bar4 p");
  transparentBarElement4.textContent = rows[6]["sname"];

  const transparentBarElement5 = document.querySelector(".transparent_bar5 p");
  transparentBarElement5.textContent = rows[7]["sname"];

  const transparentBarElement6 = document.querySelector(".transparent_bar6 p");
  transparentBarElement6.textContent = rows[8]["sname"];

  const transparentBarElement7 = document.querySelector(".transparent_bar7 p");
  transparentBarElement7.textContent = rows[9]["sname"];

  const transparentBarElement8 = document.querySelector(".transparent_bar8 p");
  transparentBarElement8.textContent = rows[10]["sname"];

  const transparentBarElement9 = document.querySelector(".transparent_bar9 p");
  transparentBarElement9.textContent = rows[11]["sname"];

  const transparentBarElement10 = document.querySelector(
    ".transparent_bar10 p"
  );
  transparentBarElement10.textContent = rows[12]["sname"];

  const oneRowTransparentBar1 = document.querySelector("#bar1 p");
  oneRowTransparentBar1.textContent = rows[3]["sname"];

  const oneRowTransparentBar2 = document.querySelector("#bar2 p");
  oneRowTransparentBar2.textContent = rows[4]["sname"];

  const oneRowTransparentBar3 = document.querySelector("#bar3 p");
  oneRowTransparentBar3.textContent = rows[5]["sname"];

  const oneRowTransparentBar4 = document.querySelector("#bar4 p");
  oneRowTransparentBar4.textContent = rows[6]["sname"];

  const oneRowTransparentBar5 = document.querySelector("#bar5 p");
  oneRowTransparentBar5.textContent = rows[7]["sname"];

  const oneRowTransparentBar6 = document.querySelector("#bar6 p");
  oneRowTransparentBar6.textContent = rows[8]["sname"];

  const oneRowTransparentBar7 = document.querySelector("#bar7 p");
  oneRowTransparentBar7.textContent = rows[9]["sname"];

  const oneRowTransparentBar8 = document.querySelector("#bar8 p");
  oneRowTransparentBar8.textContent = rows[10]["sname"];

  const oneRowTransparentBar9 = document.querySelector("#bar9 p");
  oneRowTransparentBar9.textContent = rows[11]["sname"];

  const oneRowTransparentBar10 = document.querySelector("#bar10 p");
  oneRowTransparentBar10.textContent = rows[12]["sname"];

  const wordSmall1 = document.querySelector("#word_small1 p");
  wordSmall1.textContent = rows[0]["sname"];

  const wordSmall2 = document.querySelector("#word_small2 p");
  wordSmall2.textContent = rows[1]["sname"];

  const wordSmall3 = document.querySelector("#word_small3 p");
  wordSmall3.textContent = rows[2]["sname"];

  const wordsmall4 = document.querySelector(".oneR1");
  wordsmall4.textContent = rows[3]["sname"];

  const wordsmall5 = document.querySelector(".oneR2");
  wordsmall5.textContent = rows[4]["sname"];

  const wordsmall6 = document.querySelector(".oneR3");
  wordsmall6.textContent = rows[5]["sname"];

  const wordsmall7 = document.querySelector(".oneR4");
  wordsmall7.textContent = rows[6]["sname"];

  const wordsmall8 = document.querySelector(".oneR5");
  wordsmall8.textContent = rows[7]["sname"];

  const wordsmall9 = document.querySelector(".oneR6");
  wordsmall9.textContent = rows[8]["sname"];

  const wordsmall10 = document.querySelector(".oneR7");
  wordsmall10.textContent = rows[9]["sname"];

  const wordsmall11 = document.querySelector(".oneR8");
  wordsmall11.textContent = rows[10]["sname"];

  const wordsmall12 = document.querySelector(".oneR9");
  wordsmall12.textContent = rows[11]["sname"];

  const wordsmall13 = document.querySelector(".oneR10");
  wordsmall13.textContent = rows[12]["sname"];

  // 圖片資源

  const resImg = await fetch("https://cwpeng.github.io/test/assignment-3-2");
  const dataImg = await resImg.json();
  console.log(dataImg);

  const rowImg = dataImg.rows;

  const targetSerial = rows[0]["serial"];
  let inde1 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial;
  });
  const desktopPromotion1 = document.querySelector(".promotion1 img");
  desktopPromotion1.src =
    dataImg.host + rowStringDestruction(rowImg[inde1]["pics"])[0];

  const targetSerial1 = rows[1]["serial"];
  let inde2 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial1;
  });
  const desktopPromotion2 = document.querySelector(".promotion2 img");
  desktopPromotion2.src =
    dataImg.host + rowStringDestruction(rowImg[inde2]["pics"])[0];

  const targetSerial3 = rows[2]["serial"];
  let inde3 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial3;
  });
  const desktopPromotion3 = document.querySelector(".promotion3 img");
  desktopPromotion3.src =
    dataImg.host + rowStringDestruction(rowImg[inde3]["pics"])[0];

  const targetSerial4 = rows[3]["serial"];
  let inde4 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial4;
  });
  const desktopTitle1 = document.querySelector(".title1 img");
  desktopTitle1.src =
    dataImg.host + rowStringDestruction(rowImg[inde4]["pics"])[0];

  const targetSerial5 = rows[4]["serial"];
  let inde5 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial5;
  });
  const desktopTitle2 = document.querySelector(".title2 img");
  desktopTitle2.src =
    dataImg.host + rowStringDestruction(rowImg[inde5]["pics"])[0];

  const targetSerial6 = rows[5]["serial"];
  let inde6 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial6;
  });
  const desktopTitle3 = document.querySelector(".title3 img");
  desktopTitle3.src =
    dataImg.host + rowStringDestruction(rowImg[inde6]["pics"])[0];

  const targetSerial7 = rows[6]["serial"];
  let inde7 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial7;
  });
  const desktopTitle4 = document.querySelector(".title4 img");
  desktopTitle4.src =
    dataImg.host + rowStringDestruction(rowImg[inde7]["pics"])[0];

  const targetSerial8 = rows[7]["serial"];
  let inde8 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial8;
  });
  const desktopTitle5 = document.querySelector(".title5 img");
  desktopTitle5.src =
    dataImg.host + rowStringDestruction(rowImg[inde8]["pics"])[0];

  const targetSerial9 = rows[8]["serial"];
  let inde9 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial9;
  });
  const desktopTitle6 = document.querySelector(".title6 img");
  desktopTitle6.src =
    dataImg.host + rowStringDestruction(rowImg[inde9]["pics"])[0];

  const targetSerial10 = rows[9]["serial"];
  let inde10 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial10;
  });
  const desktopTitle7 = document.querySelector(".title7 img");
  desktopTitle7.src =
    dataImg.host + rowStringDestruction(rowImg[inde10]["pics"])[0];

  const targetSerial11 = rows[10]["serial"];
  let inde11 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial11;
  });
  const desktopTitle8 = document.querySelector(".title8 img");
  desktopTitle8.src =
    dataImg.host + rowStringDestruction(rowImg[inde11]["pics"])[0];

  const targetSerial12 = rows[11]["serial"];
  let inde12 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial12;
  });
  const desktopTitle9 = document.querySelector(".title9 img");
  desktopTitle9.src =
    dataImg.host + rowStringDestruction(rowImg[inde12]["pics"])[0];

  const targetSerial13 = rows[12]["serial"];
  let inde13 = rowImg.findIndex(function (item) {
    return item.serial === targetSerial13;
  });
  const desktopTitle10 = document.querySelector(".title10 img");
  desktopTitle10.src =
    dataImg.host + rowStringDestruction(rowImg[inde13]["pics"])[0];

  const RWDPromotion1 = document.querySelector(".image_1 img");
  RWDPromotion1.src =
    dataImg.host + rowStringDestruction(rowImg[inde1]["pics"])[0];

  const RWDPromotion2 = document.querySelector(".image_2 img");
  RWDPromotion2.src =
    dataImg.host + rowStringDestruction(rowImg[inde2]["pics"])[0];

  const RWDPromotion3 = document.querySelector(".image_3 img");
  RWDPromotion3.src =
    dataImg.host + rowStringDestruction(rowImg[inde3]["pics"])[0];

  const RWDTitle1 = document.querySelector("#RWD1 img");
  RWDTitle1.src = dataImg.host + rowStringDestruction(rowImg[inde4]["pics"])[0];

  const RWDTitle2 = document.querySelector("#RWD2 img");
  RWDTitle2.src = dataImg.host + rowStringDestruction(rowImg[inde5]["pics"])[0];

  const RWDTitle3 = document.querySelector("#RWD3 img");
  RWDTitle3.src = dataImg.host + rowStringDestruction(rowImg[inde6]["pics"])[0];

  const RWDTitle4 = document.querySelector("#RWD4 img");
  RWDTitle4.src = dataImg.host + rowStringDestruction(rowImg[inde7]["pics"])[0];

  const RWDTitle5 = document.querySelector("#RWD5 img");
  RWDTitle5.src = dataImg.host + rowStringDestruction(rowImg[inde8]["pics"])[0];

  const RWDTitle6 = document.querySelector("#RWD6 img");
  RWDTitle6.src = dataImg.host + rowStringDestruction(rowImg[inde9]["pics"])[0];

  const RWDTitle7 = document.querySelector("#RWD7 img");
  RWDTitle7.src =
    dataImg.host + rowStringDestruction(rowImg[inde10]["pics"])[0];

  const RWDTitle8 = document.querySelector("#RWD8 img");
  RWDTitle8.src =
    dataImg.host + rowStringDestruction(rowImg[inde11]["pics"])[0];

  const RWDTitle9 = document.querySelector("#RWD9 img");
  RWDTitle9.src =
    dataImg.host + rowStringDestruction(rowImg[inde12]["pics"])[0];

  const RWDTitle10 = document.querySelector("#RWD10 img");
  RWDTitle10.src =
    dataImg.host + rowStringDestruction(rowImg[inde13]["pics"])[0];

  const RWDSmall1 = document.querySelector("#small1 img");
  RWDSmall1.src = dataImg.host + rowStringDestruction(rowImg[inde1]["pics"])[0];

  const RWDSmall2 = document.querySelector("#small2 img");
  RWDSmall2.src = dataImg.host + rowStringDestruction(rowImg[inde2]["pics"])[0];

  const RWDSmall3 = document.querySelector("#small3 img");
  RWDSmall3.src = dataImg.host + rowStringDestruction(rowImg[inde3]["pics"])[0];

  const RWDSmall4 = document.querySelector("#small4 img");
  RWDSmall4.src = dataImg.host + rowStringDestruction(rowImg[inde4]["pics"])[0];

  const RWDSmall5 = document.querySelector("#small5 img");
  RWDSmall5.src = dataImg.host + rowStringDestruction(rowImg[inde5]["pics"])[0];

  const RWDSmall6 = document.querySelector("#small6 img");
  RWDSmall6.src = dataImg.host + rowStringDestruction(rowImg[inde6]["pics"])[0];

  const RWDSmall7 = document.querySelector("#small7 img");
  RWDSmall7.src = dataImg.host + rowStringDestruction(rowImg[inde7]["pics"])[0];

  const RWDSmall8 = document.querySelector("#small8 img");
  RWDSmall8.src = dataImg.host + rowStringDestruction(rowImg[inde8]["pics"])[0];

  const RWDSmall9 = document.querySelector("#small9 img");
  RWDSmall9.src = dataImg.host + rowStringDestruction(rowImg[inde9]["pics"])[0];

  const RWDSmall10 = document.querySelector("#small10 img");
  RWDSmall10.src =
    dataImg.host + rowStringDestruction(rowImg[inde10]["pics"])[0];

  const RWDSmall11 = document.querySelector("#small11 img");
  RWDSmall11.src =
    dataImg.host + rowStringDestruction(rowImg[inde11]["pics"])[0];

  const RWDSmall12 = document.querySelector("#small12 img");
  RWDSmall12.src =
    dataImg.host + rowStringDestruction(rowImg[inde12]["pics"])[0];

  const RWDSmall13 = document.querySelector("#small13 img");
  RWDSmall13.src =
    dataImg.host + rowStringDestruction(rowImg[inde13]["pics"])[0];
}
getData();
