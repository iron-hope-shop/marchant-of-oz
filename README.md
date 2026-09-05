# merchant-of-oz

Simple Hello World web application deployed to Google Cloud Run with Nginx reverse proxy for Firebase Authentication SSO.

## Direct Console & Configuration Links

### 1. Firebase Authorized Domains
- **Direct Link**: [Firebase Authentication Settings](https://console.firebase.google.com/project/iron-hope-shop-ff854/authentication/settings)
- **Authorized Domain to Add**: `merchant-of-oz-zk4so6dwua-uc.a.run.app`

### 2. Google Cloud OAuth 2.0 Credentials
- **Direct Link**: [GCP Credentials Console](https://console.cloud.google.com/apis/credentials?project=iron-hope-shop-ff854)
- **Authorized JavaScript origins**:
  - `https://merchant-of-oz-zk4so6dwua-uc.a.run.app`
- **Authorized redirect URIs**:
  - `https://merchant-of-oz-zk4so6dwua-uc.a.run.app/__/auth/handler`
  - `https://iron-hope-shop-ff854.firebaseapp.com/__/auth/handler`

### 3. Google Cloud Run Dashboard
- **Direct Link**: [Cloud Run Console](https://console.cloud.google.com/run?project=iron-hope-shop-ff854)

### 4. Google Artifact Registry Repositories
- **Direct Link**: [Artifact Registry Console](https://console.cloud.google.com/artifacts?project=iron-hope-shop-ff854)

## Architecture & Configuration

- `nginx.conf`: Nginx server on port `8080`, cache-control headers for PWA/SPA assets, `/healthz` endpoint, and reverse-proxy `/ __/auth/` to `https://iron-hope-shop-ff854.firebaseapp.com/__/auth/`.
- `Dockerfile`: Minimal `nginx:alpine` image.
- `public/index.html`: Static entry point and interactive Tamagui UI showcase.
- `public/tamagui.css`: Zero-dependency Tamagui design system with 12-step color scales, themes (Light/Dark), sub-themes (blue, purple, green, red, orange, pink, yellow), layout stacks (YStack, XStack, ZStack), and component styles.
- `public/tamagui-theme.js`: Vanilla theme runtime engine with persistence and responsive color-scheme listener.
- `.github/workflows/deploy.yml`: Automated CI/CD pipeline.
