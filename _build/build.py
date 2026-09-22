#!/usr/bin/env python3
"""
Baut alle HTML-Seiten von grabensteinsales.de aus einem gemeinsamen
Grundgeruest (Kopfbereich, Navigation, Fusszeile) + dem Inhalt je Seite.

Aufruf:  python3 _build/build.py        (aus dem Projektordner heraus)

Warum:   So sehen Navigation und Fusszeile auf allen Seiten garantiert
         gleich aus. Du kannst die fertigen .html-Dateien trotzdem ganz
         normal von Hand bearbeiten - dieses Skript ist optional.
         Wenn du es erneut laufen laesst, werden Handaenderungen im
         Geruest allerdings ueberschrieben.
"""
import os, pathlib

SITE = "https://www.grabensteinsales.de"
BRAND = "Grabenstein Sales"
OUT = pathlib.Path(__file__).resolve().parent.parent

NAV = [
    ("index.html",     "Start"),
    ("ueber-uns.html", "Über mich"),
    ("angebot.html",   "Leistungen"),
    ("ablauf.html",    "So arbeite ich"),
]

def head(title, desc, page):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – {BRAND}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{page}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title} – {BRAND}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{page}">
<meta property="og:locale" content="de_DE">
<link rel="icon" href="favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip-link" href="#main">Zum Inhalt springen</a>
"""

def nav():
    items = "\n".join(
        f'        <li><a href="{href}">{label}</a></li>' for href, label in NAV
    )
    return f"""<header class="nav">
  <div class="wrap nav__inner">
    <a class="nav__brand" href="index.html">
      <img class="nav__logo" src="logo-dunkel.png" alt="" width="320" height="320">
      <span class="nav__name">{BRAND}</span>
    </a>
    <button class="nav__burger" type="button" aria-expanded="false" aria-controls="hauptmenue" aria-label="Menü öffnen">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav__links" id="hauptmenue">
{items}
        <li><a class="btn btn--primary" href="kontakt.html">Kontakt</a></li>
    </ul>
  </div>
</header>
"""

def footer():
    links = "\n".join(
        f'        <li><a href="{href}">{label}</a></li>' for href, label in NAV
    )
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="footer__top">
      <div class="footer__brand">
        <strong>{BRAND}</strong>
        <p>Gemeinsam starten. Gemeinsam wachsen.</p>
      </div>
      <div>
        <h4>Seiten</h4>
        <ul>
{links}
        <li><a href="kontakt.html">Kontakt</a></li>
        </ul>
      </div>
      <div>
        <h4>Rechtliches</h4>
        <ul>
          <li><a href="impressum.html">Impressum</a></li>
          <li><a href="datenschutz.html">Datenschutzerklärung</a></li>
          <li><a href="agb.html">AGB</a></li>
        </ul>
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul>
          <li><a href="mailto:kontakt@grabensteinsales.de">kontakt@grabensteinsales.de</a></li>
          <li><span class="todo">[Telefonnummer ergänzen]</span></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span data-year>2026</span> {BRAND}</span>
      <span>Alle Rechte vorbehalten.</span>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""

def page(filename, title, desc, body, extra_head="", extra_js=""):
    html = head(title, desc, filename).replace("</head>", extra_head + "</head>") \
         + nav() \
         + f'<main id="main">\n{body}\n</main>\n' \
         + footer().replace("</body>", extra_js + "</body>")
    (OUT / filename).write_text(html, encoding="utf-8")
    print(f"  geschrieben: {filename}")

def redirect(filename, target, label):
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>Weiterleitung – {BRAND}</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{SITE}/{target}">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<main class="section"><div class="wrap prose">
<p>Diese Seite heißt jetzt <a href="{target}">{label}</a>. Du wirst automatisch weitergeleitet.</p>
</div></main>
<script>location.replace("{target}");</script>
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")
    print(f"  weiterleitung: {filename} -> {target}")


# =====================================================================
#  INHALTE DER EINZELNEN SEITEN
#  Stellen mit  <span class="todo">  musst du noch ausfuellen.
#  Sie sind auf der Seite gelb markiert, damit du keine uebersiehst.
# =====================================================================

TODO = '<span class="todo">{}</span>'

# ---------------------------------------------------------------- START
index_body = """
<section class="hero hero--image">
  <div class="wrap hero__inner">
    <span class="eyebrow" style="color:#8FD3B0">Gemeinsam starten. Gemeinsam wachsen.</span>
    <h1>Vertrieb, der zu deinem Startup passt</h1>
    <p>Viele junge Unternehmen haben ein gutes Produkt – aber keinen verlässlichen Weg zum Kunden.
       Genau da setze ich an: Wir bauen gemeinsam einen Vertrieb auf, der zu deinem Team,
       deinem Markt und deinem Budget passt. Ohne Konzept in der Schublade, sondern mit
       Gesprächen, die tatsächlich geführt werden.</p>
    <div class="hero__actions">
      <a class="btn btn--primary" href="angebot.html">Leistungen ansehen</a>
      <a class="btn btn--ghost" href="kontakt.html">Unverbindlich sprechen</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section__head section__head--center">
      <span class="eyebrow">Wobei ich helfe</span>
      <h2>Drei Bereiche, ein Ziel: planbarer Umsatz</h2>
      <p class="lead">Je nachdem, wo du gerade stehst, setzen wir an einem anderen Punkt an.</p>
    </div>
    <div class="grid grid--3">
      <article class="card">
        <div class="card__num">1</div>
        <h3>Erste Kunden gewinnen</h3>
        <p>Vom fertigen Produkt zur ersten zahlenden Kundschaft: Zielgruppe schärfen,
           Ansprache entwickeln, Gespräche führen – und aus den Absagen lernen,
           bevor sie sich wiederholen.</p>
      </article>
      <article class="card">
        <div class="card__num">2</div>
        <h3>Vertrieb strukturieren</h3>
        <p>Aus Zufallstreffern wird ein Prozess. Klare Pipeline, nachvollziehbare Angebote,
           verlässliches Nachfassen und Zahlen, auf die du dich bei der Planung stützen kannst.</p>
      </article>
      <article class="card">
        <div class="card__num">3</div>
        <h3>Team befähigen</h3>
        <p>Damit der Vertrieb auch ohne mich weiterläuft: Gesprächsleitfäden, Training
           am echten Fall und klare Verantwortlichkeiten im Team.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="section__head section__head--center">
      <span class="eyebrow">Zusammenarbeit</span>
      <h2>Zwei Wege, mit mir zu arbeiten</h2>
      <p class="lead">Ein kompakter Einstieg oder eine längere Begleitung – je nachdem,
         wie viel Struktur schon steht.</p>
    </div>
    <div class="grid grid--2">
      <article class="card plan">
        <h3>Basic Paket</h3>
        <p>Ideal für junge Startups, die erste Kunden gewinnen möchten, aber noch keine
           feste Vertriebsstruktur haben.</p>
        <a class="btn btn--outline" href="angebot.html">Details ansehen</a>
      </article>
      <article class="card plan plan--featured">
        <span class="plan__tag">Meist gewählt</span>
        <h3>Plus Paket</h3>
        <p>Für Startups, die aktiv Kunden gewinnen und eine langfristige Vertriebsstrategie
           aufbauen möchten.</p>
        <a class="btn btn--primary" href="angebot.html">Details ansehen</a>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap about">
    <div>
      <span class="eyebrow">Über mich</span>
      <h2>Moin, ich bin Leon</h2>
      <p>Ich bin Leon Grabenstein und begleite junge Unternehmen beim Aufbau ihres Vertriebs.
         Mir geht es nicht um Verkaufstricks, sondern um etwas Unspektakuläreres:
         die richtigen Leute ansprechen, ehrlich zuhören und dann konsequent dranbleiben.</p>
      <p>Statt einer Präsentation, die danach niemand mehr öffnet, arbeite ich mit dir
         an den Dingen, die du am Montag danach tatsächlich brauchst.</p>
      <a class="btn btn--outline" href="ueber-uns.html">Mehr über mich</a>
    </div>
    <div class="about__photo">
      <div class="about__placeholder">
        <p>Hier kommt dein Foto hin.<br><br>
        Speichere es als <strong>leon.jpg</strong> im Projektordner –<br>
        dann tauscht es sich automatisch ein.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <h2>Lass uns über deinen Vertrieb sprechen</h2>
    <p>Ein erstes Gespräch kostet dich nichts außer 30 Minuten. Danach weißt du,
       ob und wie ich dir helfen kann.</p>
    <a class="btn btn--primary" href="kontakt.html">Gespräch anfragen</a>
  </div>
