# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2026-09-05

### Added
- **E-Commerce Routing & Storefront System**:
  - Hash-based Single Page App (SPA) router supporting routes: `#/home`, `#/shop`, `#/product/:id`, `#/cart`, `#/settings`, `#/settings/themes`, `#/settings/account`, `#/settings/general`, `#/login`.
  - Product Catalog grid with categories, pricing, item cards, and direct "Add to Cart" / "Details" actions.
  - Dedicated Product Detail view with rich specifications and direct cart integration.
  - Interactive Shopping Cart with live item counter badge in the top navigation, item quantity controls (+/-), item removal, order total calculation, and checkout modal confirmation.
- **Dynamic Auth-State Navigation**:
  - Unauthenticated guests see a dedicated `Log In` tab in the top navigation bar and direct login call-to-actions on the home screen.
  - Authenticated users dynamically see the `Settings` tab in top navigation and workspace settings controls.
- Incremented build version to `v1.0.6-44` in `public/version.json` and UI watermarks.
- Updated unit test suite in `tests/test_deploy.py` to assert e-commerce views, route handling, and auth-state navigation controls.
- Explicit Google OAuth scopes (`profile`, `email`) and `prompt: 'select_account'` parameter added to `GoogleAuthProvider` to enforce proper avatar photo retrieval permissions.
- Safe client-side local avatar upload mechanism using HTML5 Canvas re-encoding:
  - Validates file type (`image/jpeg`, `image/png`, `image/webp`, `image/gif`) and enforces a 2MB size limit.
  - Re-encodes images onto a sanitized Canvas (max 256x256) to strip malicious EXIF/metadata and prevent polyglot file execution before storing in client storage.
  - Added visual avatar source badge and one-click "Reset to Google Photo" action.
- Auth-gated theme customization:
  - Theme mode (Light/Dark/Auto) and accent color sub-theme controls now require user sign-in.
  - Displays a clean "Sign In Required" lock banner with a quick navigation link to the Account sign-in view when signed out.
- Incremented build version to `v1.0.5-43` in `public/version.json` and UI watermarks.
- Updated unit test suite in `tests/test_deploy.py` to assert presence of theme auth gating and custom avatar components.
  - Design tokens for sizing, spacing ($size/$space), radius, typography, shadows, transitions, and z-indices.
  - 12-step color scales for Gray, Blue, Purple, Green, Red, Orange, Pink, and Yellow.
  - Light and Dark base themes with system auto-detection and sub-theme color palettes (`blue`, `purple`, `green`, `red`, `orange`, `pink`, `yellow`).
  - Core layout primitives: `YStack`, `XStack`, `ZStack`, `Group`, and `Spacer`.
  - Component library: `Card`, `Button` (primary, subtle, ghost, destructive, sizes), `Input`/`Textarea`, `Switch`, `Badge`, `Avatar`, `Separator`, `Tooltip` (with `.t-tooltip-primary` adaptive color support), and `Modal Dialog`.
  - Distinct badge variants separating semantic statuses (`.t-badge-warning`, `.t-badge-danger`, `.t-badge-success`, `.t-badge-info`) from raw palette colors (`.t-badge-yellow`, `.t-badge-red`, `.t-badge-blue`, `.t-badge-purple`, `.t-badge-green`, `.t-badge-orange`, `.t-badge-pink`, `.t-badge-gray`).
  - Top navigation bar component (`.t-nav`, `.t-nav-tabs`, `.t-nav-tab`).
  - Left drawer navigation layout (`.t-drawer-layout`, `.t-drawer-nav`, `.t-drawer-item`, `.t-drawer-content`).
- Internal version and build tracker (`public/version.json`) with version number and build number.
- Lightweight theme management runtime (`public/tamagui-theme.js`) providing theme switching, sub-theme selection, local persistence, media query listening, and state event subscriptions.
- Redesigned `public/index.html` application shell with:
  - Top navigation simplified to `Home` and `Settings`.
  - Robust Google profile avatar resolution checking `user.photoURL` and `providerData` with high-res formatting (`=s256-c`), `referrerpolicy="no-referrer"`, error fallbacks, and rendering in header and account view.
  - Consolidated authentication/portal view into `Settings -> Account`.
  - Streamlined `Settings -> Themes` drawer view containing theme pickers and live component controls.
  - Minimized footer into a discreet bottom-right build watermark (`v1.0.4-42`) with full details available under `Settings -> General`.
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
