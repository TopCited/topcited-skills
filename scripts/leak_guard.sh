#!/usr/bin/env bash
# Fail if any tracked file contains a forbidden pattern.
#
# Patterns come from two places:
#   - GENERIC_PATTERNS below (safe to publish);
#   - the LEAK_GUARD_PATTERNS env var: extended regexes, one per line.
#     In CI it is filled from a repository secret.
#
# Each file's whitespace (newlines included) is collapsed to single spaces
# before matching, so a phrase that wraps across lines is still caught.
# Matching is case-insensitive.
set -euo pipefail

GENERIC_PATTERNS='/home/
design-docs/
design[ -]docs?\b
§ ?[0-9]'

patterns_file=$(mktemp)
trap 'rm -f "$patterns_file"' EXIT
printf '%s\n%s\n' "$GENERIC_PATTERNS" "${LEAK_GUARD_PATTERNS:-}" \
  | tr -d '\r' | grep -v '^[[:space:]]*$' > "$patterns_file"

# A malformed regex makes grep exit 2, which below would read as "no match".
rc=0; grep -qiE -f "$patterns_file" /dev/null || rc=$?
if [ "$rc" -gt 1 ]; then
  echo "::error::LEAK_GUARD_PATTERNS contains an invalid regex; refusing to pass."
  exit 1
fi

found=0
while IFS= read -r -d '' f; do
  case "$f" in .github/*|scripts/leak_guard.sh) continue ;; esac
  if hits=$(tr -s '[:space:]' ' ' < "$f" | grep -oiE -f "$patterns_file" | sort -u); then
    while IFS= read -r hit; do
      echo "::error file=$f::forbidden reference: $hit"
    done <<< "$hits"
    found=1
  fi
done < <(git ls-files -z)

if [ "$found" -ne 0 ]; then
  echo "Found references that must not ship in a public repo (see above)."
  exit 1
fi
echo "No internal references found ($(wc -l < "$patterns_file") patterns)."
