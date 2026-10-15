# MC-II Hands-on - Grounding Without Building RAG

Title: Diagnose the model, improve the result
Time: 25 minutes 
Tool: Copilot Chat 

**Deliverables:**
1.	Original prompt and its weakness.
2.	Improved prompt and response.
3.	Two unsupported claims or assumptions they checked.
4.	One limitation that prompting alone could not resolve.

**Ground rules:**
- Use only the supplied exercise data.
- Do not modify source data.
- Do not execute operational actions.
- Do not treat hypotheses as confirmed facts.
- Verify important calculations and claims.

## Data Track Tasks

### Task 1: investigate transaction quality
**Sample transaction dataset:**

transaction_id,amount,currency
T101,1200,INR
T102,850,INR
T103,,INR
T104,-250,INR
T105,700,USD

**Initial prompt:**
Analyze this transaction data and tell me whether it is correct.

**Participant task:**
Identify why this request is underspecified, then replace it with a more precise prompt.

**Files required:*
None. The incident record is embedded in the slide.

### Task 2: Use a larger dataset and a more precise prompt
Dataset: `data_quality_incidents_24.csv` with 24 data-quality incidents.

Synthetic data-quality incidents covering missing values, duplicate candidates, invalid dates, unrecognized codes, currency issues, numeric anomalies and potential remediation risks.

**Lab activities:**
- Prioritize exceptions
- Develop read-only SQL validation checks
- Identify secondary risks
- Decide when data-owner approval is required.

**TODOs:**
- Use a better prompt to investigate this dataset.
- You may use the same prompt you created in Task #1 and modify it for this task.
- Deliverables and rules remain the same as listed above.

## Enterprise Ops Track Tasks

### Task 1: investigate an incident
**Sample incident record:**

Incident: INC-3091
Service: Customer API
Alert: Disk utilization at 92%
Trend: Increased from 78% over 30 minutes
Customer impact: Intermittent API timeouts reported
Recent change: Unknown
Available evidence: Disk utilization alert only

**Initial prompt:**
Tell me how to fix this incident.

**Participant task:**
Identify why this prompt could lead to unsupported or risky remediation recommendations.

**Files required:*
None. The incident record is embedded in the slide.

### Task 2: Use a larger dataset and a more precise prompt
Dataset: `datasets/enterprise_ops_incidents_20.csv` | 20 records

Operational incidents covering API availability, payment performance, identity security, database capacity, backups, batch jobs, data pipelines and file transfers.

**Lab activities:**
- Prioritize incidents
- Assess SLA indicators
- Separate evidence from hypotheses
- Identify safe diagnostics
- Flag actions requiring human approval.

**TODOs:**
- Use a better prompt to investigate this dataset.
- You may use the same prompt you created in Task #1 and modify it for this task.
- Deliverables and rules remain the same as listed above.

