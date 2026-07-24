import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(fileURLToPath(import.meta.url));
const site = join(root, "site");
const [html, gallery, css, js] = await Promise.all([
  readFile(join(site, "index.html"), "utf8"),
  readFile(join(site, "wallpapers.html"), "utf8"),
  readFile(join(site, "styles.css"), "utf8"),
  readFile(join(site, "app.js"), "utf8"),
]);

assert.equal((html.match(/<section class="slide /g) ?? []).length, 9);
assert.match(html, /Jutta, Manny, Maxi und Benny\./);
assert.doesNotMatch(html, /Einfach ihr zwei\.|Einfach alle vier\.|Einfach mit Spaß\./);
assert.match(html, /Auf zum Agility\./);
assert.match(html, /Natürlich zu viert\./);
assert.match(html, /Jutta und Maxi fahren mit\./);
assert.match(html, /Ein Geldgeschenk als/);
assert.doesNotMatch(html, /Ein Geldgeschenk für/);
assert.match(html, /mila-road-skeptical\.webp/);
assert.doesNotMatch(html, /id="slide-more-wallpapers"/);
assert.equal((html.match(/href="wallpapers\.html"/g) ?? []).length, 1);
const wallpaperSlide = html.match(/<section class="slide slide--wallpapers"[\s\S]*?<\/section>/)?.[0] ?? "";
assert.match(wallpaperSlide, /Alle 15 Wallpaper öffnen/);
assert.doesNotMatch(wallpaperSlide, /\sdownload(?:>|\s)/);
assert.match(css, /@keyframes deck-wipe/);
assert.match(css, /@media \(prefers-reduced-motion: reduce\)/);
assert.match(css, /html:not\(\.motion-forced\) \*/);
assert.match(css, /\.motion-control-visible \.deck-nav/);
assert.match(css, /\.slide\.is-revealed \[data-reveal\]/);
assert.match(html, /<nav class="deck-nav"[\s\S]*?data-motion-toggle[\s\S]*?data-prev/);
assert.match(js, /deck\.classList\.add\("is-wiping"\)/);
assert.match(js, /function stageSlideReveal/);
assert.match(js, /motionStorageKey = "joellebday-motion"/);
assert.match(js, /classList\.toggle\("motion-forced"/);
assert.match(js, /classList\.toggle\("motion-control-visible"/);
assert.match(js, /prefersReducedMotion\.addEventListener\("change"/);
assert.match(js, /#slide-more-wallpapers.+#slide-wallpapers/);
assert.ok((html.match(/data-reveal="[0-6]"/g) ?? []).length >= 40);
assert.equal((gallery.match(/<article class="download-card/g) ?? []).length, 15);
assert.doesNotMatch(gallery, /Schon im Schrank|Die neue Sammlung/);
const phoneSection = gallery.match(/<section class="library-section" aria-labelledby="phone-wallpapers">[\s\S]*?<\/section>/)?.[0] ?? "";
const laptopSection = gallery.match(/<section class="library-section library-section--laptop"[\s\S]*?<\/section>/)?.[0] ?? "";
assert.equal((phoneSection.match(/<article class="download-card/g) ?? []).length, 14);
assert.equal((laptopSection.match(/<article class="download-card/g) ?? []).length, 1);
assert.match(laptopSection, /1 Motiv · 3 Varianten/);
assert.equal((gallery.match(/href="\.\/#slide-wallpapers"/g) ?? []).length, 2);
assert.match(gallery, /downloads\/mila-foto-handy-1440x3200\.jpg/);
assert.match(gallery, /downloads\/mila-foto-laptop-2560x1440\.jpg/);

const assets = [...(html + gallery).matchAll(/(?:src|href)="((?:assets|downloads)\/[^"?]+)/g)];
await Promise.all(assets.map(([, path]) => access(join(site, path))));

console.log(`OK: 9 Folien, ${assets.length} lokale Assets, Übergänge und Texte geprüft.`);
