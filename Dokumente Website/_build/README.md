# Hinweise zum Aufbau der Website

## Normale Änderungen
Bearbeite einfach die HTML-Dateien im Hauptordner. Fertig.

## Änderungen an Navigation oder Fußzeile
Die stehen in **jeder** HTML-Datei drin. Damit sie überall gleich bleiben,
gibt es `build.py`:

    python3 _build/build.py

Das Skript schreibt alle Seiten neu aus einer gemeinsamen Vorlage.
**Achtung:** Dabei gehen Änderungen verloren, die du direkt in den
HTML-Dateien gemacht hast. Entweder du arbeitest nur in `build.py`,
oder nur in den HTML-Dateien – nicht gemischt.

Der Ordner `_build` beginnt mit einem Unterstrich und wird von
GitHub Pages deshalb nicht veröffentlicht.

## Noch zu erledigen
Alle offenen Stellen sind auf der Website **gelb markiert**.
Suche im Code nach `class="todo"`, um sie zu finden.
