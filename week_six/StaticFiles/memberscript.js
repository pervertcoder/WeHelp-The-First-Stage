"use strict";

const message = document.getElementById("messageinput");
const messageSenter = document.getElementById("buttonmessage");
const messageData = document.getElementById("message");

const clickSent = function (event) {
  event.preventDefault();
  if (message.value === "") {
    alert("請輸入訊息");
  } else {
    console.log("test");
    messageData.submit();
  }
};

messageSenter.addEventListener("click", clickSent);

const messagedelete = document.querySelectorAll(".buttondelete");

for (let i = 0; i < messagedelete.length; i++) {
  messagedelete[i].addEventListener("click", function () {
    let text = "確定要刪除留言嗎？";
    if (confirm(text)) {
      let commentId = this.dataset.id;
      console.log(commentId);
      fetch("/deleteMessage", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: commentId }),
      })
        .then((response) => response.json())
        .then((data) => {
          window.location.href = "/member";
          console.log(data);
        });
    } else {
      console.log("取消刪除");
    }
  });
}
