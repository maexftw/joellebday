const slides = [...document.querySelectorAll(".slide")];
const prevButtons = [...document.querySelectorAll("[data-prev]")];
const nextButtons = [...document.querySelectorAll("[data-next]")];
const progressNumber = document.querySelector(".progress__number");
const progressTitle = document.querySelector(".progress__title");
const progressBar = document.querySelector(".progress__bar i");
const status = document.querySelector(".sr-status");
const deck = document.querySelector(".deck");
const prefersReducedMotion = matchMedia("(prefers-reduced-motion: reduce)");

let current = 0;
let touchStartX = null;

function resetViewportScroll() {
  const reset = () => {
    deck.scrollLeft = 0;
    deck.scrollTop = 0;
    window.scrollTo(0, 0);
  };

  reset();
  requestAnimationFrame(() => {
    reset();
    requestAnimationFrame(reset);
  });
}

function clamp(index) {
  return Math.max(0, Math.min(slides.length - 1, index));
}

function showSlide(index, announce = true, animate = true) {
  const next = clamp(index);

  if (animate && next !== current && !prefersReducedMotion.matches) {
    deck.classList.remove("is-wiping");
    requestAnimationFrame(() => deck.classList.add("is-wiping"));
  }

  current = next;
  document.documentElement.style.setProperty("--slide", current);

  slides.forEach((slide, slideIndex) => {
    const active = slideIndex === current;
    slide.classList.toggle("is-active", active);
    slide.setAttribute("aria-hidden", String(!active));
    slide.inert = !active;
  });

  prevButtons.forEach((button) => {
    button.disabled = current === 0;
  });
  nextButtons.forEach((button) => {
    button.disabled = current === slides.length - 1;
  });

  const number = String(current + 1).padStart(2, "0");
  const title = slides[current].dataset.title;
  progressNumber.textContent = number;
  progressTitle.textContent = title;
  progressBar.style.transform = `scaleX(${(current + 1) / slides.length})`;

  history.replaceState(null, "", `#${slides[current].id}`);
  resetViewportScroll();
  if (announce) status.textContent = `Folie ${current + 1} von ${slides.length}: ${title}`;
}

function move(direction) {
  showSlide(current + direction);
}

prevButtons.forEach((button) => button.addEventListener("click", () => move(-1)));
nextButtons.forEach((button) => button.addEventListener("click", () => move(1)));

document.addEventListener("keydown", (event) => {
  if (event.target.matches("a, button")) return;

  if (["ArrowRight", "PageDown", " "].includes(event.key)) {
    event.preventDefault();
    move(1);
  } else if (["ArrowLeft", "PageUp"].includes(event.key)) {
    event.preventDefault();
    move(-1);
  } else if (event.key === "Home") {
    event.preventDefault();
    showSlide(0);
  } else if (event.key === "End") {
    event.preventDefault();
    showSlide(slides.length - 1);
  }
});

document.addEventListener("touchstart", (event) => {
  touchStartX = event.changedTouches[0].clientX;
}, { passive: true });

document.addEventListener("touchend", (event) => {
  if (touchStartX === null) return;
  const delta = event.changedTouches[0].clientX - touchStartX;
  touchStartX = null;
  if (Math.abs(delta) < 48) return;
  move(delta < 0 ? 1 : -1);
}, { passive: true });

addEventListener("hashchange", () => {
  const index = slides.findIndex((slide) => `#${slide.id}` === location.hash);
  if (index >= 0 && index !== current) showSlide(index, false);
});

const initialSlide = slides.findIndex((slide) => `#${slide.id}` === location.hash);
showSlide(initialSlide >= 0 ? initialSlide : 0, false, false);
addEventListener("load", resetViewportScroll);

if (!prefersReducedMotion.matches) {
  document.documentElement.classList.add("motion-ok");
}
