"use strict";

const nameID = document.getElementById("nameID");
const nameSearch = document.getElementById("searchBTN");
const memberName = document.getElementById("name");
nameSearch.addEventListener("click", async function () {
  if (nameID.value.trim() === "") {
    alert("請輸入資料");
  } else {
    const res = await fetch("/api/member/" + nameID.value.trim());
    const memberData = await res.json();
    if (!memberData.id) {
      memberName.textContent = "找不到會員";
    }
    if (memberData.id) {
      // const childBlock = document.createElement("p");
      // childBlock.setAttribute("class", "childClass");
      // childBlock.textContent =
      //   memberData.name + " " + "(" + memberData.email + ")";
      // memberName.appendChild(childBlock);
      memberName.textContent =
        memberData.name + " " + "(" + memberData.email + ")";
    }
  }
});

const newName = document.getElementById("newNameID");
const updatebtn = document.getElementById("updateBTN");
const nameTitle = document.getElementById("newNameTitle");
const state = document.getElementById("state");

updatebtn.addEventListener("click", async function () {
  if (newName.value.trim() === "") {
    alert("請輸入資料");
  } else {
    console.log(typeof newName.value);
    let res = await fetch("/api/member", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: newName.value }),
    });
    let result = await res.json();
    console.log(result);
    if (result["ok"]) {
      nameTitle.textContent = newName.value + "，歡迎登入系統";
      newName.value = "";
      state.textContent = "更新成功";
    }
    if (result["error"]) {
      state.textContent = "更新失敗";
    }
  }
});
