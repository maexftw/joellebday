# Graph Report - .  (2026-07-24)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 89 nodes · 142 edges · 10 communities (9 shown, 1 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f00d1e4b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Zehn-Folien-Geburtstagskarte
- app.js
- Joelles digitale Geburtstagskarte
- Automatisches GitHub-main-Deployment
- build_card.py
- Canvas
- draw_inside_page
- draw_inside_top
- verify_site.mjs
- Lucide Icons ISC License

## God Nodes (most connected - your core abstractions)
1. `Zehn-Folien-Geburtstagskarte` - 10 edges
2. `draw_inside_top()` - 9 edges
3. `draw_svg_icon()` - 7 edges
4. `draw_outer_page()` - 7 edges
5. `draw_inside_page()` - 7 edges
6. `build_pdf()` - 7 edges
7. `Joelles digitale Geburtstagskarte` - 7 edges
8. `draw_inside_bottom()` - 6 edges
9. `draw_rounded_photo()` - 5 edges
10. `draw_cover()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Lucide Icons ISC License` --semantically_similar_to--> `Produktive Lucide Icons ISC License`  [INFERRED] [semantically similar]
  assets/lucide/LICENSE.txt → site/assets/icons/LICENSE.txt
- `Folie 3: Inoffizielle Drucker-Begründung` --semantically_similar_to--> `Skeptischer Mila-Blick`  [INFERRED] [semantically similar]
  site/index.html → output/generated/PROMPTS.md
- `Neue Sammlung mit 10 Handy-Wallpapern` --semantically_similar_to--> `Neue Wallpaper-Sammlung`  [INFERRED] [semantically similar]
  site/wallpapers.html → output/generated/new-wallpapers/PROMPTS.md
- `Frameworkfreie statische Geburtstagskarte` --semantically_similar_to--> `Joelles digitale Geburtstagskarte`  [INFERRED] [semantically similar]
  README.md → PROJECT_HANDOFF.md
- `Automatische Veröffentlichung von main` --semantically_similar_to--> `Automatisches GitHub-main-Deployment`  [INFERRED] [semantically similar]
  README.md → PROJECT_HANDOFF.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Native Git deployment path** — project_handoff_github_repository_joellebday, project_handoff_main_branch, project_handoff_automatic_git_deployment, project_handoff_site_output_directory [EXTRACTED 1.00]
- **Git deployment plus preserved Direct Upload production** — project_handoff_cloudflare_direct_upload_project, project_handoff_direct_upload_production_preservation [EXTRACTED 1.00]
- **Digitale Geschenk-Erfahrung** — project_handoff_digitale_geburtstagskarte, project_handoff_vollbildfolien_praesentation, project_handoff_wallpaper_galerie, project_handoff_spassbudget [EXTRACTED 1.00]

## Communities (10 total, 1 thin omitted)

### Community 0 - "Zehn-Folien-Geburtstagskarte"
Cohesion: 0.13
Nodes (20): Identitätserhaltender 9:20-Workflow, Neue Wallpaper-Sammlung, Quellfoto-Provenienz der zehn Motive, Finale Wallpaper-Prompts, Knautschnase, Schneetag und Kopf über, Skeptischer Mila-Blick, Folie 5: Hüpfen, Lachen, Leckerli, Folie 8: Geburtstagsgruß (+12 more)

### Community 1 - "app.js"
Cohesion: 0.16
Nodes (14): clamp(), deck, initialSlide, move(), nextButtons, prefersReducedMotion, prevButtons, progressBar (+6 more)

### Community 2 - "Joelles digitale Geburtstagskarte"
Cohesion: 0.15
Nodes (14): Barrierefreiheitsgrundlagen, Joelles digitale Geburtstagskarte, Gemeinsame Freude im eigenen Tempo, Graphify als Navigations- und Übergabeschicht, Immutable Asset-Caching mit neuen Dateinamen, Öffentlich erreichbar, aber nicht für Suchmaschinen, Projekt-Handoff: Joelles digitale Geburtstagskarte, Spaßbudget für gemeinsame Agility-Zeit (+6 more)

### Community 3 - "Automatisches GitHub-main-Deployment"
Cohesion: 0.25
Nodes (11): Automatisches GitHub-main-Deployment, Cloudflare Pages Direct-Upload-Projekt joelle-mila-geburtstag, Bestehende Direct-Upload-Produktion bleibt unangetastet, Frameworkfreie statische Website ohne Build-Schritt, GitHub-Repository maexftw/joellebday, GitHub main Branch, Cloudflare-Ausgabeverzeichnis site, Cloudflare Pages Projekt joellebday (+3 more)

### Community 4 - "build_card.py"
Cohesion: 0.57
Nodes (6): build_pdf(), build_preview(), prepare_photo(), register_fonts(), rounded_paste(), Path

### Community 5 - "Canvas"
Cohesion: 0.67
Nodes (6): draw_back_cover_upright(), draw_inside_bottom(), draw_money_area(), draw_qr(), draw_svg_icon(), Canvas

### Community 6 - "draw_inside_page"
Cohesion: 0.53
Nodes (6): draw_cover(), draw_fold_ticks(), draw_inside_page(), draw_outer_page(), draw_rounded_photo(), Image

### Community 7 - "draw_inside_top"
Cohesion: 0.67
Nodes (4): draw_inside_top(), draw_paragraph(), draw_speech_bubble(), ParagraphStyle

### Community 8 - "verify_site.mjs"
Cohesion: 0.50
Nodes (3): assets, root, site

## Knowledge Gaps
- **25 isolated node(s):** `slides`, `prevButtons`, `nextButtons`, `progressNumber`, `progressTitle` (+20 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Joelles digitale Geburtstagskarte` connect `Joelles digitale Geburtstagskarte` to `Automatisches GitHub-main-Deployment`?**
  _High betweenness centrality (0.054) - this node is a cross-community bridge._
- **Why does `Frameworkfreie statische Website ohne Build-Schritt` connect `Automatisches GitHub-main-Deployment` to `Joelles digitale Geburtstagskarte`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **What connects `slides`, `prevButtons`, `nextButtons` to the rest of the system?**
  _25 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Zehn-Folien-Geburtstagskarte` be split into smaller, more focused modules?**
  _Cohesion score 0.13157894736842105 - nodes in this community are weakly interconnected._