</section>
"""

# ------------------------------------------------------------ UEBER MICH
ueber_body = """
<section class="hero hero--sub">
  <div class="wrap hero__inner">
    <h1>Über mich</h1>
    <p>Wer hinter Grabenstein Sales steckt – und wie ich arbeite.</p>
  </div>
</section>

<section class="section">
  <div class="wrap about">
    <div>
      <span class="eyebrow">Zur Person</span>
      <h2>Moin, ich bin Leon</h2>
      <p>Ich bin Leon Grabenstein und helfe Startups dabei, ihren Vertrieb aufzubauen –
         von der ersten Kundenansprache bis zu einer Struktur, die auch dann noch trägt,
         wenn das Team wächst.</p>
      <p><span class="todo">[Bitte ergänzen: Was hast du vorher gemacht? Ausbildung, Studium,
         Stationen im Vertrieb, Branchen. Zwei bis drei Sätze reichen – das ist der Absatz,
         der über Vertrauen entscheidet.]</span></p>
      <p>Was mich antreibt: Ich sehe zu viele gute Produkte, die scheitern, weil niemand
         von ihnen erfährt. Ein gutes Produkt verkauft sich eben nicht von allein –
         es braucht jemanden, der den Weg zum Kunden baut.</p>
      <a class="btn btn--outline" href="kontakt.html">Lass uns sprechen</a>
    </div>
    <div class="about__photo">
      <div class="about__placeholder">
        <p>Hier kommt dein Foto hin.<br><br>
        Speichere es als <strong>leon.jpg</strong> im Projektordner –<br>
        dann tauscht es sich automatisch ein.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="section__head section__head--center">
      <span class="eyebrow">Haltung</span>
      <h2>Wofür ich stehe</h2>
      <p class="lead">Vier Punkte, auf die du dich bei der Zusammenarbeit verlassen kannst.</p>
    </div>
    <div class="grid grid--4">
      <article class="card">
        <h3>Ehrlichkeit</h3>
        <p>Wenn ich dir nicht helfen kann, sage ich das im Erstgespräch – und nicht,
           nachdem du bezahlt hast.</p>
      </article>
      <article class="card">
        <h3>Nachvollziehbarkeit</h3>
        <p>Du weißt jederzeit, woran ich arbeite und warum. Keine Methoden,
           die ich dir nicht erklären kann.</p>
      </article>
      <article class="card">
        <h3>Praxis vor Theorie</h3>
        <p>Wir arbeiten an deinen echten Kunden und echten Gesprächen,
           nicht an Musterbeispielen.</p>
      </article>
      <article class="card">
        <h3>Unabhängigkeit</h3>
        <p>Ziel ist, dass du mich irgendwann nicht mehr brauchst.
           Alles, was wir aufbauen, gehört dir.</p>
      </article>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <h2>Passt das zu dir?</h2>
    <p>Dann lass uns 30 Minuten sprechen und schauen, wo du gerade stehst.</p>
    <a class="btn btn--primary" href="kontakt.html">Gespräch anfragen</a>
  </div>
