#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOK_DIR="$(cd "$ROOT_DIR" && git rev-parse --git-path hooks)"
HOOK_PATH="$HOOK_DIR/pre-commit"

mkdir -p "$HOOK_DIR"

cat > "$HOOK_PATH" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
if [ -x "$ROOT/scripts/secret_scan.sh" ]; then
  "$ROOT/scripts/secret_scan.sh"
elif [ -x "$ROOT/okto-juvenile-bnb/scripts/secret_scan.sh" ]; then
  "$ROOT/okto-juvenile-bnb/scripts/secret_scan.sh"
else
  echo "[WARN] secret_scan.sh not found; skipping"
fi
EOF

chmod +x "$HOOK_PATH"
chmod +x "$ROOT_DIR/scripts/secret_scan.sh"

echo "[SECURITY] pre-commit hook installed at .git/hooks/pre-commit"
