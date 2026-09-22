/* ---------------------------------------------------------------
   Kontaktformular – Versand über EmailJS

   Datenschutz-Kniff: Das EmailJS-Skript wird NICHT beim Laden der
   Seite geholt, sondern erst in dem Moment, in dem jemand wirklich
   auf "Nachricht senden" klickt und zugestimmt hat. Vorher baut die
   Seite keine Verbindung zu Dritten auf – deshalb braucht sie auch
   kein Cookie-Banner.
   --------------------------------------------------------------- */
(function () {
  'use strict';

  var PUBLIC_KEY  = 'LysyGFZwKaRolLZqO';
  var SERVICE_ID  = 'service_fxkf4yj';
  var TEMPLATE_ID = 'template_7ozivz4';
  var SDK_URL     = 'https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js';

  var form = document.getElementById('kontaktformular');
  if (!form) { return; }

  var knopf   = document.getElementById('senden');
  var erfolg  = document.getElementById('erfolg');
  var fehler  = document.getElementById('fehler');
  var sdkLaed = null;

  /* Laedt das EmailJS-Skript genau einmal, on demand. */
  function sdkLaden() {
    /* Schon vorhanden? Dann nichts nachladen. */
    if (window.emailjs && typeof window.emailjs.send === 'function') {
      return Promise.resolve();
    }
    if (sdkLaed) { return sdkLaed; }
    sdkLaed = new Promise(function (erfuellen, ablehnen) {
      var s = document.createElement('script');
      s.src = SDK_URL;
      s.onload = function () {
        try {
          window.emailjs.init({ publicKey: PUBLIC_KEY });
          erfuellen();
        } catch (e) { ablehnen(e); }
      };
      s.onerror = function () { ablehnen(new Error('EmailJS konnte nicht geladen werden.')); };
      document.head.appendChild(s);
    });
    return sdkLaed;
  }

  function meldung(welche) {
    erfolg.hidden = (welche !== 'ok');
    fehler.hidden = (welche !== 'fehler');
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    meldung(null);

    /* Browser-eigene Pflichtfeldpruefung inklusive Einwilligung */
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    /* Spam-Falle: Bots fuellen das unsichtbare Feld aus.
       Wir tun so, als waere alles gut, senden aber nichts. */
    if (document.getElementById('website').value !== '') {
      meldung('ok');
      form.reset();
      return;
    }

    knopf.disabled = true;
    knopf.textContent = 'Wird gesendet …';

    sdkLaden()
      .then(function () {
        return window.emailjs.send(SERVICE_ID, TEMPLATE_ID, {
          from_name:    document.getElementById('name').value,
          company_name: document.getElementById('firma').value,
          reply_to:     document.getElementById('email').value,
          message:      document.getElementById('message').value
        });
      })
      .then(function () {
        meldung('ok');
        form.reset();
      })
      .catch(function (err) {
        console.error('Versand fehlgeschlagen:', err);
        meldung('fehler');
      })
      .then(function () {
        knopf.disabled = false;
        knopf.textContent = 'Nachricht senden';
      });
  });
})();
