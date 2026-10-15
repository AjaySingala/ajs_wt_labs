# Participant Task Brief: Customer 360 Transformation

## Your role
You are a data engineer creating a repeatable Customer 360 dataset from the supplied customer, account and interaction extracts.

## Tasks
1. Inspect all four CSVs and document grain, keys, relationships and quality risks.
2. Produce a source-to-target mapping.
3. Use Copilot Chat to draft a transformation specification before generating SQL or Python/pandas.
4. Use GitHub Copilot to generate, explain and review the implementation.
5. Aggregate accounts and interactions separately to customer grain before joining.
6. Preserve orphan account and interaction records in separate exception outputs.
7. Flag repeated-looking interactions without deleting them.
8. Normalize email by trimming and lowercasing. Do not invent missing contact details.
9. Create reconciliation checks and tests for counts, unknown IDs, multiple child records, missing values and rerun consistency.
10. Record unresolved questions, including how interaction success should be defined.

## Deliverables
- Source-to-target mapping
- Transformation SQL or Python/pandas code
- Customer-level target definition
- Orphan account and interaction exception outputs or queries
- Duplicate-candidate report/query
- At least six test cases with expected behaviour
- Reconciliation checklist and results, if executed
- Short design note listing assumptions, risks and unresolved questions

## Constraints
Do not modify source files, silently drop unmatched records, automatically delete duplicate candidates, or treat SUCCESS and COMPLETED as equivalent without approval. Do not claim execution if code was only generated or reviewed.
