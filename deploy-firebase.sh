#!/usr/bin/env bash
set -e

PROJECT_ID="iron-hope-shop-ff854"

echo "Deploying Firebase Hosting for project: ${PROJECT_ID}"

if [ -n "$FIREBASE_TOKEN" ]; then
  echo "Using FIREBASE_TOKEN for authentication..."
  npx --yes firebase-tools deploy --only hosting --project "${PROJECT_ID}" --token "$FIREBASE_TOKEN" --non-interactive
elif [ -n "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
  echo "Using GOOGLE_APPLICATION_CREDENTIALS for authentication..."
  npx --yes firebase-tools deploy --only hosting --project "${PROJECT_ID}" --non-interactive
else
  echo "No FIREBASE_TOKEN or GOOGLE_APPLICATION_CREDENTIALS detected."
  echo "Attempting standard deploy (requires prior 'firebase login' or interactive auth)..."
  npx --yes firebase-tools deploy --only hosting --project "${PROJECT_ID}" --non-interactive
fi
