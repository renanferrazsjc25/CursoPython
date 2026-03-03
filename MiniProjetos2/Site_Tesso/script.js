function scrollToSection(id) {
  const el = document.getElementById(id);
  if (!el) return;
  el.scrollIntoView({ behavior: "smooth", block: "start" });
}

function handleFormSubmit(event) {
  event.preventDefault();
  const form = event.target;
  const feedback = document.getElementById("form-feedback");
  if (feedback) {
    feedback.hidden = false;
  }
  form.reset();
}

(function setYear() {
  const yearSpan = document.getElementById("year");
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear().toString();
  }
})();

