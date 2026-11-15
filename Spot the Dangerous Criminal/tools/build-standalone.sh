#!/bin/sh
# Rebuild standalone.html from index.html.
#
# The actual work is done by the build-standalone skill, which is shared across
# repos; this script only records the flags this particular activity needs.
# index.html is never modified.
set -e

HERE=$(cd "$(dirname "$0")/.." && pwd)
BUNDLER="$HOME/.claude/skills/build-standalone/scripts/bundle.py"

if [ ! -f "$BUNDLER" ]; then
  echo "Can't find the bundler at:" >&2
  echo "  $BUNDLER" >&2
  echo "It comes from the build-standalone skill in ~/.claude/skills/." >&2
  exit 1
fi

exec python3 "$BUNDLER" "$HERE/index.html" \
  -o "$HERE/standalone.html" \
  --design 720x405 \
  --assets img/faces --assets-var FACES \
  --replace "$HERE/tools/rewrites.json" \
  --extra-css "$HERE/tools/fit.css" \
  "$@"
