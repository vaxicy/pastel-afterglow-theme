<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/pastel-afterglow-theme/main/logo/logo128.png" width="128" alt="Pastel Afterglow Theme icon">
</p>

<h1 align="center">Pastel Afterglow Theme</h1>

<p align="center">A soft pastel Chrome theme in muted lavender, blush pink and creamy peach.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Chrome%20Web%20Store-theme-blue?logo=googlechrome" alt="Chrome Web Store">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="version">
  <img src="https://img.shields.io/badge/license-Non--Commercial-lightgrey" alt="license">
</p>

## About

Pastel Afterglow Theme brings the last soft light of evening to the browser. A muted lavender frame wraps the top of the window, the toolbar and active tab warm into creamy peach, and the new tab page opens on pale blush so the page you are reading stays the brightest thing on screen. Deep lavender marks the new tab header and every link, deep plum text keeps tab titles, bookmark labels, toolbar icons and the address bar sharp on the light surfaces, and background tabs use a darker plum so they stay readable on the lavender frame. The design is flat colour throughout — no wallpaper, no textures, no gradients — and the icon distills it into a pale cloud drifting in front of a low sun, with a single sparkle above.

## Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Muted Lavender | `#957DAD` | Window frame (active and inactive) and window button background |
| Creamy Peach | `#FFDFD3` | Toolbar, active tab, bookmarks bar |
| Milk White | `#FFF7F3` | Omnibox (address bar) field |
| Pale Blush | `#FCEEF3` | New tab page background |
| Deep Plum | `#493850` | Tab, bookmark, toolbar and new-tab text, toolbar icons |
| Deep Lavender | `#765B8B` | New tab page header and links |
| Dark Plum | `#241B2D` | Background tab titles on the lavender frame |
| Pale Plum | `#E0BBE4` | Accent tone used in the logo and store artwork |
| Dusty Rose | `#D291BC` | Accent tone used in the logo and store artwork |
| Blush Pink | `#FEC8D8` | Accent tone used in the store artwork; inspired the pale blush page |

Deep plum carries all small text, because lavender at this lightness is too low-contrast to read at 12–13px. Pale plum, dusty rose and blush pink live in the logo and artwork rather than on browser chrome.

## Chrome UI notes

Not every pixel in the window comes from the manifest — Chrome and the operating system paint some of them — so the store previews follow what a real install renders:

- **Google wordmark on the new tab page:** drawn by Chrome as a single flat tint computed from the new tab background, so it appears soft pink here rather than as the four-colour brand mark.
- **Shortcut tiles:** Chrome tints the round shortcut buttons the same way, so they pick up the same blush tone instead of a fixed brand colour.
- **Window buttons, hover fills and separators:** painted by Chrome and Windows, and left in their own neutral tones on the lavender frame.
- **Address bar:** a white field with Chrome's own focus outline, which stays legible against the creamy peach toolbar.

## Features

- Muted lavender frame with a creamy peach toolbar and active tab for crisp, readable browser chrome.
- Flat, solid colour design with no wallpaper, textures or gradients.
- Pale blush new tab page with deep plum text and deep lavender header and links.
- Background tab titles kept readable on the lavender frame with a darker plum.
- One continuous frame colour whether the window is focused or not.
- Single-tone Google wordmark drawn by Chrome itself through `ntp_logo_alternate`.
- Pure theme: no scripts, no permissions, nothing collected.

## Install

### From source (unpacked)

1. Download or clone this repository.
2. Open Chrome and navigate to `chrome://extensions`.
3. Enable **Developer mode** in the top-right corner.
4. Click **Load unpacked** and select this folder.
5. The theme applies immediately; reset it any time under Settings, then Appearance, then Themes.

### From the Chrome Web Store

The store listing is in preparation. Until it is live, load the unpacked copy with the steps above.

## Preview

### Store screenshots · 1280×800

**Browser interface** — the themed window with a bookmarks bar and the new tab page.

![Pastel Afterglow Theme browser preview](https://raw.githubusercontent.com/vaxicy/pastel-afterglow-theme/main/store-assets/screenshots/en/screenshot-1-browser.png)

**Palette & highlights** — the five tones the theme is built from and what each one controls.

![Pastel Afterglow Theme palette](https://raw.githubusercontent.com/vaxicy/pastel-afterglow-theme/main/store-assets/screenshots/en/screenshot-2-introduction.png)

### Store promo tiles

**Marquee tile · 1400×560** — “Soft lavender. Warm peach. A gentle glow for every tab.”

![Pastel Afterglow Theme marquee](https://raw.githubusercontent.com/vaxicy/pastel-afterglow-theme/main/store-assets/promo/1400x560.png)

**Small tile · 440×280** — “A little afterglow for your everyday browser.”

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/pastel-afterglow-theme/main/store-assets/promo/440x280.png" width="440" alt="Pastel Afterglow Theme promo tile">
</p>

These are illustrative English HTML/CSS layouts rendered by headless Chromium and calibrated against a real installed Chrome session. Browser surfaces take their colours from `manifest.json`; the Chrome-painted details — the pink Google wordmark and shortcut tiles, the white search field, the dark AI cards and the dark *Customize Chrome* button — follow the reference browser, and the sampled tones are listed in [`store-assets/ASSET-NOTES.md`](store-assets/ASSET-NOTES.md). Tabs and bookmarks use generic English labels. These are not native captures, so controls and new tab content can vary by browser version and operating system.

## Files

| File | Description |
|------|-------------|
| `manifest.json` | Chrome theme manifest (MV3) with an inline `theme` block — single source of truth for every colour |
| `logo/logo128.png` | Theme and store icon, 128x128, the only size the manifest references |
| `store-assets/screenshots/en/` | Store listing screenshots (1280x800) |
| `store-assets/promo/` | Promo tiles (440x280 and 1400x560) |
| `store-assets/references/` | The browser, introduction and promo mock-up HTML plus their PNG renders |
| `store-assets/ASSET-NOTES.md` | Calibration notes: which tones are manifest colours and which are sampled from Chrome |
| `store-assets/store-description.txt` | Store listing description (English) |
| `scripts/generate-store-assets.py` | Draws the 128px logo and renders every store asset in one pass |
| `scripts/requirements.txt` | Python dependencies for the asset generator |
| `scripts/package.ps1` | Builds the release ZIP |
| `PACKAGING.md` | How the upload ZIP is built |
| `LICENSE` | Non-Commercial License (bilingual) |

## Regenerating the assets

```
pip install -r scripts/requirements.txt
playwright install chromium

python scripts/generate-store-assets.py
```

One composer renders all four store assets — both screenshots, both promo tiles, and the HTML sources in `store-assets/references/` — so a style change is made in the script and re-rendered, never patched onto a PNG. The script draws the transparent 128x128 logo, downsamples it for smooth edges, and asserts that every output matches its declared size.

## Packaging

```
powershell -ExecutionPolicy Bypass -File scripts/package.ps1 -Force
```

Writes one ZIP to the default folder `D:\迅雷下载\vibe coding`: `pastel-afterglow-theme-<version>.zip`, holding the complete project with `manifest.json` at the archive root, so the same archive is what the Chrome Web Store upload form takes. `-Force` overwrites an existing archive.

The screenshots and promo tiles travel inside the complete ZIP, but the store form still needs them uploaded one by one: `store-assets/screenshots/en/` fills the two screenshot slots, `store-assets/promo/1400x560.png` is the marquee tile and `store-assets/promo/440x280.png` is the small tile.

## License

Non-Commercial License — personal use permitted, commercial use requires permission. See [LICENSE](LICENSE).
