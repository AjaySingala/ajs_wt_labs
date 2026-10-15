# Reusable ETL-generation prompt

Act as a senior data engineer designing a repeatable ETL transformation.

Business objective
[Describe the desired data product or target dataset.]

Source and target
Use the supplied source schema, target schema, data dictionary and approved transformation rules.

Transformation requirements
- Specify the source-to-target mapping for each field.
- Define type conversions, normalization and validation.
- Identify missing, invalid and conflicting values.
- State the deduplication key and deterministic survivor-selection rule, if documented.
- Define how rejected records and exceptions are represented.
- Explain whether the transformation is a full refresh or incremental load.
- Specify how reruns, late-arriving records and previously processed records are handled.

Deliverables
1.	Transformation specification.
2.	SQL or Python/pandas implementation, with the selected technology justified.
3.	Assumptions and unresolved business questions.
4.	Unit tests for normal, boundary and invalid cases.
5.	Reconciliation checks for input count, output count, rejected records and relevant totals.
6.	A failure and recovery analysis.

Do not invent source columns, target fields, reference mappings, business rules or primary keys. Do not silently discard records. 

Do not claim the transformation was executed or tested unless it actually was. 

Keep the raw source unchanged and make the proposed transformation reviewable.
