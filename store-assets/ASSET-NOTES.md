# Asset notes

- Only one logo export: `logo/logo128.png`, 128×128 RGBA with transparent background.
- Screenshots: `screenshots/en/screenshot-1-browser.png` and `screenshot-2-introduction.png`, 1280×800 RGB.
- Promotional artwork: `promo/440x280.png` and `promo/1400x560.png`, RGB.
- All store text is English. The formal listing name is **Pastel Afterglow Theme**.
- Introduction background: #F1F3F5, separate from every palette swatch. Borders help define the lightest swatches.
- The browser previews are HTML/CSS illustrations rendered by headless Chromium, not screenshots of an installed theme. The Google wordmark color is illustrative. Native UI and new tab content can vary.
- Five base colors: #E0BBE4, #957DAD, #D291BC, #FEC8D8, #FFDFD3. The introduction identifies which colors belong to browser surfaces and which are artwork accents.
- Small promo: visible logo, title, tagline and category visually centered as one group. Large promo: visible logo, title and copy vertically balanced alongside a browser preview.
- Browser surfaces read from `manifest.json`; regenerate assets after palette changes.
