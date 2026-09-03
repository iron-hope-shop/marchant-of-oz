# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2026-09-03

### Changed
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
