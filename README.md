# Joelles digitale Geburtstagskarte

Frameworkfreie, statische Geburtstagskarte mit zehn Vollbildfolien und einer
Wallpaper-Galerie für Joelle und Mila.

- Produktion: <https://joelle-mila-geburtstag.pages.dev/>
- Wallpaper: <https://joelle-mila-geburtstag.pages.dev/wallpapers>
- Git-Deployment: <https://joellebday.pages.dev/>
- Deploy-Root: `site/`
- Build-Schritt: keiner

## Lokal prüfen

```powershell
node --check site\app.js
node verify_site.mjs
```

Erwartet:

```text
OK: 10 Folien, 71 lokale Assets, Übergänge und Texte geprüft.
```

## Cloudflare Pages

`main` ist nativ mit dem Cloudflare-Pages-Projekt `joellebday` verbunden.
Cloudflare veröffentlicht Pushes automatisch aus `site/`.

Das bestehende Projekt `joelle-mila-geburtstag` bleibt als stabile
Direct-Upload-Produktion erhalten und kann bei Bedarf manuell aktualisiert
werden:

```powershell
npx --yes wrangler@4.114.0 pages deploy site --project-name joelle-mila-geburtstag --branch main
```

Der vollständige Projektstand, die inhaltlichen Leitplanken und die
Abnahme-Checks stehen in [PROJECT_HANDOFF.md](PROJECT_HANDOFF.md).

Dieses öffentliche Repository enthält nur den Webstand und seine
Provenienz. Private Originalfotos, iCloud-Exporte und lokale QA-Artefakte
sind absichtlich ausgeschlossen.