</section>
"""

# ------------------------------------------------------------ LEISTUNGEN
angebot_body = """
<section class="hero hero--sub">
  <div class="wrap hero__inner">
    <h1>Leistungen</h1>
    <p>Zwei Pakete, je nachdem wie viel Vertriebsstruktur bei dir schon steht.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--2">

      <!-- ============ BASIC ============ -->
      <article class="card plan">
        <h3>Basic Paket</h3>
        <p>Ideal für junge Startups, die erste Kunden gewinnen möchten, aber noch keine
           feste Vertriebsstruktur haben.</p>
        <div class="plan__price">
          <span class="todo">[Preis eintragen oder „auf Anfrage“]</span>
          <small>zzgl. USt., falls zutreffend</small>
        </div>
        <p><span class="todo">Entwurf – bitte prüfen und durch deine echten Leistungen ersetzen:</span></p>
        <ul>
          <li>Analyse deiner aktuellen Vertriebssituation</li>
          <li>Zielgruppe und Wunschkunde klar definiert</li>
          <li>Ansprache und Gesprächsleitfaden für den Erstkontakt</li>
          <li>Gemeinsame Live-Gespräche mit echten Interessenten</li>
          <li>Kompakte Handlungsempfehlung zum Abschluss</li>
        </ul>
        <a class="btn btn--outline" href="kontakt.html">Basic Paket anfragen</a>
      </article>

      <!-- ============ PLUS ============ -->
      <article class="card plan plan--featured">
        <span class="plan__tag">Meist gewählt</span>
        <h3>Plus Paket</h3>
        <p>Für Startups, die aktiv Kunden gewinnen und eine langfristige Vertriebsstrategie
           aufbauen möchten.</p>
        <div class="plan__price">
          <span class="todo">[Preis eintragen oder „auf Anfrage“]</span>
          <small>zzgl. USt., falls zutreffend</small>
        </div>
        <p><span class="todo">Entwurf – bitte prüfen und durch deine echten Leistungen ersetzen:</span></p>
        <ul>
          <li>Alles aus dem Basic Paket</li>
          <li>Aufbau einer Vertriebspipeline inklusive Tool-Einrichtung</li>
          <li>Angebots- und Nachfassprozess, der wirklich genutzt wird</li>
          <li>Schulung deines Teams am echten Fall</li>
          <li>Feste Begleitung über <span class="todo">[Zeitraum]</span> mit regelmäßigen Terminen</li>
          <li>Kennzahlen, mit denen du den Vertrieb steuern kannst</li>
        </ul>
        <a class="btn btn--primary" href="kontakt.html">Plus Paket anfragen</a>
      </article>

    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="section__head section__head--center">
      <span class="eyebrow">Häufige Fragen</span>
      <h2>Bevor du anfragst</h2>
    </div>
    <div class="grid grid--2">
      <article class="card">
        <h3>Für wen ist das nichts?</h3>
        <p>Wenn du jemanden suchst, der dir fertige Kundenlisten verkauft oder
           in deinem Namen Kaltakquise betreibt, bin ich der Falsche.
           Ich baue mit dir auf – ich übernehme nicht.</p>
      </article>
      <article class="card">
        <h3>Wie lange dauert das?</h3>
        <p><span class="todo">[Bitte ergänzen: typische Dauer der beiden Pakete,
           z.&nbsp;B. „Basic: 2–3 Wochen, Plus: 3–6 Monate“]</span></p>
      </article>
      <article class="card">
        <h3>Wie läuft der Start ab?</h3>
        <p>Immer mit einem unverbindlichen Gespräch von etwa 30 Minuten.
           Danach bekommst du ein schriftliches Angebot – erst dann entscheidest du.</p>
      </article>
      <article class="card">
        <h3>Arbeitest du vor Ort?</h3>
        <p><span class="todo">[Bitte ergänzen: remote, vor Ort, oder beides?
           Falls vor Ort: in welchem Umkreis?]</span></p>
      </article>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <h2>Noch unsicher, welches Paket passt?</h2>
    <p>Schreib mir kurz, wo du stehst. Ich sage dir ehrlich, was Sinn ergibt –
       auch wenn das heißt, dass du noch warten solltest.</p>
    <a class="btn btn--primary" href="kontakt.html">Frage stellen</a>
  </div>
</section>
"""

# ------------------------------------------------------------ SO ARBEITE ICH
ablauf_body = """
<section class="hero hero--sub">
  <div class="wrap hero__inner">
    <h1>So arbeite ich</h1>
    <p>Vom ersten Gespräch bis zu einem Vertrieb, der ohne mich weiterläuft.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section__head section__head--center">
      <span class="eyebrow">Ablauf</span>
      <h2>Vier Schritte, die aufeinander aufbauen</h2>
      <p class="lead">Kein starres Programm – aber eine Reihenfolge, die sich bewährt hat.</p>
    </div>
    <div class="grid grid--4">
      <article class="card">
        <div class="card__num">1</div>
        <h3>Zuhören</h3>
        <p>Ein Gespräch von etwa 30 Minuten: Was verkaufst du, an wen, und woran
           hakt es gerade konkret? Kostenlos und unverbindlich.</p>
      </article>
      <article class="card">
        <div class="card__num">2</div>
        <h3>Einordnen</h3>
        <p>Ich schaue mir deine bisherigen Gespräche, Angebote und Zahlen an
           und benenne die zwei, drei Stellen mit dem größten Hebel.</p>
      </article>
      <article class="card">
        <div class="card__num">3</div>
        <h3>Umsetzen</h3>
        <p>Wir arbeiten gemeinsam an echten Fällen: Ansprache schärfen,
           Gespräche führen, Angebote überarbeiten, nachfassen.</p>
      </article>
      <article class="card">
        <div class="card__num">4</div>
        <h3>Übergeben</h3>
        <p>Alles Erarbeitete geht dokumentiert an dich und dein Team über –
           damit es auch ohne mich weiterläuft.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section__head section__head--center">
      <span class="eyebrow">Grundsätze</span>
      <h2>Worauf du dich verlassen kannst</h2>
    </div>
    <div class="grid grid--3">
      <article class="card" style="background:rgba(255,255,255,.06); border-color:rgba(255,255,255,.14)">
        <h3>Kein Verkaufsdruck</h3>
        <p style="color:#C3D6CE">Wenn dein Produkt noch nicht so weit ist, sage ich dir das –
           statt dir ein Paket zu verkaufen, das jetzt nichts bringt.</p>
      </article>
      <article class="card" style="background:rgba(255,255,255,.06); border-color:rgba(255,255,255,.14)">
        <h3>Feste Ansprechperson</h3>
        <p style="color:#C3D6CE">Du arbeitest mit mir – nicht mit einem wechselnden Team
           oder einer Assistenz, die den Kontext nicht kennt.</p>
      </article>
      <article class="card" style="background:rgba(255,255,255,.06); border-color:rgba(255,255,255,.14)">
        <h3>Vertraulichkeit</h3>
        <p style="color:#C3D6CE">Zahlen, Kundenlisten und Strategien bleiben zwischen uns.
           Auf Wunsch auch schriftlich per NDA.</p>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section__head section__head--center">
      <h2>Kundenstimmen folgen</h2>
      <p class="lead">Grabenstein Sales ist jung. Sobald die ersten Projekte abgeschlossen sind
         und meine Kunden mit ihrem Namen dahinterstehen möchten, findest du ihre
         Rückmeldungen genau hier. Erfundene Zitate wirst du auf dieser Seite nicht finden.</p>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <h2>Bereit für Schritt&nbsp;1?</h2>
    <p>Das erste Gespräch ist kostenlos und verpflichtet zu nichts.</p>
    <a class="btn btn--primary" href="kontakt.html">Gespräch anfragen</a>
  </div>
