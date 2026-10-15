# Session 10 Hands-on Lab: Operational Ticket Triage and Runbook-Guided Response

**Track:** Enterprise Ops only  
**Duration:** 25 minutes  
**Tools:** Microsoft Copilot Chat, GitHub Copilot in VS Code  
**Scenario:** Synthetic operational tickets and an API latency incident

> **Important:** All files and rules in this exercise are fictional training materials, not approved WinTrust production policy. This is a read-only exercise. Do not update tickets, execute operational commands, or connect to production systems.

## 1. Objectives

By the end of this lab, you should be able to:
1. Write a structured prompt for operational ticket triage.
2. Distinguish confirmed facts, hypotheses, and missing evidence.
3. Apply explicit SLA and severity rules without silently changing them.
4. Identify safe read-only diagnostics and actions requiring authorization.
5. Define test cases for a deterministic ticket-triage script.

## 2. Files to use

Use only these new Session 10 exercise files:
- `ops_ticket_triage_mc1_80.csv`: synthetic operational ticket export with 80 base tickets and deliberately included validation cases.
- `Operations_Triage_Exercise_Guide.docx`: exercise rules, validation checks, output expectations, and safety boundaries.
- `Runbook_API_Latency_Exercise.docx`: procedure for investigating API latency.
- `Operational_Scripting_Requirements.docx`: requirements for a deterministic triage function.

Do not use datasets or runbooks from earlier sessions.

## 3. Exercise rules

Use the exercise guide as the authority for this lab:
- An SLA breach occurs only when `elapsed_minutes > sla_target_minutes`.
- Equality at the SLA limit is **not** a breach.
- P1 tickets are recommended for escalation under the exercise rules.
- An SLA breach is recommended for escalation under the exercise rules.
- Supported severity values are P1, P2, P3, and P4.
- Blank ticket IDs, blank descriptions, unsupported severity values, negative elapsed times, and nonpositive SLA targets must be flagged for review.
- Do not infer root cause from a ticket symptom.
- Do not claim that a diagnostic was performed or a ticket was resolved.
- Do not execute actions, update tickets, or contact users.

These are training rules only. Validate applicable operational policy before generalizing them to a real environment.

## 4. Tasks

### Task A: Build a structured triage prompt (5 minutes)

Use Microsoft Copilot Chat. Provide `ops_ticket_triage_mc1_80.csv` and `Operations_Triage_Exercise_Guide.docx`.

Ask Copilot to analyze a small sample first, rather than making unverified claims about every row. Request these fields for each selected ticket:
- Ticket ID and service
- Confirmed facts from the ticket record
- Severity validity
- SLA breach result, including the calculation
- Escalation recommendation and reason codes
- Missing evidence
- Whether human review is required

Require Copilot to apply the exact SLA boundary rule, flag invalid records instead of silently correcting them, separate facts from hypotheses, avoid inventing root causes or policy, and state exactly which records it analyzed.

**Deliverable A:** Save your final prompt in `session10_lab_triage_prompt.md` or include it in your lab notes.

### Task B: Analyze tickets and validate the result (7 minutes)

Ask Copilot to analyze at least five tickets, including:
1. A ticket below its SLA target.
2. A ticket exactly at its SLA target, if available.
3. A ticket above its SLA target.
4. A P1 ticket.
5. An invalid record, such as unsupported severity or a blank description.

Check each selected record against the CSV. Independently calculate the SLA outcome for at least two records. If you cannot find a required case in your sample, search the CSV for a suitable record rather than inventing one.

| Ticket ID | Source values checked | Copilot result | Your verification | Issue or follow-up |
|-----------|-----------------------|----------------|-------------------|--------------------|

**Deliverable B:** A verified sample triage result, with incorrect or unsupported output noted.

### Task C: Prepare an incident assessment (6 minutes)

Use `Runbook_API_Latency_Exercise.docx` and one or more relevant ticket records. Ask Copilot to produce:
1. Confirmed facts
2. Hypotheses, explicitly marked as unconfirmed
3. Missing evidence
4. Safe read-only diagnostics
5. Actions requiring authorization
6. A concise update for an incident lead

Require evidence references to supplied ticket fields or runbook instructions. Challenge at least one hypothesis by asking:

> What evidence proves this cause, and what alternative explanations remain possible?

Do not accept a temporal association as proof of causation.

**Deliverable C:** A short incident assessment separating facts, hypotheses, and evidence gaps.

### Task D: Define tests for a triage script (7 minutes)

Use `Operational_Scripting_Requirements.docx`. You do not need to complete a production implementation during this lab.

Prepare at least six test cases for a deterministic function that accepts one ticket and returns a structured triage result. Include:
- Valid ticket below the SLA target
- Ticket exactly at the SLA target
- Ticket above the SLA target
- P1 escalation
- Unsupported severity
- Missing ticket ID or blank description
- Negative elapsed time or nonpositive SLA target
- Malformed numeric input

For each test, specify the input condition and expected outcome. If time permits, use GitHub Copilot to generate `ticket_triage.py` and `test_ticket_triage.py`, then review the code before executing tests.

**Deliverable D:** A test-case list or unit-test file. Do not claim tests passed unless you executed them.

## 5. Submission checklist

- [ ] Structured triage prompt.
- [ ] Verified sample triage result.
- [ ] At least one invalid record identified and explained.
- [ ] Incident assessment separating facts, hypotheses, and missing evidence.
- [ ] Safe diagnostics distinguished from actions requiring authorization.
- [ ] At least six test cases for the triage logic.
- [ ] No unsupported claims that an incident was resolved or an action was executed.

## 6. Reflection questions

1. Which parts of triage are deterministic rules, and which require human judgment?
2. What can go wrong if `>` is accidentally implemented as `>=`?
3. Why is a ticket summary not the same as verified row-by-row classification?
4. What evidence is needed before authorizing a restart, rollback, or other production change?
5. What controls are required before connecting this utility to a real ticketing system?

## 7. Success criteria

A strong submission is evidence-based, follows the documented exercise rules, identifies uncertainty, flags invalid records, and distinguishes recommendations from execution. A polished AI response without verification is not sufficient.
