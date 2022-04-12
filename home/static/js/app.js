/*showing the menu */
const navMenu = document.getElementById("nav-menu"),
  navToggle = document.getElementById("nav-toggle"),
  navClose = document.getElementById("nav-close");

if (navToggle) {
  navToggle.addEventListener("click", () => {
    navMenu.classList.add("show-menu");
  });
}

if (navClose) {
  navClose.addEventListener("click", () => {
    navMenu.classList.remove("show-menu");
  });
}




// background header sticky

function scrollHeader() {
  const nav = document.getElementById("header");

  if (this.scrollY >= 5) nav.classList.add("sticky");
  else nav.classList.remove("sticky");
}
window.addEventListener("scroll", scrollHeader);

// SMOOTH SCROLL

// EFFECTS

//scroll uppppppppp staffff

function scrollUp() {
  const scrollUp = document.getElementById("scroll-up");

  if (this.scrollY >= 200) scrollUp.classList.add("show-scroll");
  else scrollUp.classList.remove("show-scroll");
}
window.addEventListener("scroll", scrollUp);


// modal viewwwwwwwwwwwwwwwwwwwwwwwwwwwww//////////////

const modalViews = document.querySelectorAll(".form"),
  modalBtns = document.querySelectorAll(".modal"),
  modalCloses = document.querySelectorAll(".modal-close");

let modal = function (modalClick) {
  modalViews[modalClick].classList.add("active-modal");
};

modalBtns.forEach((modalBtn, i) => {
  modalBtn.addEventListener("click", () => {
    modal(i);
  });
});

modalCloses.forEach((modalClose) => {
  modalClose.addEventListener("click", () => {
    modalViews.forEach((modalView) => {
      modalView.classList.remove("active-modal");
    });
  });
});