</section>
"""

# ---------------------------------------------------------------- KONTAKT
kontakt_body = """
<section class="hero hero--sub">
  <div class="wrap hero__inner">
    <h1>Kontakt</h1>
    <p>Schreib mir, wo du gerade stehst. Ich melde mich in der Regel innerhalb von
       24&nbsp;Stunden zurück.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--2" style="align-items:start; gap:44px">

      <div class="card">
        <h2 style="font-size:1.5rem">Nachricht senden</h2>
        <form class="form" id="kontaktformular" novalidate>
          <div class="form__row">
            <div class="field">
              <label for="name">Name <span aria-hidden="true">*</span></label>
              <input type="text" id="name" name="name" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="firma">Unternehmen</label>
              <input type="text" id="firma" name="firma" autocomplete="organization">
            </div>
          </div>

          <div class="field">
            <label for="email">E-Mail <span aria-hidden="true">*</span></label>
            <input type="email" id="email" name="email" autocomplete="email" required>
          </div>

          <div class="field">
            <label for="message">Nachricht <span aria-hidden="true">*</span></label>
            <textarea id="message" name="message" required
              placeholder="Was verkaufst du, an wen – und woran hakt es gerade?"></textarea>
          </div>

          <!-- Honeypot gegen Spam-Bots: fuer Menschen unsichtbar -->
          <div style="position:absolute; left:-9999px" aria-hidden="true">
            <label for="website">Website</label>
            <input type="text" id="website" name="website" tabindex="-1" autocomplete="off">
          </div>

          <div class="consent">
            <input type="checkbox" id="einwilligung" required>
            <label for="einwilligung">
              Ich bin damit einverstanden, dass meine Angaben zur Beantwortung meiner Anfrage
              verarbeitet und dafür über den Dienstleister EmailJS versendet werden.
              Details in der <a href="datenschutz.html">Datenschutzerklärung</a>.
              <span aria-hidden="true">*</span>
            </label>
          </div>

          <button class="btn btn--primary" type="submit" id="senden">Nachricht senden</button>

          <p class="form__note">Mit <span aria-hidden="true">*</span> markierte Felder sind
             Pflichtfelder. Solange du nicht auf „Senden“ klickst, verlassen deine Eingaben
             deinen Browser nicht.</p>

          <div class="alert alert--ok"   id="erfolg" role="status" hidden>
            Danke! Deine Nachricht ist raus. Ich melde mich zeitnah bei dir.
          </div>
          <div class="alert alert--fail" id="fehler" role="alert" hidden>
            Das hat leider nicht geklappt. Schreib mir gern direkt an
            <a href="mailto:kontakt@grabensteinsales.de">kontakt@grabensteinsales.de</a>.
          </div>
        </form>
      </div>

      <div>
        <h2 style="font-size:1.5rem">Lieber direkt?</h2>
        <p>Kein Formular nötig – erreich mich einfach so:</p>
        <p>
          <strong>E-Mail</strong><br>
          <a href="mailto:kontakt@grabensteinsales.de">kontakt@grabensteinsales.de</a>
        </p>
        <p>
          <strong>Telefon</strong><br>
          <span class="todo">[Telefonnummer ergänzen]</span>
        </p>
        <p>
          <strong>Erreichbarkeit</strong><br>
          <span class="todo">[z.&nbsp;B. Mo–Fr, 9–18 Uhr]</span>
        </p>
        <hr style="border:none; border-top:1px solid var(--c-line); margin:28px 0">
        <h3>Was passiert nach deiner Anfrage?</h3>
        <p>Ich melde mich innerhalb von 24 Stunden und schlage einen Termin für ein
           unverbindliches Gespräch von etwa 30 Minuten vor. Kein Verkaufsgespräch –
           erst einmal geht es nur darum zu verstehen, wo du stehst.</p>
      </div>

    </div>
  </div>
</section>
"""

KONTAKT_JS = """<script src="js/kontakt.js"></script>
"""

# -------------------------------------------------------------- IMPRESSUM
impressum_body = """
<section class="hero hero--sub">
  <div class="wrap hero__inner"><h1>Impressum</h1></div>
</section>

<section class="section">
  <div class="wrap prose">

    <h2>Angaben gemäß § 5 DDG</h2>
    <address>
      <span class="todo">[Vollständiger Name, z.&nbsp;B. Leon Grabenstein]</span><br>
      <span class="todo">[Firmierung, falls abweichend, z.&nbsp;B. Grabenstein Sales]</span><br>
      <span class="todo">[Straße und Hausnummer]</span><br>
      <span class="todo">[PLZ und Ort]</span><br>
      Deutschland
    </address>
    <p><strong>Hinweis:</strong> Eine ladungsfähige Anschrift ist Pflicht. Ein Postfach
       genügt nicht. Wenn du von zu Hause arbeitest, muss deine Privatadresse hier stehen –
       eine Alternative ist eine sogenannte ladungsfähige Geschäftsadresse von einem
       Anbieter für virtuelle Büros.</p>

    <h2>Kontakt</h2>
    <p>
      Telefon: <span class="todo">[Telefonnummer]</span><br>
      E-Mail: <a href="mailto:kontakt@grabensteinsales.de">kontakt@grabensteinsales.de</a>
    </p>
    <p><strong>Hinweis:</strong> Eine Telefonnummer ist nicht zwingend, aber es muss eine
       zweite Möglichkeit zur schnellen Kontaktaufnahme neben der E-Mail geben.
       Eine Telefonnummer ist der einfachste Weg, das zu erfüllen.</p>

    <h2>Umsatzsteuer</h2>
    <p class="todo">[Falls USt-IdNr. vorhanden: „Umsatzsteuer-Identifikationsnummer gemäß
       § 27a UStG: DE…“ — Falls Kleinunternehmer nach § 19 UStG: diesen Abschnitt ersatzlos
       löschen. Die Steuernummer gehört NICHT ins Impressum.]</p>

    <h2>Redaktionell verantwortlich</h2>
    <address>
      <span class="todo">[Name und Anschrift wie oben]</span>
    </address>

    <h2>Verbraucherstreitbeilegung</h2>
    <p>Ich bin nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer
       Verbraucherschlichtungsstelle teilzunehmen.</p>

    <h2>Haftung für Inhalte</h2>
    <p>Als Diensteanbieter bin ich gemäß § 7 Abs. 1 DDG für eigene Inhalte auf diesen Seiten
       nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 DDG bin ich als
       Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde
       Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige
       Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von
       Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine
       diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten
       Rechtsverletzung möglich. Bei Bekanntwerden entsprechender Rechtsverletzungen werde
       ich diese Inhalte umgehend entfernen.</p>

    <h2>Haftung für Links</h2>
    <p>Mein Angebot enthält gegebenenfalls Links zu externen Websites Dritter, auf deren
       Inhalte ich keinen Einfluss habe. Deshalb kann ich für diese fremden Inhalte auch
       keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige
       Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum
       Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft; rechtswidrige Inhalte
       waren zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente inhaltliche
       Kontrolle der verlinkten Seiten ist ohne konkrete Anhaltspunkte einer Rechtsverletzung
       nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werde ich derartige Links
       umgehend entfernen.</p>

    <h2>Urheberrecht</h2>
    <p>Die durch den Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten
       unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung,
       Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechts
       bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.
       Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen
       Gebrauch gestattet.</p>

  </div>
