# Projekt-Handoff: Joelles digitale Geburtstagskarte

Stand: 24. Juli 2026

## Zweck und aktueller Status

Dieses Projekt ist eine private, deutschsprachige digitale Geburtstagskarte für
Joelle und ihren Hund Mila. Die produktive Seite ist öffentlich erreichbar,
aber absichtlich nicht für Suchmaschinen gedacht:

- Geburtstagskarte: https://joelle-mila-geburtstag.pages.dev/
- Wallpaper-Galerie: https://joelle-mila-geburtstag.pages.dev/wallpapers
- GitHub-Repository: https://github.com/maexftw/joellebday
- Cloudflare-Pages-Projekt: `joelle-mila-geburtstag`
- Cloudflare-Git-Projekt: `joellebday`
- Deploy-Root: `site/`
- Es gibt bewusst keinen Build-Schritt.

Das Geschenk ist Geld als flexibles „Spaßbudget“ für gemeinsame Agility-Zeit.
Es wurde kein Termin und kein Trainer gebucht, kein Betrag wird angezeigt und
Joelle sucht den Termin selbst aus. Der externe Buchungslink ist:
https://hsz-luenen-brambauer.de/buchen/

Die Botschaft ist gemeinsame Freude in eigenem Tempo. Sie darf nicht als
Turnier-, Leistungs-, Erfolgs- oder „nächstes Level“-Botschaft umgedeutet
werden. Der aktuelle Geburtstagsgruß lautet exakt:
`Jutta, Manny, Maxi und Benny.`

## Was produktiv läuft

`site/` ist eine vollständig statische, frameworkfreie Website. Sie benötigt
zur Laufzeit nur HTML, CSS, JavaScript und die lokalen Bilddateien.

### Präsentation

`site/index.html` enthält neun Vollbildfolien:

1. Digitale Geburtstagskarte
2. Offizielle Umweltschutz-Begründung
3. Inoffizielle Drucker-Begründung mit skeptischer Mila
4. Qualitätskontrolle durch Mila
5. Agility: Hüpfen, Lachen, Leckerli
6. Spaß und eigenes Tempo
7. Geldgeschenk als Spaßbudget mit externem Buchungslink
8. Geburtstagsgruß von Jutta, Manny, Maxi und Benny
9. Konsolidierte Wallpaper-Übersicht mit Handy-/Laptop-Vorschau und Link zur vollständigen Galerie

`site/app.js` verwaltet genau einen aktuellen Folienindex. `showSlide()`:

- begrenzt den Index auf vorhandene Folien,
- setzt `.is-active`, `aria-hidden` und `inert`,
- aktualisiert Fortschritt, Titel, Live-Status und URL-Hash,
- startet den farbigen Wipe-Übergang,
- baut Bilder und Texte danach in einer gestaffelten Reihenfolge auf,
- setzt versehentliche Scrollpositionen zurück.

Navigation funktioniert über Vor/Zurück-Buttons, Pfeiltasten,
PageUp/PageDown, Leertaste, Home/End, horizontales Wischen ab 48 Pixeln und
direkte Hash-Links wie `#slide-gift`. Bei `prefers-reduced-motion: reduce`
werden die aufwendigen Animationen praktisch deaktiviert.

`site/styles.css` enthält das komplette Design:

- Creme, Waldgrün und warmes Gold
- Editorial-/Bilderbuch-Anmutung
- dreifarbiger Slide-Wipe und gestaffelte Inhaltsanimationen
- Desktop-, Tablet-, Handy- und kurze-Handy-Layouts
- separate Styles für die scrollbare Wallpaper-Galerie

### Wallpaper-Galerie

`site/wallpapers.html` ist die zentrale, JavaScript-freie und responsive Downloadseite mit
15 Karten:

- 14 gleichwertige Handy-Wallpaper in einem gemeinsamen Raster
- 1 Laptop-Wallpaper mit 16:9- und 16:10-Download
- Originalfoto-Varianten direkt bei „Waldmärchen“ und „Hürdenpause“

