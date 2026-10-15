# Session 12 Hands-on Lab: Safe Runbook Automation

**Track:** Enterprise Ops  
**Duration:** 28 minutes  
**Tools:** Microsoft Copilot Chat and GitHub Copilot in VS Code  
**Working mode:** Local synthetic exercise only. No production systems.

## Lab objective

Review and validate a small workflow for identifying eligible old log files and archiving them inside the supplied exercise folder. The aim is not simply to make the script work. Demonstrate that operational automation needs explicit scope, a dry-run mode, an approval gate, validation, audit evidence, and a clear definition of success.

You will use Copilot to understand the runbook, review the starter script, plan and, if authorized, perform a safe dry run, then recommend improvements. You are not expected to create an autonomous agent.

## Files to use

Use the supplied Session 12 materials:

- `Runbook_Disk_Utilization_Exercise.docx`
- `Runbook_Automation_Control_Checklist.docx`
- `runbook_automation_starter.py`
- `sample_server/logs/`
- `sample_server/archive/`


The files and log contents are synthetic training data. The script is intended for the exercise folder only.

## Safety rules

1. Keep all work inside the supplied exercise folder.
2. Do not point the script at a real server, real log directory, or production environment.
3. Start with a static review. Do not run the script until the facilitator confirms that the exercise copy and paths are correct.
4. Use dry-run behaviour first. Do not add `--approve` merely to make the script appear successful.
5. Do not delete logs. The exercise runbook permits archiving eligible files, not deleting them.
6. Do not assume that moving old logs will resolve high disk utilization. Verify the operational outcome separately.
7. Do not claim that a test passed unless you actually ran it and observed the result.
8. Do not overwrite existing archive files or bypass an approval requirement to get a green result.
9. If a path, file eligibility rule, or required approval is unclear, record the question and stop rather than inventing a rule.

## Exercise scenario

An operations team is investigating high disk utilization. A runbook proposes identifying eligible older `.log` files in a controlled directory and archiving them. Some files may be too recent or otherwise ineligible. The archive may already contain a file with the same name. The team needs evidence that the script stays within scope, does not move files in dry-run mode, handles errors safely, and verifies each permitted move.

The supplied script is a training starter, not production-ready automation. Treat its behaviour as something to inspect and validate, not something to trust automatically.

## Tasks

### Task 1: Translate the runbook into controls (4 minutes)

Read both Word documents. Write down the operational requirements before looking for implementation details.

Capture at least:

- The permitted source directory and destination directory.
- The criteria for a file to be considered eligible.
- What dry-run mode must and must not do.
- What explicit approval is intended to authorize in this exercise.
- What must happen if a destination filename already exists.
- What evidence is required to verify a move.
- Which failures must stop the workflow or require human intervention.
- What the script must not claim about disk utilization or incident resolution.

**Deliverable:** A short checklist of requirements, each labelled `Required`, `Requires clarification`, or `Not authorized`.

### Task 2: Review the starter script with GitHub Copilot (7 minutes)

Open `runbook_automation_starter.py` in VS Code. Use GitHub Copilot Chat to perform a static review against the two runbook documents.

Inspect:

- Path confinement and the possibility of escaping the exercise root.
- Candidate selection and age-threshold validation.
- Dry-run behaviour and any filesystem changes that still occur.
- Approval-gate limitations.
- Destination collisions.
- Move verification and behaviour after partial failure.
- Audit logging and error handling.
- Repeated runs and restart behaviour.
- Whether the script proves that disk utilization decreased or the incident was resolved.

For each finding, capture:

1. Severity.
2. Relevant code or function.
3. Observed behaviour.
4. Possible consequence.
5. Recommended fix or control.
6. Whether it is a confirmed code issue, a residual risk, or a requirement needing clarification.

Challenge Copilot's output with this follow-up:

> Which findings are directly demonstrated by the code, and which are only potential risks or assumptions? Point to the code evidence for each confirmed finding. Do not modify the file or claim that tests were run.

**Deliverable:** A prioritized list of at least three findings, including one safety control and one test recommendation.

### Task 3: Define a safe test plan (7 minutes)

Prepare a test plan before making any approved file movement. Include at least six tests:

- Invalid or negative age threshold.
- A path outside the exercise root.
- Dry-run mode leaves files in their original locations.
- A recent `.log` file is not selected.
- A non-log file is not selected.
- An existing destination filename is handled without overwriting.
- An eligible file is moved only when the exercise approval gate is satisfied.
- Successful movement is independently verified.
- A permission error or failed move is reported clearly.
- A partial failure does not produce a misleading overall success message.
- Repeated execution is safe and predictable.
- Audit evidence records what was planned, attempted, completed, and failed.

For each test, specify:

- **Setup:** Files, paths, and arguments required.
- **Action:** What you would do.
- **Expected result:** What should happen.
- **Control verified:** The safety or reliability requirement being tested.
- **Execution status:** `Planned`, `Run and passed`, `Run and failed`, or `Not run`.

Do not describe a planned test as passed. If you have not run tests, label them `Planned` or `Not run`.

**Deliverable:** A test matrix with at least six cases.

### Task 4: Perform a controlled dry-run review (6 minutes)

Only after the facilitator confirms the exercise copy and paths are correct:

1. Inspect the script's command-line options and default behaviour.
2. Confirm the configured root is the supplied `sample_server` exercise directory.
3. Use dry-run mode, without the approval flag, if the facilitator authorizes execution.
4. Compare the reported candidates with the files actually present in `sample_server/logs/`.
5. Confirm that the files remain in their original locations and that no files were deleted.
6. Record any mismatch, unexpected filesystem change, unclear message, or missing audit evidence.

If execution is not authorized or you cannot confirm the paths, do not run the script. Complete this task as a proposed test and mark it `Not run`.

**Deliverable:** A brief dry-run observation record with the command or mode used, expected behaviour, observed behaviour, and execution status. Do not include secrets or unrelated local file paths.

### Task 5: Recommend the next safe step (4 minutes)

Choose one outcome:

- `Proceed with the local training exercise`
- `Proceed only after specified fixes`
- `Stop and escalate for clarification`

State the evidence behind your choice. List the changes needed before any approved archive move in the exercise. Separately list the additional authorization, monitoring, rollback or recovery, audit, and operational validation controls that would be needed before adapting the design for a real environment.

Do not treat the training `--approve` flag as real production authorization.

**Deliverable:** A short decision note with a recommendation, evidence, blockers, and next steps.

## Final submission checklist

- [ ] Runbook-to-control checklist.
- [ ] Prioritized static code-review findings.
- [ ] Test matrix with accurate execution statuses.
- [ ] Dry-run observation record, or a clear `Not run` explanation.
- [ ] Final recommendation and list of required controls.

## Success criteria

You have completed the lab successfully when you can explain:

- Why dry-run mode is important and what it does not guarantee.
- Why a command-line approval flag is not equivalent to organizational authorization.
- How path confinement, destination collision handling, error handling, and verification reduce operational risk.
- Why audit logs should distinguish planned, attempted, successful, and failed actions.
- Why a successful file move does not prove that disk utilization decreased or that an incident is resolved.
- Which findings are supported by code evidence and which require clarification or further testing.

