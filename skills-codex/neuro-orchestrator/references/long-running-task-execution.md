# Long-Running Task Execution

Verification status: user-validated

## Failure Pattern

An IDE or agent owns the terminal process that owns a long-running training,
evaluation, download, upload, or synchronization job. Closing or interrupting
the IDE/agent then sends a hangup or closes the PTY, killing the scientific job
and leaving only a partial checkpoint or output directory.

Unsafe ownership tree:

```text
IDE or agent
└── interactive tool session
    └── long-running job
```

Required ownership tree:

```text
tmux, nohup + setsid, or systemd-run
└── long-running job

IDE or agent
└── short, read-only status and log checks
```

## When to Trigger

Apply this playbook before starting any command that may outlive the current
agent turn or editor session, especially GPU training, multi-stage experiments,
large transfers, rendering, sampling, evaluation, and benchmark sweeps.

## Launch Contract

1. Resolve the command, environment, GPU assignment, run directory, seed, and
   checkpoint policy before launch.
2. Create an immutable run directory with, at minimum, a log path, PID or tmux
   session identifier, and a completion or exit-status marker.
3. Launch the job under one of these independent supervisors:
   - `tmux` for an interactive process that a human may reattach to.
   - `nohup` plus `setsid` for a non-interactive batch command.
   - `systemd-run` when a managed user service and resource policy are available.
4. Redirect stdin from `/dev/null` for non-interactive jobs and redirect stdout
   and stderr to a persistent log. A bare trailing `&` is not sufficient.
5. Record the supervisor PID/session immediately. Do not rely on an agent tool's
   session ID as the experiment identifier.
6. Verify independence before reporting that the job is protected: the process
   must have its own session or tmux supervisor and must not depend on the agent's
   PTY. For a detached batch job, inspect PID, PPID, SID, command, and log growth.
7. After launch, the agent may only run short, read-only monitoring commands.
   Never keep a long poll, `tee` pipeline, training command, or transfer attached
   to an agent-owned execution session.

## Checkpoint and Recovery Contract

- Write checkpoints atomically when possible.
- A resumable training checkpoint must contain the live model, optimizer,
  scheduler, AMP scaler when used, EMA state when used, epoch/update count, and
  RNG state. A best-model-only or EMA-only file is an inference checkpoint, not
  an exact resume checkpoint.
- Write `stage_complete` or an equivalent sentinel only after the stage exits
  successfully and all required artifacts pass validation.
- If a job dies without the completion sentinel, preserve the run as
  interrupted. Do not relabel a partial best checkpoint as a completed run.
- If exact resume state is unavailable, either restart under the original
  protocol or explicitly label any partial-checkpoint continuation as a changed
  protocol. Never mix it silently into a formal comparison.

## Minimal Monitoring Probe

Check only what changes the decision:

- supervisor and worker processes still exist;
- PID/PPID/SID show an independent ownership tree;
- log or structured training record is advancing;
- expected GPU, disk, and output directory are in use;
- no error traceback or failed stage sentinel has appeared.

Monitoring failure must not affect the job. A cancelled status check should be
safe to repeat.

## Acceptance Criteria

- The long job survives editor, agent, and monitoring-session interruption.
- A human can recover status from the run directory without chat history.
- The exact launch command and resolved experiment identity are reconstructable.
- Completion is determined from process exit plus validated sentinels, not from
  the presence of a best checkpoint alone.
- Restart and resume decisions preserve protocol truthfulness.

## Reviewer-Facing Interpretation

Detached execution improves operational reliability, not scientific validity.
Claims still require split parity, metric parity, seed/config tracking, complete
stage markers, and inspected outputs. Interrupted or protocol-changed runs must
remain distinguishable from completed formal runs.