Der Downloadbereich hat bewusst nur zwei Oberflächen: Folie 9 als kompakte Übersicht
mit einem eindeutigen Galerie-CTA und diese Seite als einzigen Ort für alle einzelnen
Downloads. Die Galerie verlinkt zurück auf Folie 9. Auf dem Handy nutzt sie zwei
Spalten, auf größeren Ansichten drei beziehungsweise fünf.

## Dateistruktur und Quellen der Wahrheit

- `site/index.html` – Text, Folienreihenfolge und produktive Verlinkungen
- `site/styles.css` – gesamtes visuelles und responsives System
- `site/app.js` – Folienzustand und Eingabesteuerung
- `site/wallpapers.html` – vollständiger Wallpaper-Schrank
- `site/_headers` – Cloudflare-Sicherheits- und Cache-Header
- `site/assets/photos/` – kleine produktive Vorschauen
- `site/assets/icons/` – lokale Icons samt Lizenz
- `site/downloads/` – öffentlich herunterladbare hochauflösende Dateien
- `verify_site.mjs` – kleinster ausführbarer Integritätscheck
- `output/generated/PROMPTS.md` – ältere Bildprompts und skeptische Mila
- `output/generated/new-wallpapers/PROMPTS.md` – exakte Prompts und
  Quellzuordnung der zehn neuen Motive
- `output/generated/new-wallpapers/*-source.png` – bearbeitbare
  image-gen-Quellen, nicht Teil der Website
- JPEG-Dateien im Projektstamm – private Originalfotos, nicht deployt
- `build_card.py` – ältere druckbare A4-Kartenvariante; nicht Teil der Website
- `graphify-out/` – generierter Wissensgraph für KI-Navigation

Für Änderungen an der Website sind `site/` und dieser Handoff maßgeblich.
`output/` enthält Herkunfts- und QA-Artefakte, aber keinen zweiten
Website-Quellstand.

## Bild- und Wallpaper-Workflow

Der bisherige Workflow für ein neues Handy-Wallpaper:

1. Privates Quell-JPEG im Projektstamm visuell prüfen.
2. Mit dem eingebauten Bildgenerator und einem markenunabhängigen Prompt
   bearbeiten.
3. Identität, Fellzeichnung, Beziehung und natürliche Körperform erhalten.
4. Keine Markenstile, Schrift, Logos, Wasserzeichen oder zusätzlichen Figuren.
5. Für die Handy-Uhr das obere Viertel ruhig und detailarm halten.
6. Generierte 9:20-Quelle mit 841 × 1870 Pixeln unter
   `output/generated/new-wallpapers/` ablegen.
7. Vorschau als 540 × 1200 WebP nach `site/assets/photos/` exportieren.
8. Download als 1440 × 3200 JPEG nach `site/downloads/` exportieren.
9. Vorschau und Download in `site/wallpapers.html` verlinken.
10. `node verify_site.mjs` und anschließend Browser-QA ausführen.

Bestehende Laptop-Downloads liegen in 2560 × 1440 und 2560 × 1600 vor.
Es gibt keinen automatischen Bild-Build. Die exakten Prompts bleiben deshalb
als Provenienz in den beiden `PROMPTS.md`-Dateien erhalten.

Wichtig: `/assets/*` und `/downloads/*` werden ein Jahr lang als `immutable`
gecacht. Wird eine Binärdatei sichtbar verändert, sollte sie einen neuen
Dateinamen bekommen; nur dieselbe Datei zu überschreiben kann alte CDN- oder
Browser-Caches stehen lassen.

## Prüfung

Minimaler lokaler Check:

```powershell
node --check site\app.js
node verify_site.mjs
```

Erwarteter Kernoutput:

```text
OK: 9 Folien, 62 lokale Assets, Übergänge und Texte geprüft.
```

Der Check sichert aktuell ab:

- exakt 9 Folien,
- den Namen `Manny` und `Benny`,
- das skeptische Mila-Bild,
- Wipe-Animation, 53 gestaffelte Reveal-Marker und Reduced-Motion-Fallback,
- genau einen Galerie-CTA in der konsolidierten Wallpaper-Folie,
- keine einzelnen Downloadlinks mehr innerhalb der Präsentation,
- 15 Galerie-Karten, ihre Gruppierung als 14 Handy- plus 1 Laptop-Motiv und beide Originalfoto-Varianten,
- Rücklinks der Galerie auf Folie 9,
- Existenz aller in HTML referenzierten lokalen Assets.

