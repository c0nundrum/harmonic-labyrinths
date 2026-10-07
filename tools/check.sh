#!/usr/bin/env bash
# Build the site and run the repository checks (AGENTS.md, "Validation").
# The same script runs locally and in CI.
#
#   tools/check.sh            build, XML, links, accessibility
#   tools/check.sh --no-a11y  skip the accessibility pass (no browser needed)
#
# Requires: hugo, python3, htmltest; Node (npx) for the accessibility pass.
set -euo pipefail
cd "$(dirname "$0")/.."

a11y=true
[[ "${1:-}" == "--no-a11y" ]] && a11y=false

out=public
mirror=.check   # the site under its base path, so root-relative links resolve
port=8123

echo "==> Build (warnings are errors)"
rm -rf "$out" "$mirror"
hugo --gc --minify --panicOnWarning --destination "$out"

base_url=$(hugo config --format json | python3 -c 'import json, sys; print(json.load(sys.stdin)["baseurl"])')
read -r origin base_path < <(python3 -c 'import sys, urllib.parse as u; p = u.urlparse(sys.argv[1]); print(f"{p.scheme}://{p.netloc}", p.path.strip("/") or ".")' "$base_url")
mkdir -p "$mirror/$base_path"
cp -R "$out"/. "$mirror/$base_path"/

echo "==> Feeds and sitemap are well-formed XML"
python3 - "$out" <<'PY'
import pathlib, sys, xml.etree.ElementTree as ET
files = sorted(pathlib.Path(sys.argv[1]).rglob("*.xml"))
for f in files:
    ET.parse(f)
print(f"{len(files)} XML files parse")
PY

echo "==> Internal links and fragments"
htmltest --conf .htmltest.yml

if $a11y; then
  echo "==> Accessibility: axe on every page in the sitemap, plus the specimen and 404"
  python3 -m http.server "$port" --directory "$mirror" >/dev/null 2>&1 &
  server=$!
  trap 'kill $server 2>/dev/null' EXIT
  local_root="http://localhost:$port/${base_path#.}"
  local_root="${local_root%/}"
  for _ in {1..50}; do curl -fs "$local_root/" >/dev/null && break; sleep 0.1; done
  # Pages outside the sitemap go in a generated config; the CLI keeps only one extra URL.
  python3 -c 'import json, sys
config = json.load(open(".pa11yci.json"))
config["urls"] = [sys.argv[1] + "/specimen/", sys.argv[1] + "/404.html"]
print(json.dumps(config))' "$local_root" > "$mirror/pa11yci.json"
  npx --yes pa11y-ci@5.0.0 --config "$mirror/pa11yci.json" \
    --sitemap "$local_root/sitemap.xml" \
    --sitemap-find "$origin" --sitemap-replace "http://localhost:$port"
fi

echo "==> All checks passed"
