# Packaging

Run `scripts/package.ps1` from PowerShell. By default, ZIPs are written to `D:\迅雷下载\vibe coding`, derived as the parent of the Chrome-themes workspace. Use `-OutputDirectory` to choose another location. Use `-Force` only to replace an existing ZIP.

- `pastel-afterglow-theme-1.0.0.zip`: complete project, including store artwork, scripts, documentation and license.
- `pastel-afterglow-theme-1.0.0-upload.zip`: manifest and logo only, for the store theme upload.

Both ZIPs have `manifest.json` at their root. Store screenshots and promo images are uploaded separately in the listing form. The packaging script checks manifest identity, referenced logo inclusion and excludes local caches, repository metadata and nested archives.
