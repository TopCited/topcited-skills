#!/usr/bin/env bash
# Convenience wrapper for TopCited API calls.
#
# Usage: tc-api.sh METHOD /api/v1/path [extra curl args...]
#   tc-api.sh GET  /api/v1/users/me
#   tc-api.sh POST /api/v1/brands -d '{"name":"Acme","website":"https://acme.com"}'
#
# Environment:
#   TOPCITED_API_KEY   required — your personal key, starts with "tc_"
#   TOPCITED_BASE_URL  optional — API base, defaults to https://api.topcited.ai
#
# Prints the response body on stdout. Exits 2 if the key is missing, 1 on any
# HTTP status >= 400 (with the status on stderr).
set -euo pipefail
: "${TOPCITED_BASE_URL:=https://api.topcited.ai}"
if [[ -z "${TOPCITED_API_KEY:-}" ]]; then
  echo "error: TOPCITED_API_KEY is not set (Settings -> Profile -> API Key in the TopCited app)" >&2
  exit 2
fi
method=${1:?usage: tc-api.sh METHOD /api/v1/path [curl args...]}
path=${2:?usage: tc-api.sh METHOD /api/v1/path [curl args...]}
shift 2
body_file=$(mktemp)
trap 'rm -f "$body_file"' EXIT
status=$(curl -sS -o "$body_file" -w '%{http_code}' -X "$method" \
  -H "Authorization: Bearer ${TOPCITED_API_KEY}" \
  -H "Content-Type: application/json" \
  "${TOPCITED_BASE_URL}${path}" "$@")
cat "$body_file"
echo
if (( status >= 400 )); then
  echo "error: HTTP $status from $method $path" >&2
  exit 1
fi
