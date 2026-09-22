/* Grabenstein Sales – gemeinsames Skript für alle Seiten */
(function () {
  'use strict';

  /* --- Mobiles Menü auf- und zuklappen --- */
  var burger = document.querySelector('.nav__burger');
  var links  = document.querySelector('.nav__links');

  if (burger && links) {
    burger.addEventListener('click', function () {
      var open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', String(!open));
      links.classList.toggle('is-open', !open);
    });

    /* Nach Klick auf einen Link wieder schließen */
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        burger.setAttribute('aria-expanded', 'false');
        links.classList.remove('is-open');
      }
    });

    /* Escape schließt das Menü */
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && links.classList.contains('is-open')) {
        burger.setAttribute('aria-expanded', 'false');
        links.classList.remove('is-open');
        burger.focus();
      }
    });
  }

  /* --- Aktuelle Seite in der Navigation markieren --- */
  var here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav__links a').forEach(function (a) {
    var target = a.getAttribute('href');
    if (target === here) { a.setAttribute('aria-current', 'page'); }
  });

  /* --- Jahreszahl im Footer automatisch aktuell halten --- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();

/* --- Foto-Platzhalter durch leon.jpg ersetzen, sobald die Datei existiert --- */
(function () {
  var platzhalter = document.querySelectorAll('.about__placeholder');
  if (!platzhalter.length) { return; }

  var probe = new Image();
  probe.onload = function () {
    platzhalter.forEach(function (el) {
      var img = document.createElement('img');
      img.src = 'leon.jpg';
      img.alt = 'Leon Grabenstein';
      img.loading = 'lazy';
      el.replaceWith(img);
    });
  };
  probe.src = 'leon.jpg';
})();
