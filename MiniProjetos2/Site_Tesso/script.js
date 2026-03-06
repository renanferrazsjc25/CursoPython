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

(function initFloatingPromo() {
  const promo = document.getElementById("floating-promo");
  if (!promo) return;

  const cta = document.getElementById("floating-promo-cta");
  const closeBtn = document.getElementById("floating-promo-close");

  const storageKey = "promo_primeira_consulta_dismissed_until";
  const now = Date.now();
  const dismissedUntil = Number(localStorage.getItem(storageKey) || "0");
  if (dismissedUntil && dismissedUntil > now) {
    promo.remove();
    return;
  }

  function hideForDays(days) {
    const until = Date.now() + days * 24 * 60 * 60 * 1000;
    localStorage.setItem(storageKey, String(until));
    promo.remove();
  }

  if (closeBtn) {
    closeBtn.addEventListener("click", function () {
      hideForDays(3);
    });
  }

  if (cta) {
    cta.addEventListener("click", function (event) {
      event.preventDefault();
      scrollToSection("cadastro");
      window.setTimeout(function () {
        const firstField = document.getElementById("nome");
        if (firstField && typeof firstField.focus === "function") {
          firstField.focus({ preventScroll: true });
        }
      }, 450);
    });
  }
})();

