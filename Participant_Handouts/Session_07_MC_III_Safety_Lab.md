# MASTER CLASS III Hands-on - RISKS, SECURITY & GOVERNANCE
Duration: 25 minutes | Copilot Chat | Both tracks
Tools: Copilot Chat

## Data track
**Files:**
- Session_07_MC_III_Data\Data_Track\Data_Track_Risk_Review_Case.docx
    - Reviews five data-quality scenarios: missing currency, an unknown product code, a possible duplicate, a negative amount, and missing identifiers. The AI's proposed fixes could introduce financial, reconciliation, or identity errors.
- Session_07_MC_III_Data\Data_Track\Data_Track_Risk_Review_Criteria.docx
    - Guides participants in assessing evidence, secondary risks, authoritative reference data, remediation controls, and validation.
The expected outcome is a prioritized investigation plan and a safe remediation proposal, without guessing missing values or modifying source data.

**Objective:**
Evaluate proposed data-quality corrections and redesign them to prevent secondary data-quality problems.

**Participant tasks:**
-	Review the supplied data-quality exceptions and proposed corrections.
-	Identify which corrections are supported by evidence and which rely on assumptions.
-	Assess the potential impact on financial accuracy, reconciliation, customer identity, product attribution, and auditability.
-	Identify missing information, reference data, or business rules required before making a correction.
-	Classify each proposed correction as:
o	Suitable for read-only analysis
o	Requires verification against authoritative evidence
o	Requires human approval
o	Must not proceed as proposed
-	Recommend safe validation checks before and after an approved correction.
-	Prepare a prioritized investigation and remediation plan.
-	Summarize the three highest-risk cases and explain the controls needed.

**Expected output:**
A risk register, a prioritized investigation plan, and a safe remediation proposal. No source data should be modified.

## Enterprise Ops track

**Files:**
- Session_07_MC_III_Data\Enterprise_Ops_Track\Enterprise_Ops_Risk_Review_Case.docx
    - Reviews a simulated Customer API incident with elevated latency, increased errors, high database CPU, and a nearby scheduled export. The proposed AI response recommends potentially disruptive actions without establishing root cause.
- Session_07_MC_III_Data\Enterprise_Ops_Track\Enterprise_Ops_Risk_Review_Criteria.docx
    - Provides the review criteria for operational impact, missing evidence, human approval, recovery considerations, and safer diagnostics.
The expected outcome is a safer incident-response sequence and a stakeholder update that distinguishes facts from hypotheses.

**Objective:**
Evaluate AI-generated operational recommendations and distinguish safe diagnostics from actions that could disrupt production.

**Participant tasks:**
- Review the supplied incident information and the proposed operational response.
- Separate confirmed observations from hypotheses, assumptions, and unsupported conclusions.
- Identify potential risks to service availability, data integrity, security, customers, and diagnostic evidence.
- Assess each proposed action for operational impact and reversibility.
- Identify missing diagnostics, preconditions, ownership information, and approvals.
- Classify actions as read-only diagnostics, low-risk reversible actions, actions requiring human approval, or actions that must not proceed as proposed.
- Develop a safer, ordered incident-response plan that starts with evidence gathering.
- Rewrite the stakeholder update so that it communicates known facts and uncertainty without making unsupported root-cause or recovery-time claims.

**Expected output:**
An operational risk register, a safer incident-response sequence, and a revised stakeholder update. No operational action should be executed.

# Optional Extension: GitHub Copilot Code Review
Tools: GitHub Copilot

## Enterprise Ops Track

**Files:**
- Session_07_MC_III_Data\Code_Review\Enterprise_Ops\unsafe_runbook_automation_review.py

**Objective:**
Use GitHub Copilot to identify security and reliability risks in an operational automation script and propose safer alternatives.

**Participant tasks:**
- Open the supplied Python script in VS Code and inspect its implementation.
- Identify security vulnerabilities, unsafe operations, and reliability weaknesses.
- Pay particular attention to command execution, file deletion, credentials, database operations, HTTP requests, permissions, and error handling.
- Rank findings by severity and explain their potential impact.
- Recommend safer implementation patterns for each significant finding.
- Propose appropriate tests, including failure cases and authorization checks.
- Review the proposed improvements for residual risks and operational assumptions.
- Explain which changes would require additional testing or approval before deployment.

**Expected output:**
A prioritized code-review report, recommended fixes, and a proposed test plan.

**Safety constraint:**
Do not execute the supplied script or any proposed replacement.

## Data Track Prompt

**Files:**
- Session_07_MC_III_Data\Code_Review\Data_SQL\unsafe_resolve_data_quality_exception.sql

**Objective:**
Review a stored procedure for security, data-integrity, and governance weaknesses, then propose a safer design.

**Participant tasks:**
- Open the supplied SQL stored procedure in VS Code and examine its logic.
- Identify security vulnerabilities, unsafe SQL construction, and missing input validation.
- Evaluate transaction handling, rollback, error handling, and authorization.
- Determine whether the procedure adequately validates reference data and business rules before changing records.
- Examine how it handles missing records, unexpected row counts, audit trails, and reconciliation.
- Identify circumstances in which an exception could incorrectly be marked as resolved.
- Propose a safer stored-procedure design and explain the controls it should implement.
- Define validation checks and tests needed before the procedure could be considered for use.
- List schema details, business rules, and governance controls that must be confirmed.

**Expected output:**
A prioritized SQL code-review report, a safer stored-procedure design, and a validation and testing plan.

**Safety constraint:**
Do not execute the supplied SQL or connect it to a database.
