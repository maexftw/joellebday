# Graph Report - .  (2026-07-24)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 81 nodes · 132 edges · 9 communities (8 shown, 1 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Zehn-Folien-Geburtstagskarte
- Joelles digitale Geburtstagskarte
- app.js
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
- `Cloudflare Pages Deployment` --semantically_similar_to--> `Cloudflare Pages Direct Upload`  [INFERRED] [semantically similar]
  README.md → PROJECT_HANDOFF.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Digitale Geschenk-Erfahrung** — project_handoff_digitale_geburtstagskarte, project_handoff_vollbildfolien_praesentation, project_handoff_wallpaper_galerie, project_handoff_spassbudget [EXTRACTED 1.00]
- **Statische Auslieferung ohne Build-Schritt** — project_handoff_frameworkfreie_statische_website, project_handoff_cloudflare_pages_direct_upload, project_handoff_noindex_privatsphaere [EXTRACTED 1.00]

## Communities (9 total, 1 thin omitted)

### Community 0 - "Zehn-Folien-Geburtstagskarte"
Cohesion: 0.13
Nodes (20): Identitätserhaltender 9:20-Workflow, Neue Wallpaper-Sammlung, Quellfoto-Provenienz der zehn Motive, Finale Wallpaper-Prompts, Knautschnase, Schneetag und Kopf über, Skeptischer Mila-Blick, Folie 5: Hüpfen, Lachen, Leckerli, Folie 8: Geburtstagsgruß (+12 more)

### Community 1 - "Joelles digitale Geburtstagskarte"
Cohesion: 0.14
Nodes (17): Barrierefreiheitsgrundlagen, Cloudflare Pages Direct Upload, Joelles digitale Geburtstagskarte, Frameworkfreie statische Website, Gemeinsame Freude im eigenen Tempo, Graphify als Navigations- und Übergabeschicht, Immutable Asset-Caching mit neuen Dateinamen, Öffentlich erreichbar, aber nicht für Suchmaschinen (+9 more)

### Community 2 - "app.js"
Cohesion: 0.16
Nodes (14): clamp(), deck, initialSlide, move(), nextButtons, prefersReducedMotion, prevButtons, progressBar (+6 more)

### Community 3 - "build_card.py"
Cohesion: 0.57
Nodes (6): build_pdf(), build_preview(), prepare_photo(), register_fonts(), rounded_paste(), Path

### Community 4 - "Canvas"
Cohesion: 0.67
Nodes (6): draw_back_cover_upright(), draw_inside_bottom(), draw_money_area(), draw_qr(), draw_svg_icon(), Canvas

### Community 5 - "draw_inside_page"
Cohesion: 0.53
Nodes (6): draw_cover(), draw_fold_ticks(), draw_inside_page(), draw_outer_page(), draw_rounded_photo(), Image

### Community 6 - "draw_inside_top"
Cohesion: 0.67
Nodes (4): draw_inside_top(), draw_paragraph(), draw_speech_bubble(), ParagraphStyle

### Community 7 - "verify_site.mjs"
Cohesion: 0.50
Nodes (3): assets, root, site

## Knowledge Gaps
- **23 isolated node(s):** `slides`, `prevButtons`, `nextButtons`, `progressNumber`, `progressTitle` (+18 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `slides`, `prevButtons`, `nextButtons` to the rest of the system?**
  _23 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Zehn-Folien-Geburtstagskarte` be split into smaller, more focused modules?**
  _Cohesion score 0.13157894736842105 - nodes in this community are weakly interconnected._
- **Should `Joelles digitale Geburtstagskarte` be split into smaller, more focused modules?**
  _Cohesion score 0.13970588235294118 - nodes in this community are weakly interconnected._