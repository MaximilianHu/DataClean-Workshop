#!/usr/bin/env bash
# Utility to retroactively rewrite commit dates with random jitter for hobby cadence
set -euo pipefail

base="$1" # ISO8601 start
offset_min=${2:-5}
offset_max=${3:-720}

commit_list=$(git rev-list --reverse HEAD)
current="$base"
for c in $commit_list; do
  delta=$(( RANDOM % (offset_max - offset_min + 1) + offset_min ))
  seconds=$(( delta * 60 + (RANDOM % 53) ))
  current_ts=$(date -j -f %Y-%m-%dT%H:%M:%S "$current" +%s 2>/dev/null || date -d "$current" +%s)
  next_ts=$(( current_ts + seconds ))
  next=$(date -r "$next_ts" +%Y-%m-%dT%H:%M:%S 2>/dev/null || date -d @"$next_ts" +%Y-%m-%dT%H:%M:%S)
  GIT_COMMITTER_DATE="$next" GIT_AUTHOR_DATE="$next" git commit --amend --no-edit --date "$next" --allow-empty >/dev/null
  git rebase --committer-date-is-author-date --rebase-merges --reapply-cherry-picks --no-keep-base --onto "$c^" "$c^" "$c" >/dev/null 2>&1 || true
  current="$next"
done

echo "Rewrote dates up to: $current"

