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

assert.equal((html.match(/<section class="slide /g) ?? []).length, 10);
assert.match(html, /Jutta, Manny, Maxi und Benny\./);
assert.match(html, /mila-road-skeptical\.webp/);
assert.match(css, /@keyframes deck-wipe/);
assert.match(css, /@media \(prefers-reduced-motion: reduce\)/);
assert.match(js, /deck\.classList\.add\("is-wiping"\)/);
assert.equal((gallery.match(/<article class="download-card/g) ?? []).length, 15);

const assets = [...(html + gallery).matchAll(/(?:src|href)="((?:assets|downloads)\/[^"?]+)/g)];
await Promise.all(assets.map(([, path]) => access(join(site, path))));

console.log(`OK: 10 Folien, ${assets.length} lokale Assets, Übergänge und Texte geprüft.`);
