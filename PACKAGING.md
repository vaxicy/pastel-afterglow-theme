# Packaging

Run `scripts/package.ps1` from PowerShell. By default, the ZIP is written to `D:\迅雷下载\vibe coding`, derived as the parent of the Chrome-themes workspace. Use `-OutputDirectory` to choose another location. Use `-Force` to replace an existing ZIP.

- `pastel-afterglow-theme-1.0.0.zip`: the complete project, including store artwork, scripts, documentation and license.

`manifest.json` sits at the archive root, so the same archive is what the Chrome Web Store upload form takes. Store screenshots and promo images travel inside the ZIP but are attached separately in the listing form. The packaging script checks manifest identity, referenced logo inclusion and excludes local caches, repository metadata and nested archives.
