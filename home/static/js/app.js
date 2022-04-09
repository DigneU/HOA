// background header sticky

function scrollHeader() {
  const nav = document.getElementById("header");

  if (this.scrollY >= 5) nav.classList.add("sticky");
  else nav.classList.remove("sticky");
}
window.addEventListener("scroll", scrollHeader);

// SMOOTH SCROLL

// EFFECTS


