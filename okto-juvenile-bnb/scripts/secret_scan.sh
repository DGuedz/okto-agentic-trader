#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[SECURITY] running secret scan..."

PATTERN='(OKTO_PK=|BINANCE_API_KEY=|BINANCE_SECRET=|ASTER_API_KEY=|ASTER_SECRET=|DEPLOYER_PK=0x|-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----|MNEMONIC|SEED PHRASE|PRIVATE[_ ]?KEY)'

if git rev-parse --verify --quiet HEAD >/dev/null; then
  TARGETS="$(git diff --cached --name-only)"
else
  TARGETS="$(git ls-files)"
fi

if [[ -z "${TARGETS}" ]]; then
  echo "[SECURITY] no files to scan."
  exit 0
fi

# shellcheck disable=SC2086
MATCHES="$(rg -n -H -e "$PATTERN" $TARGETS \
  --no-messages \
  --glob '!**/.env.example' \
  --glob '!**/*.pyc' \
  --glob '!**/node_modules/**' \
  --glob '!**/.next/**' || true)"

if [[ -n "$MATCHES" ]]; then
  echo "[SECURITY] potential secrets found:"
  echo "$MATCHES"
  echo "[SECURITY] commit blocked. move secrets to local .env and rotate exposed keys."
  exit 1
fi

echo "[SECURITY] secret scan passed."