</section>
"""

# ------------------------------------------------------------ DATENSCHUTZ
datenschutz_body = """
<section class="hero hero--sub">
  <div class="wrap hero__inner"><h1>Datenschutzerklärung</h1></div>
</section>

<section class="section">
  <div class="wrap prose">

    <h2>1. Verantwortlicher</h2>
    <p>Verantwortlich für die Datenverarbeitung auf dieser Website ist:</p>
    <address>
      <span class="todo">[Vollständiger Name]</span><br>
      <span class="todo">[Straße und Hausnummer]</span><br>
      <span class="todo">[PLZ und Ort]</span><br>
      Deutschland<br>
      E-Mail: <a href="mailto:kontakt@grabensteinsales.de">kontakt@grabensteinsales.de</a><br>
      Telefon: <span class="todo">[Telefonnummer]</span>
    </address>
    <p>Ein Datenschutzbeauftragter ist nicht bestellt, da die gesetzlichen Voraussetzungen
       hierfür nicht vorliegen.</p>

    <h2>2. Grundsätzliches</h2>
    <p>Diese Website verarbeitet so wenige personenbezogene Daten wie möglich. Konkret heißt das:</p>
    <ul>
      <li>Es werden <strong>keine Cookies</strong> gesetzt.</li>
      <li>Es findet <strong>keine Analyse oder Reichweitenmessung</strong> statt –
          kein Google Analytics, kein Matomo, keine Tracking-Pixel.</li>
      <li>Es sind <strong>keine Schriftarten, Karten oder Videos von Dritten</strong> eingebunden.
          Die Seite nutzt ausschließlich Schriften, die bereits auf deinem Gerät vorhanden sind.</li>
      <li>Solange du das Kontaktformular nicht absendest, wird <strong>keine Verbindung
          zu Dritten</strong> aufgebaut.</li>
    </ul>
    <p>Aus diesem Grund ist auf dieser Website auch kein Cookie-Banner erforderlich.</p>

    <h2>3. Hosting und Server-Logdateien</h2>
    <p>Diese Website wird bei GitHub Pages gehostet, einem Dienst der GitHub&nbsp;Inc.,
       88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA (Tochterunternehmen der
       Microsoft Corporation).</p>
    <p>Beim Aufruf der Website werden vom Server automatisch Informationen erfasst, die dein
       Browser übermittelt. Dazu gehören insbesondere:</p>
    <ul>
      <li>IP-Adresse des anfragenden Geräts</li>
      <li>Datum und Uhrzeit des Zugriffs</li>
      <li>Name und URL der abgerufenen Datei</li>
      <li>Verwendeter Browser und Betriebssystem</li>
      <li>Gegebenenfalls die zuvor besuchte Website (Referrer)</li>
    </ul>
    <p>Diese Daten sind technisch erforderlich, um die Website auszuliefern und ihre
       Stabilität und Sicherheit zu gewährleisten. Rechtsgrundlage ist Art.&nbsp;6 Abs.&nbsp;1
       lit.&nbsp;f DSGVO (berechtigtes Interesse an einer technisch fehlerfreien Darstellung).
       Eine Zusammenführung dieser Daten mit anderen Datenquellen findet nicht statt.</p>
    <p>Da GitHub seinen Sitz in den USA hat, kann eine Übermittlung personenbezogener Daten
       in ein Drittland nicht ausgeschlossen werden.
       <span class="todo">[Bitte prüfen und ergänzen: aktuelle Grundlage der Übermittlung,
       z.&nbsp;B. Zertifizierung nach dem EU-US Data Privacy Framework oder
       Standardvertragsklauseln. Steht in den Datenschutzhinweisen von GitHub.]</span></p>
    <p>Weitere Informationen:
       <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement"
          rel="noopener">Datenschutzerklärung von GitHub</a>.</p>

    <h2>4. Kontaktformular</h2>
    <p>Wenn du mir über das Kontaktformular eine Nachricht schickst, werden die von dir
       eingegebenen Daten – Name, optional dein Unternehmen, deine E-Mail-Adresse und deine
       Nachricht – zum Zweck der Bearbeitung deiner Anfrage verarbeitet.</p>
    <p><strong>Ablauf:</strong> Deine Eingaben verlassen deinen Browser erst, wenn du aktiv
       auf „Nachricht senden“ klickst und zuvor der Verarbeitung zugestimmt hast. Erst in
       diesem Moment wird der technische Baustein des Versanddienstleisters nachgeladen.</p>
    <p><strong>Eingesetzter Dienstleister:</strong> Der Versand erfolgt über EmailJS.
       <span class="todo">[Bitte ergänzen: vollständiger Name und Anschrift des Anbieters
       sowie Link zu dessen Datenschutzerklärung – findest du auf emailjs.com. Prüfe dort
       außerdem, ob ein Auftragsverarbeitungsvertrag nach Art. 28 DSGVO angeboten wird,
       und schließe ihn ab.]</span></p>
    <p><strong>Rechtsgrundlage:</strong> Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;a DSGVO (deine
       Einwilligung über die Checkbox) sowie Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;b DSGVO,
       soweit deine Anfrage auf den Abschluss eines Vertrages gerichtet ist.
       Du kannst deine Einwilligung jederzeit für die Zukunft widerrufen – eine formlose
       E-Mail genügt.</p>
    <p><strong>Speicherdauer:</strong> Deine Anfrage verbleibt in meinem E-Mail-Postfach,
       bis der Zweck ihrer Verarbeitung entfällt, also die Anfrage abschließend bearbeitet
       ist. Danach lösche ich sie, sofern keine gesetzlichen Aufbewahrungspflichten
       entgegenstehen.</p>

    <h2>5. Kontaktaufnahme per E-Mail oder Telefon</h2>
    <p>Wenn du mich direkt per E-Mail oder Telefon kontaktierst, verarbeite ich deine Angaben
       ausschließlich zur Bearbeitung deines Anliegens. Rechtsgrundlage ist
       Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;b DSGVO bei vertragsbezogenen Anfragen, ansonsten
       Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;f DSGVO.</p>

    <h2>6. Verschlüsselung</h2>
    <p>Diese Website nutzt eine SSL- bzw. TLS-Verschlüsselung. Du erkennst sie am „https://“
       in der Adresszeile deines Browsers. Dadurch können die Daten, die du an mich
       übermittelst, nicht von Dritten mitgelesen werden.</p>

    <h2>7. Deine Rechte</h2>
    <p>Dir stehen gegenüber mir folgende Rechte hinsichtlich deiner personenbezogenen Daten zu:</p>
    <ul>
      <li><strong>Auskunft</strong> (Art.&nbsp;15 DSGVO) – welche Daten ich über dich verarbeite</li>
      <li><strong>Berichtigung</strong> (Art.&nbsp;16 DSGVO) – falsche Daten korrigieren lassen</li>
      <li><strong>Löschung</strong> (Art.&nbsp;17 DSGVO) – auch „Recht auf Vergessenwerden“</li>
      <li><strong>Einschränkung der Verarbeitung</strong> (Art.&nbsp;18 DSGVO)</li>
      <li><strong>Datenübertragbarkeit</strong> (Art.&nbsp;20 DSGVO)</li>
      <li><strong>Widerspruch</strong> gegen Verarbeitungen auf Grundlage berechtigter
          Interessen (Art.&nbsp;21 DSGVO)</li>
      <li><strong>Widerruf einer Einwilligung</strong> (Art.&nbsp;7 Abs.&nbsp;3 DSGVO) mit
          Wirkung für die Zukunft</li>
    </ul>
    <p>Für die Ausübung genügt eine formlose Nachricht an
       <a href="mailto:kontakt@grabensteinsales.de">kontakt@grabensteinsales.de</a>.</p>

    <h2>8. Beschwerderecht bei der Aufsichtsbehörde</h2>
    <p>Unabhängig davon steht dir das Recht zu, dich bei einer Datenschutz-Aufsichtsbehörde
       zu beschweren, insbesondere in dem Mitgliedstaat deines Aufenthaltsorts, deines
       Arbeitsplatzes oder des Orts des mutmaßlichen Verstoßes. Zuständig ist in der Regel
       die Aufsichtsbehörde des Bundeslandes, in dem ich meinen Sitz habe:
       <span class="todo">[Bundesland eintragen und die zuständige Landesdatenschutzbehörde
       mit Adresse und Website benennen]</span></p>

    <h2>9. Stand und Änderungen</h2>
    <p>Stand dieser Datenschutzerklärung: <span class="todo">[Monat und Jahr eintragen]</span>.
       Durch die Weiterentwicklung der Website oder geänderte gesetzliche Vorgaben kann eine
       Anpassung erforderlich werden. Die jeweils aktuelle Fassung findest du stets auf
       dieser Seite.</p>

  </div>
