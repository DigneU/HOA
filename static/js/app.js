// background header sticky

function scrollHeader() {
  const nav = document.getElementById("header");

  if (this.scrollY >= 5) nav.classList.add("sticky");
  else nav.classList.remove("sticky");
}
window.addEventListener("scroll", scrollHeader);

// SMOOTH SCROLL

// EFFECTS


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

