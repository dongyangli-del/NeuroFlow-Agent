#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="${ROOT_DIR}/skills"
CODEX_SKILLS_SRC="${ROOT_DIR}/skills-codex"
CODEX_HOME_DIR="${CODEX_HOME:-${HOME}/.codex}"
SKILLS_DIR="${CODEX_HOME_DIR}/skills"

if [[ ! -d "${SKILLS_SRC}" ]]; then
  echo "Cannot find skills source: ${SKILLS_SRC}" >&2
  exit 1
fi

mkdir -p "${SKILLS_DIR}"

install_shared_resources() {
  local shared_src="${SKILLS_SRC}/_shared"
  local shared_dest="${SKILLS_DIR}/_shared"

  [[ -d "${shared_src}" ]] || return

  if [[ -L "${shared_dest}" ]]; then
    current_target="$(readlink "${shared_dest}")"
    if [[ "${current_target}" != "${shared_src}" ]]; then
      echo "Skipping _shared: existing symlink points to ${current_target}" >&2
      return
    fi
    rm "${shared_dest}"
  elif [[ -e "${shared_dest}" ]]; then
    echo "Skipping _shared: ${shared_dest} already exists and is not a symlink" >&2
    return
  fi

  ln -s "${shared_src}" "${shared_dest}"
  echo "Installed _shared -> ${shared_src}"
}

install_skill() {
  local skill_src="$1"
  local skill_name="$2"
  local skill_dest="${SKILLS_DIR}/${skill_name}"

  if [[ -L "${skill_dest}" ]]; then
    current_target="$(readlink "${skill_dest}")"
    repo_skill_target="${SKILLS_SRC}/${skill_name}"
    repo_codex_target="${CODEX_SKILLS_SRC}/${skill_name}"
    if [[ "${current_target}" != "${skill_src}" && "${current_target}" != "${repo_skill_target}" && "${current_target}" != "${repo_codex_target}" ]]; then
      echo "Skipping ${skill_name}: existing symlink points to ${current_target}" >&2
      return
    fi
    rm "${skill_dest}"
  elif [[ -e "${skill_dest}" ]]; then
    echo "Skipping ${skill_name}: ${skill_dest} already exists and is not a symlink" >&2
    return
  fi

  ln -s "${skill_src}" "${skill_dest}"
  echo "Installed ${skill_name} -> ${skill_src}"
}

install_shared_resources

for skill_src in "${SKILLS_SRC}"/*; do
  [[ -d "${skill_src}" ]] || continue
  [[ "$(basename "${skill_src}")" == _* ]] && continue
  [[ -f "${skill_src}/SKILL.md" ]] || continue
  skill_name="$(basename "${skill_src}")"
  codex_override="${CODEX_SKILLS_SRC}/${skill_name}"
  if [[ -f "${codex_override}/SKILL.md" ]]; then
    install_skill "${codex_override}" "${skill_name}"
  else
    install_skill "${skill_src}" "${skill_name}"
  fi
done

echo "Restart Codex to pick up the skill."
