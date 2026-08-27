#!/usr/bin/env sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repository_root=$(dirname "$script_dir")
source_skill="$repository_root/skills/production-web-standard"
destination_root="${1:-${CODEX_HOME:-$HOME/.codex}/skills}"
target_skill="$destination_root/production-web-standard"

if [ -e "$target_skill" ]; then
  printf 'Installation already exists at %s. Remove or back it up before reinstalling.\n' "$target_skill" >&2
  exit 1
fi

mkdir -p "$destination_root"
cp -R "$source_skill" "$target_skill"
printf 'Installed production-web-standard to %s\n' "$target_skill"