Die letzte Browser-QA wurde bei 1440 × 900, 768 × 1024, 390 × 844 und
320 × 568 durchgeführt. Dabei gab es keine horizontalen Überläufe, keine kaputten
Bilder und keine Browserkonsolen-, Page- oder Requestfehler. Der Galerie-CTA und die
Downloadziele sind mindestens 44 Pixel hoch; auch die kurze 320-Pixel-Ansicht hält
34 Pixel Abstand zwischen den Vorschaukarten und der unteren Navigation.

## Deployment

Das öffentliche GitHub-Repository enthält nur den deploybaren Webstand,
Handoff, Prüfroutine, Prompt-Provenienz und die kleinen Graphify-Artefakte.
Private Originalfotos, iCloud-Exporte, generierte Bildquellen, QA-Artefakte
und Caches werden durch eine strikte `.gitignore`-Allowlist ausgeschlossen.

Das bestehende Cloudflare-Pages-Projekt ist ein Direct-Upload-Projekt. Die
Seite wird ohne Build direkt aus `site/` hochgeladen:

```powershell
npx --yes wrangler@4.114.0 whoami
npx --yes wrangler@4.114.0 pages deploy site --project-name joelle-mila-geburtstag --branch main
```

Zusätzlich ist das GitHub-Repository nativ mit dem Cloudflare-Pages-Projekt
`joellebday` verbunden. Pushes auf `main` werden ohne Build-Befehl direkt aus
dem Ausgabeverzeichnis `site` veröffentlicht:
https://joellebday.pages.dev/

Das zusätzliche Git-Projekt ist absichtlich nicht an die Stelle der
bestehenden Direct-Upload-Produktion getreten. Cloudflare kann ein bestehendes
Direct-Upload-Projekt nicht nachträglich auf native Git-Integration umstellen;
die bisherige produktive URL bleibt dadurch unangetastet.

Nach dem Deploy müssen mindestens geprüft werden:

- Produktions-Root lädt die neun Folien.
- Der Gruß enthält `Jutta, Manny, Maxi und Benny.`
- `/wallpapers` zeigt 15 Karten und die Originalfoto-Varianten.
- Der konsolidierte CTA auf Folie 9 öffnet die zentrale Galerie.
- Ein JPEG-Download liefert HTTP 200 und `image/jpeg`.
- Handyansicht hat keinen horizontalen Überlauf.

`site/_headers` setzt `nosniff`, eine strikte Referrer-Policy, deaktiviert
Kamera/Mikrofon/Geolocation, verhindert Framing und setzt
`noindex, nofollow, noarchive`.

## Bewusste Nicht-Ziele

Es gibt keinen Backenddienst, keine Datenbank, keine Anmeldung, keine
Analytics, keine Zahlung, keine Buchungs-API und keinen gespeicherten
Geldbetrag. Die Website verlinkt ausschließlich auf die externe Buchungsseite.

Barrierefreiheitsgrundlagen sind beabsichtigt und sollen erhalten bleiben:
Skip-Link, semantische Buttons, Tastaturbedienung, Wischbedienung,
ARIA-Beschriftungen, Live-Status, `inert` für inaktive Folien, Alt-Texte und
Reduced-Motion-Unterstützung.

## Graphify für die nächste KI

`.graphifyignore` schließt Binärbilder, PDFs, ZIPs und QA-Duplikate aus. Die
Dateinamen und Beziehungen der produktiven Bilder bleiben über HTML,
Prompt-Provenienz und diesen Handoff im Graphen sichtbar, ohne 187 fast
inhaltgleiche Bildknoten zu erzeugen.

Nach einer dauerhaften Änderung an Code, Texten, Prompts oder diesem Handoff:

```powershell
graphify update .
```

Danach Manifest-Freshness, Graph-Gesundheit und mindestens eine gezielte
`graphify query` prüfen. Der Graph ist eine Navigations- und Übergabeschicht;
die oben genannten Quelldateien bleiben die Wahrheit.
