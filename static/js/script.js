document.addEventListener("DOMContentLoaded", () => {
  const text = "Srishti Srivastava";
  const el = document.querySelector(".typing-text");
  let i = 0;

  function type() {
    if (i < text.length) {
      el.textContent += text.charAt(i);
      i++;
      setTimeout(type, 100);
    }
  }

  if (el) {
    el.textContent = ""; // Reset
    type();
  }
});
