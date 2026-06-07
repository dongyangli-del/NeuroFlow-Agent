#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="${ROOT_DIR}/skills"
CODEX_HOME_DIR="${CODEX_HOME:-${HOME}/.codex}"
SKILLS_DIR="${CODEX_HOME_DIR}/skills"

if [[ ! -d "${SKILLS_SRC}" ]]; then
  echo "Cannot find skills source: ${SKILLS_SRC}" >&2
  exit 1
fi

mkdir -p "${SKILLS_DIR}"

for skill_src in "${SKILLS_SRC}"/*; do
  [[ -d "${skill_src}" ]] || continue
  [[ -f "${skill_src}/SKILL.md" ]] || continue
  skill_name="$(basename "${skill_src}")"
  skill_dest="${SKILLS_DIR}/${skill_name}"
  rm -rf "${skill_dest}"
  ln -s "${skill_src}" "${skill_dest}"
  echo "Installed ${skill_name} -> ${skill_src}"
done

echo "Restart Codex to pick up the skill."