</section>
"""

# -------------------------------------------------------------------- AGB
agb_body = """
<section class="hero hero--sub">
  <div class="wrap hero__inner">
    <h1>Allgemeine Geschäftsbedingungen</h1>
    <p>Entwurf – bitte vor Veröffentlichung rechtlich prüfen lassen.</p>
  </div>
</section>

<section class="section">
  <div class="wrap prose">

    <div class="card" style="background:#FFF9E8; border-color:#E8D08A; margin-bottom:40px">
      <h3 style="margin-top:0">Hinweis an dich, Leon – diesen Kasten vor dem Livegang löschen</h3>
      <p>AGB sind <strong>nicht verpflichtend</strong>. Du hast drei Möglichkeiten:</p>
      <ol>
        <li>Diesen Entwurf von einer Anwältin oder einem Anwalt prüfen und anpassen lassen.</li>
        <li>Auf Website-AGB verzichten und die Bedingungen stattdessen direkt in dein
            Angebot bzw. den Beratungsvertrag schreiben. Dann den Link zu dieser Seite
            im Footer entfernen (steht in <code>_build/build.py</code> und in jeder
            HTML-Datei ganz unten).</li>
        <li>Den Entwurf vorerst so lassen – aber nur, solange du noch keine Kunden hast.</li>
      </ol>
      <p>Fehlerhafte AGB sind rechtlich riskanter als gar keine: unwirksame Klauseln können
         abgemahnt werden, und im Streitfall gilt dann ohnehin das Gesetz.</p>
    </div>

    <h2>§ 1 Geltungsbereich</h2>
    <p>Diese Allgemeinen Geschäftsbedingungen gelten für alle Verträge über Beratungs- und
       Dienstleistungen zwischen <span class="todo">[Name / Firmierung]</span>
       (nachfolgend „Auftragnehmer“) und dem Auftraggeber. Abweichende Bedingungen des
       Auftraggebers werden nur wirksam, wenn der Auftragnehmer ihnen ausdrücklich
       schriftlich zustimmt.</p>
    <p>Die Leistungen richten sich ausschließlich an Unternehmer im Sinne des § 14 BGB.
       <span class="todo">[Falls du auch an Verbraucher verkaufst: diesen Satz streichen –
       dann gelten deutlich strengere Vorgaben, unter anderem ein Widerrufsrecht und eine
       Widerrufsbelehrung. In dem Fall unbedingt anwaltlich prüfen lassen.]</span></p>

    <h2>§ 2 Vertragsschluss</h2>
    <p>Die Darstellung der Leistungen auf dieser Website stellt kein bindendes Angebot dar,
       sondern eine Aufforderung zur Abgabe eines Angebots. Ein Vertrag kommt erst durch ein
       schriftliches Angebot des Auftragnehmers und dessen Annahme durch den Auftraggeber
       in Textform zustande.</p>

    <h2>§ 3 Leistungsumfang</h2>
    <p>Der konkrete Umfang der Leistungen ergibt sich aus dem jeweiligen Angebot. Der
       Auftragnehmer erbringt Beratungsleistungen im Bereich Vertrieb. Es handelt sich um
       einen Dienstvertrag im Sinne der §§ 611 ff. BGB.</p>
    <p><strong>Es wird kein bestimmter wirtschaftlicher Erfolg geschuldet.</strong>
       Insbesondere schuldet der Auftragnehmer keine bestimmte Anzahl an Kunden,
       Abschlüssen oder eine bestimmte Umsatzentwicklung.</p>

    <h2>§ 4 Mitwirkungspflichten des Auftraggebers</h2>
    <p>Der Auftraggeber stellt dem Auftragnehmer alle zur Leistungserbringung erforderlichen
       Informationen, Unterlagen und Zugänge rechtzeitig und vollständig zur Verfügung.
       Verzögerungen, die auf fehlende Mitwirkung zurückgehen, verlängern die vereinbarten
       Fristen entsprechend.</p>

    <h2>§ 5 Vergütung und Zahlungsbedingungen</h2>
    <p>Die Vergütung ergibt sich aus dem jeweiligen Angebot.
       <span class="todo">[Bitte ergänzen: Zahlungsziel, z.&nbsp;B. „Rechnungen sind innerhalb
       von 14 Tagen ohne Abzug zahlbar.“ Sowie: Anzahlung? Ratenzahlung? Abrechnung nach
       Aufwand oder Festpreis?]</span></p>
    <p><span class="todo">[Falls Kleinunternehmer nach § 19 UStG: „Es wird keine Umsatzsteuer
       ausgewiesen.“ Andernfalls: „Alle Preise verstehen sich zuzüglich der gesetzlichen
       Umsatzsteuer.“]</span></p>

    <h2>§ 6 Laufzeit und Kündigung</h2>
    <p><span class="todo">[Bitte ergänzen: Laufzeit der Pakete, Kündigungsfristen,
       Regelung zu bereits erbrachten Leistungen bei vorzeitiger Beendigung.]</span></p>

    <h2>§ 7 Vertraulichkeit</h2>
    <p>Beide Parteien verpflichten sich, alle im Rahmen der Zusammenarbeit bekannt gewordenen
       Geschäfts- und Betriebsgeheimnisse vertraulich zu behandeln und nicht an Dritte
       weiterzugeben. Diese Pflicht besteht auch nach Beendigung des Vertragsverhältnisses
       fort.</p>

    <h2>§ 8 Nutzungsrechte</h2>
    <p>An den im Rahmen des Auftrags erstellten Arbeitsergebnissen erhält der Auftraggeber
       mit vollständiger Bezahlung der Vergütung ein einfaches, zeitlich und räumlich
       unbeschränktes Nutzungsrecht für eigene Zwecke.</p>

    <h2>§ 9 Haftung</h2>
    <p>Der Auftragnehmer haftet unbeschränkt bei Vorsatz und grober Fahrlässigkeit sowie
       bei der Verletzung von Leben, Körper oder Gesundheit. Bei einfacher Fahrlässigkeit
       haftet der Auftragnehmer nur bei Verletzung einer wesentlichen Vertragspflicht, deren
       Erfüllung die ordnungsgemäße Durchführung des Vertrages überhaupt erst ermöglicht und
       auf deren Einhaltung der Auftraggeber regelmäßig vertrauen darf. In diesem Fall ist
       die Haftung auf den vertragstypischen, vorhersehbaren Schaden begrenzt.</p>

    <h2>§ 10 Referenznennung</h2>
    <p>Der Auftragnehmer ist berechtigt, den Auftraggeber als Referenz zu nennen, sofern der
       Auftraggeber hierin ausdrücklich und in Textform eingewilligt hat. Die Einwilligung
       kann jederzeit für die Zukunft widerrufen werden.</p>

    <h2>§ 11 Schlussbestimmungen</h2>
    <p>Es gilt das Recht der Bundesrepublik Deutschland unter Ausschluss des UN-Kaufrechts.
       Sofern der Auftraggeber Kaufmann, juristische Person des öffentlichen Rechts oder
       öffentlich-rechtliches Sondervermögen ist, ist Gerichtsstand
       <span class="todo">[Ort eintragen]</span>.</p>
    <p>Sollten einzelne Bestimmungen dieser AGB unwirksam sein oder werden, bleibt die
       Wirksamkeit der übrigen Bestimmungen unberührt.</p>

    <p style="margin-top:2.5em; color:var(--c-muted)">
       Stand: <span class="todo">[Monat und Jahr eintragen]</span></p>

  </div>
