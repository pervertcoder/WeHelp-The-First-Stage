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
