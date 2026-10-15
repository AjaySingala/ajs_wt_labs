# Hands-on Lab 4 - Problem Solving and Prototyping

**Tools:* GitHub Copilot

## Enterprise Ops task
Use the ticket triage starter:
`Code/ticket_triage_starter.py`
`Code/test_ticket_triage.py`

_Apply the documented training rules:_
- P1 tickets require escalation.
- Tickets exceeding their SLA limit require escalation.
- An SLA breach occurs only when elapsed time is strictly greater than the SLA limit.
- Invalid input must be rejected.
- The output must explain the decision.

Define business rules in Copilot Chat, implement them with GitHub Copilot, generate tests and identify human approval points.

**Your objective:**
Produce a small, testable prototype that implements explicit requirements, handles expected edge cases, and includes automated tests.

## Data task
Scenario: The WinTrust data team must assess whether a transaction dataset is suitable for downstream reporting.

Use this sequence:
INSPECT SCHEMA → DEFINE RULES → GENERATE SQL → REVIEW → EXECUTE → VALIDATE RESULTS
- Inspect schema: confirm the actual columns and types.
- Define rules: agree what constitutes a defect.
- Generate SQL: use Copilot to produce individual checks.
- Review: challenge the generated queries before execution.
Only if environment available to run SQL queries:
- Execute: run them against the dataset.
- Validate results: manually inspect sample records and reconcile counts.

Participants should not alter source data to make the checks pass. They should report the defects and their implications.

Participants should:
1.	Inspect the CSV headers and confirm the schema.
2.	Ask GitHub Copilot to translate the agreed rules into SQL.
3.	Execute the checks in the selected SQL environment.
4.	Investigate flagged records.
5.	Review false positives, missed cases, and assumptions.
6.	Produce a concise data-quality summary.

**Files and tools:**
- `transactions_500.csv`

By the end of the exercise, each group should produce:
- A confirmed source schema.
- SQL queries for the agreed data-quality checks.
- Results from actually executing the queries, where the SQL environment is available.
- A summary of defect counts by rule.
- A small set of manually verified records.
- One limitation or unresolved business rule.
- One recommendation for improving upstream data quality.