</section>
"""

# =====================================================================
#  DEINE DATEN – hier zentral gepflegt
# =====================================================================
NAME       = "Leon Grabenstein"
STRASSE    = "Niedertorstr. 32"
PLZ_ORT    = "32312 Lübbecke"
EMAIL      = "grabenstein.sales@outlook.com"
TEL_TEXT   = "0177 1748147"
TEL_LINK   = "+491771748147"
STAND      = "September 2026"
GERICHTSST = "Lübbecke"

MAIL_A = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
TEL_A  = f'<a href="tel:{TEL_LINK}">{TEL_TEXT}</a>'

# --- Impressum, fertig ausgefuellt (Kleinunternehmer nach § 19 UStG) ---
impressum_body = f"""
<section class="hero hero--sub">
  <div class="wrap hero__inner"><h1>Impressum</h1></div>
</section>

<section class="section">
  <div class="wrap prose">

    <h2>Angaben gemäß § 5 DDG</h2>
    <address>
      {NAME}<br>
      Grabenstein Sales<br>
      {STRASSE}<br>
      {PLZ_ORT}<br>
      Deutschland
    </address>

    <h2>Kontakt</h2>
    <p>
      Telefon: {TEL_A}<br>
      E-Mail: {MAIL_A}
    </p>

    <h2>Umsatzsteuer</h2>
    <p>Gemäß § 19 UStG wird keine Umsatzsteuer berechnet und daher auch nicht ausgewiesen
       (Kleinunternehmerregelung).</p>

    <h2>Redaktionell verantwortlich</h2>
    <address>
      {NAME}<br>
      {STRASSE}<br>
      {PLZ_ORT}
    </address>

    <h2>Verbraucherstreitbeilegung</h2>
    <p>Ich bin nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer
       Verbraucherschlichtungsstelle teilzunehmen.</p>

    <h2>Haftung für Inhalte</h2>
    <p>Als Diensteanbieter bin ich gemäß § 7 Abs. 1 DDG für eigene Inhalte auf diesen Seiten
       nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 DDG bin ich als
       Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde
       Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige
       Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von
       Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine
       diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten
       Rechtsverletzung möglich. Bei Bekanntwerden entsprechender Rechtsverletzungen werde
       ich diese Inhalte umgehend entfernen.</p>

    <h2>Haftung für Links</h2>
    <p>Mein Angebot enthält gegebenenfalls Links zu externen Websites Dritter, auf deren
       Inhalte ich keinen Einfluss habe. Deshalb kann ich für diese fremden Inhalte auch
       keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige
       Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum
       Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft; rechtswidrige Inhalte
       waren zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente inhaltliche
       Kontrolle der verlinkten Seiten ist ohne konkrete Anhaltspunkte einer Rechtsverletzung
       nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werde ich derartige Links
       umgehend entfernen.</p>

    <h2>Urheberrecht</h2>
    <p>Die durch den Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten
       unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung,
       Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechts
       bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.
       Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen
       Gebrauch gestattet.</p>

  </div>
