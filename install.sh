#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_SRC="${ROOT_DIR}/skills/ai-bci-research"
CODEX_HOME_DIR="${CODEX_HOME:-${HOME}/.codex}"
SKILLS_DIR="${CODEX_HOME_DIR}/skills"
SKILL_DEST="${SKILLS_DIR}/ai-bci-research"

if [[ ! -f "${SKILL_SRC}/SKILL.md" ]]; then
  echo "Cannot find skill source: ${SKILL_SRC}" >&2
  exit 1
fi

mkdir -p "${SKILLS_DIR}"
rm -rf "${SKILL_DEST}"
cp -R "${SKILL_SRC}" "${SKILL_DEST}"

echo "Installed ai-bci-research to ${SKILL_DEST}"
echo "Restart Codex to pick up the skill."
