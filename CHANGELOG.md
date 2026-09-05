# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2026-09-05

### Added
- **Seamless Fluid Storefront Feed & Discovery Bar**:
  - Eliminated hard visual separators and jarring section breaks across the main store scroll for a continuous, flowing discovery stream.
  - Added integrated Discovery Bar (`#storefront-discovery-bar`) featuring:
    - Real-time instant search input with live keyword matching against product names, descriptions, categories, and tags.
    - Clear search button with quick reset functionality.
    - Category pill switcher (`All Items`, `Apparel`, `Footwear`, `Accessories`, `Homeware`, `Lighting`).
    - Trending discovery topic chips (`✨ Sparkle`, `⚙️ Steampunk`, `💎 Emerald`, `🏺 Artisan`, `🏮 Glow`, `🔥 Under $50`).
    - Dynamic sorting options (Featured Picks, Price: Low to High, Price: High to Low, Alphabetical A-Z).
    - Live feed filter indicator and empty-state guidance with one-click filter reset.
- Incremented build version to `v1.1.0-48` in `public/version.json` and UI watermarks.
- Updated automated unit test suite in `tests/test_deploy.py` to assert fluid discovery feed components, search inputs, trending chips, and sort controls.

- **Global `window.AppAuth` Authentication Bridge**:
  - Resolved module-scoping limitation that isolated Firebase popup triggers from top-level event handlers.
  - Exposed universal methods `window.AppAuth.signIn()`, `window.AppAuth.signOut()`, and `window.AppAuth.getCurrentUser()`.
  - Wired all sign-in triggers (Top navigation guest Log In button, Universal Auth Modal popup button, Settings Account subpanel button) to the bridge with error handling.
- **Immediate Initial Rendering (Zero Blank Start)**:
  - Invoked immediate synchronous rendering routines (`loadCart()`, `renderHomePinterestCollage()`, `renderCatalog()`, `renderCartUI()`, `handleRoute()`) directly on script evaluation alongside `DOMContentLoaded` listeners.
  - Eliminates initial blank white screen delay prior to asynchronous module loading.
- **Google Ads Styled Responsive Ad Units**:
  - Top leaderboard ad banner unit (`.ad-banner-slot.ad-leaderboard`) with official Ad badge, partner attribution, gradient artwork, and CTA button.
  - In-feed sponsored pin in the Pinterest-style masonry feed (`.collage-pin.ad-pin`) with responsive aspect styling and promotional callout.
  - Footer display ad unit (`.ad-banner-slot.ad-footer-unit`) for delivery discounts and partner offers.
- Incremented build version to `v1.0.9-47` in `public/version.json` and UI watermarks.
- Updated automated test suite in `tests/test_deploy.py` to assert `AppAuth` bridge wiring, ad slot components, and immediate render routines.

- **Unified Storefront (Amazon + Pinterest + Walmart Experience)**:
  - Merged Home and Shop into a single, seamless, high-engagement storefront page.
  - Flash Sale deal ribbon with animated gradient highlights and discount callouts.
  - Curated Hero promo with instant catalog smooth-scrolling.
  - Interactive Pinterest-style masonry discovery collage with real-time category filter synchronization.
  - Full structured product shelf catalog embedded directly on the main page.
- **Top Navigation User Avatar Dropdown & Guest Action**:
  - Relocated user profile to the far right of the top navigation.
  - When authenticated: Displays the user's Google/Custom avatar with an interactive dropdown menu providing quick access to Theme Customization, Account Settings, General Preferences, and Sign Out.
  - When guest: Replaces avatar with a prominent Google Sign-In button.
- **Universal Auth Modal & Read-Only Access Gate**:
  - Added `#auth-prompt-modal` dialog that appears seamlessly when guests try to access restricted account/theme capabilities.
  - Retained read-only previews with clear lock callouts for signed-out visitors.
- Incremented build version to `v1.0.8-46` in `public/version.json` and UI watermarks.
- Updated unit test suite in `tests/test_deploy.py` to assert unified storefront elements, right-aligned avatar dropdown, and universal auth prompt modal.
- **Pinterest-Style Masonry Shopping Collage on Home**:
  - Replaced legacy empty state / welcome message with a Pinterest-inspired responsive masonry feed (`.pinterest-collage`, `.collage-pin`).
  - Varying pin card heights (`tall`, `medium`, `compact`, `featured`), vibrant gradient backdrops, categories, custom tags (`Bestseller`, `Handmade`, `Steampunk`, `Ambient Glow`), and quick-add overlay actions.
  - Interactive category filter bar (`All Pins`, `Apparel`, `Footwear`, `Accessories`, `Homeware`, `Lighting`) with real-time DOM filtering.
  - Responsive column adaptations for multi-device viewports.
- **Strict Route Guarding for Settings**:
  - Enforced unauthenticated guest lock on all settings routes (`#/settings`, `#/settings/*`, `#/account`), redirecting guests cleanly to the Google Sign-In panel (`#/login`).
  - Removed "Welcome Back [User]" and account action buttons from Home to present a clean, distraction-free guest storefront.
- Incremented build version to `v1.0.7-45` in `public/version.json` and UI watermarks.
- Updated unit test suite in `tests/test_deploy.py` to assert Pinterest masonry elements, category filter bar, and route guard redirects.
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
