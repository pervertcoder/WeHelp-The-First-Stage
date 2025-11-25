"use strict";

const nameID = document.getElementById("nameID");
const nameSearch = document.getElementById("searchBTN");
const memberName = document.getElementById("name");
nameSearch.addEventListener("click", async function () {
  const res = await fetch("/api/member/" + nameID.value);
  const memberData = await res.json();
  if (!memberData.id) {
    memberName.textContent = "找不到會員";
  }
  if (memberData.id) {
    memberName.textContent =
      memberData.name + " " + "(" + memberData.email + ")";
  }
});
