# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2026-09-05

### Added
- Zero-dependency Tamagui-inspired UI design system (`public/tamagui.css`) with:
  - Design tokens for sizing, spacing ($size/$space), radius, typography, shadows, transitions, and z-indices.
  - 12-step Radix/Tamagui color scales for Gray, Blue, Purple, Green, Red, Orange, Pink, and Yellow.
  - Light and Dark base themes with system auto-detection and sub-theme color palettes (`blue`, `purple`, `green`, `red`, `orange`, `pink`, `yellow`).
  - Tamagui layout primitives: `YStack`, `XStack`, `ZStack`, `Group`, and `Spacer`.
  - Component library: `Card`, `Button` (primary, subtle, ghost, destructive, sizes), `Input`/`Textarea`, `Switch`, `Badge`, `Avatar`, `Separator`, `Tooltip` (with `.t-tooltip-primary` adaptive color support), and `Modal Dialog`.
  - Distinct badge variants separating semantic statuses (`.t-badge-warning`, `.t-badge-danger`, `.t-badge-success`, `.t-badge-info`) from raw palette colors (`.t-badge-yellow`, `.t-badge-red`, `.t-badge-blue`, `.t-badge-purple`, `.t-badge-green`, `.t-badge-orange`, `.t-badge-pink`, `.t-badge-gray`).
  - Top navigation bar component (`.t-nav`, `.t-nav-tabs`, `.t-nav-tab`).
  - Left drawer navigation layout (`.t-drawer-layout`, `.t-drawer-nav`, `.t-drawer-item`, `.t-drawer-content`).
  - Persistent bottom footer for environment and build details.
- Lightweight theme management runtime (`public/tamagui-theme.js`) providing theme switching, sub-theme selection, local persistence, media query listening, and state event subscriptions.
- Redesigned `public/index.html` application shell with:
  - Sticky top navigation across views (`Home`, `Portal`, `Settings`).
  - Clean, dedicated blank Home screen.
  - Settings screen with a left drawer navigation containing `Themes` (color mode switcher, sub-theme picker, live engine output), `General`, and `Account`.
  - Dedicated bottom footer displaying Cloud Run environment & build details.
  - Preserved Firebase Google Auth SSO workflow.
- Lightweight theme management runtime (`public/tamagui-theme.js`) providing theme switching, sub-theme selection, local persistence, media query listening, and state event subscriptions.
- Updated `public/index.html` UI showcase demonstrating the design system, theme switching, interactive modal and controls while preserving Firebase Google Auth SSO.
- Added comprehensive unit tests in `tests/test_deploy.py` for design system tokens, themes, sub-themes, and theme engine functionality.
- Updated GitHub Actions workflow triggers in `.github/workflows/google-cloudrun-docker.yml` to include `cursor/**` branches and `pull_request` events.
- Logged Firebase deployment CLI authentication requirement in `error.log`.

## [1.0.0] - 2026-09-03

### Added
- Integrated Firebase Web SDK (v11) with Google Sign-In popup flow, user profile view, and sign-out handler in `public/index.html`.
- Updated direct console URLs in `README.md` for deployed service `https://merchant-of-oz-zk4so6dwua-uc.a.run.app`.

### Changed
- Logged Artifact Registry repository lookup failure in `error.log`.
- Updated unit test in `tests/test_deploy.py` to match new `REPOSITORY: merchant-of-oz` workflow configuration.

### Added
- Workflow integration for Google Cloud Run deployment (`.github/workflows/google-cloudrun-docker.yml`).
- Firebase Hosting configuration (`firebase.json` and `.firebaserc`) for project `iron-hope-shop-ff854`.
- Automated deployment helper script `deploy-firebase.sh` supporting `FIREBASE_TOKEN` and `GOOGLE_APPLICATION_CREDENTIALS`.
- Static "Hello World" frontend web application in `public/index.html`.
- Custom `nginx.conf` configured for port `8080`, cache-busting headers for PWA/SPA assets, Firebase reverse-proxy (`/__/auth/` -> `iron-hope-shop-ff854.firebaseapp.com/__/auth/`), and `/healthz` endpoint.
- `Dockerfile` using `nginx:alpine` to package and serve static files on Cloud Run.
- GitHub Actions workflow `.github/workflows/deploy.yml` for automated testing, Docker build & push to GCP Artifact Registry, and deployment to Google Cloud Run.
- Python unit test suite in `tests/test_deploy.py` to validate deployment assets and configurations.
- Comprehensive GCP and Firebase Auth configuration guide and console links in `README.md`.
- `error.log` tracking runtime errors and log output.
