#!/usr/bin/env bash
set -euo pipefail

H1_DANCE_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
H1_DANCE_PROJECT_ROOT="$(cd "$H1_DANCE_SCRIPT_DIR/../.." && pwd)"

cd "$H1_DANCE_PROJECT_ROOT"
source scripts/source_isaacsim_setup.sh

exec python "$H1_DANCE_SCRIPT_DIR/holosoma_isaacsim.py" train \
  exp:h1-19dof-wbt \
  simulator:isaacsim \
  --training.name h1_19dof_wbt_dance_standing_end_calibrated_physx \
  --command.setup-terms.motion-command.params.motion-config.motion-file="holosoma/data/motions/h1_19dof/whole_body_tracking/dance1_h1_mj_fps50_standing_end.npz" \
  "$@"