</section>
"""

# --- Datenschutz: Verantwortlichen, Aufsichtsbehoerde und Stand einsetzen ---
datenschutz_body = datenschutz_body.replace(
    """    <address>
      <span class="todo">[Vollständiger Name]</span><br>
      <span class="todo">[Straße und Hausnummer]</span><br>
      <span class="todo">[PLZ und Ort]</span><br>
      Deutschland<br>
      E-Mail: <a href="mailto:kontakt@grabensteinsales.de">kontakt@grabensteinsales.de</a><br>
      Telefon: <span class="todo">[Telefonnummer]</span>
    </address>""",
    f"""    <address>
      {NAME}<br>
      Grabenstein Sales<br>
      {STRASSE}<br>
      {PLZ_ORT}<br>
      Deutschland<br>
      E-Mail: {MAIL_A}<br>
      Telefon: {TEL_A}
    </address>"""
).replace(
    """       die Aufsichtsbehörde des Bundeslandes, in dem ich meinen Sitz habe:
       <span class="todo">[Bundesland eintragen und die zuständige Landesdatenschutzbehörde
       mit Adresse und Website benennen]</span></p>""",
    """       die Aufsichtsbehörde des Bundeslandes, in dem ich meinen Sitz habe. Für
       Nordrhein-Westfalen ist das:</p>
    <address>
      Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen<br>
      Postfach 20 04 44<br>
      40102 Düsseldorf<br>
      Telefon: <a href="tel:+4921138424 0">0211 38424-0</a><br>
      Website: <a href="https://www.ldi.nrw.de" rel="noopener">www.ldi.nrw.de</a>
    </address>"""
).replace(
    '<span class="todo">[Monat und Jahr eintragen]</span>', STAND
)

# --- AGB: Name, Kleinunternehmerregelung und Gerichtsstand einsetzen ---
agb_body = agb_body.replace(
    '<span class="todo">[Name / Firmierung]</span>',
    f"{NAME}, Grabenstein Sales,"
).replace(
    """    <p><span class="todo">[Falls Kleinunternehmer nach § 19 UStG: „Es wird keine Umsatzsteuer
       ausgewiesen.“ Andernfalls: „Alle Preise verstehen sich zuzüglich der gesetzlichen
       Umsatzsteuer.“]</span></p>""",
    """    <p>Der Auftragnehmer ist Kleinunternehmer im Sinne des § 19 UStG. Es wird daher keine
       Umsatzsteuer berechnet und in Rechnungen nicht ausgewiesen.</p>"""
).replace(
    '<span class="todo">[Ort eintragen]</span>', GERICHTSST
).replace(
    '<span class="todo">[Monat und Jahr eintragen]</span>', STAND
)

# --- E-Mail und Telefon auf allen Seiten vereinheitlichen ---
def personalisieren(text):
    return (text
        .replace('<a href="mailto:kontakt@grabensteinsales.de">kontakt@grabensteinsales.de</a>', MAIL_A)
        .replace('kontakt@grabensteinsales.de', EMAIL)
        .replace('<span class="todo">[Telefonnummer ergänzen]</span>', TEL_A)
        .replace('<span class="todo">[Telefonnummer]</span>', TEL_A))

# Auch im Angebot-Entwurf bleibt der USt-Hinweis sonst falsch stehen
angebot_body = angebot_body.replace(
    '<small>zzgl. USt., falls zutreffend</small>',
    '<small>keine USt. (Kleinunternehmer nach § 19 UStG)</small>')

# =====================================================================
#  SEITEN SCHREIBEN
# =====================================================================
_page_roh = page
def page(filename, title, desc, body, extra_head="", extra_js=""):
    """Wie oben, aber mit eingesetzten Kontaktdaten."""
    html = head(title, desc, filename).replace("</head>", extra_head + "</head>") \
         + nav() \
         + f'<main id="main">\n{body}\n</main>\n' \
         + footer().replace("</body>", extra_js + "</body>")
    (OUT / filename).write_text(personalisieren(html), encoding="utf-8")
    print(f"  geschrieben: {filename}")


if __name__ == "__main__":
    print("Baue grabensteinsales.de …")

    page("index.html", "Vertrieb für Startups",
         "Grabenstein Sales begleitet junge Unternehmen beim Aufbau ihres Vertriebs – "
         "von den ersten Kunden bis zu einer Struktur, die trägt.",
         index_body)

    page("ueber-uns.html", "Über mich",
         "Leon Grabenstein über seinen Werdegang, seine Haltung und die Art, "
         "wie er mit Startups am Vertrieb arbeitet.",
         ueber_body)

    page("angebot.html", "Leistungen",
         "Basic und Plus Paket: zwei Wege, den Vertrieb deines Startups gemeinsam "
         "aufzubauen – vom kompakten Einstieg bis zur längeren Begleitung.",
         angebot_body)

    page("ablauf.html", "So arbeite ich",
         "Zuhören, einordnen, umsetzen, übergeben: der Ablauf einer Zusammenarbeit "
         "mit Grabenstein Sales in vier Schritten.",
         ablauf_body)

    page("kontakt.html", "Kontakt",
         "Schreib Leon Grabenstein eine Nachricht oder ruf direkt an. "
         "Das erste Gespräch ist kostenlos und unverbindlich.",
         kontakt_body, extra_js=KONTAKT_JS)

    page("impressum.html", "Impressum",
         "Anbieterkennzeichnung gemäß § 5 DDG für grabensteinsales.de.",
         impressum_body)

    page("datenschutz.html", "Datenschutzerklärung",
         "Wie auf grabensteinsales.de mit personenbezogenen Daten umgegangen wird: "
         "keine Cookies, kein Tracking, keine Dienste von Dritten beim Seitenaufruf.",
         datenschutz_body)

    page("agb.html", "AGB",
         "Allgemeine Geschäftsbedingungen von Grabenstein Sales.",
         agb_body)

    # Alte Adressen weiterleiten, damit vorhandene Links nicht ins Leere laufen
    redirect("startseite.html", "index.html", "Startseite")
    redirect("referenzen.html", "ablauf.html", "So arbeite ich")

    # 404-Seite
    (OUT / "404.html").write_text(personalisieren(
        head("Seite nicht gefunden", "Diese Seite gibt es nicht (mehr).", "404.html")
        + nav()
        + """<main id="main">
<section class="section" style="text-align:center">
  <div class="wrap">
    <span class="eyebrow">Fehler 404</span>
    <h1>Diese Seite gibt es nicht</h1>
    <p class="lead" style="max-width:52ch;margin:0 auto 32px">
      Der Link ist vermutlich veraltet oder es hat sich ein Tippfehler eingeschlichen.</p>
    <a class="btn btn--primary" href="index.html">Zur Startseite</a>
  </div>
</section>
</main>
"""
        + footer()), encoding="utf-8")
    print("  geschrieben: 404.html")

    # robots.txt und sitemap.xml fuer Suchmaschinen
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print("  geschrieben: robots.txt")

    seiten = ["index.html", "ueber-uns.html", "angebot.html", "ablauf.html",
              "kontakt.html", "impressum.html", "datenschutz.html", "agb.html"]
    eintraege = "\n".join(
        f"  <url><loc>{SITE}/{s}</loc>"
        f"<priority>{'1.0' if s == 'index.html' else '0.8' if s in ('angebot.html','kontakt.html') else '0.5'}</priority></url>"
        for s in seiten)
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{eintraege}\n</urlset>\n", encoding="utf-8")
    print("  geschrieben: sitemap.xml")

    print("Fertig.")
