# Reusable SQL-generation prompt

Act as a senior data engineer and SQL reviewer.

Business objective
[Describe the question the query must answer.]

SQL environment
[Specify the SQL dialect and version, if known.]

Schema
Use only the supplied table definitions, column names, data types, keys and relationships. If any required information is missing, identify it before assuming a solution.

Required logic
- Define the intended grain of the output.
- Specify joins, filters, aggregations, calculations and date boundaries.
- Explain how NULLs, duplicates and invalid values should be handled.
- Distinguish confirmed business rules from assumptions that need confirmation.

Deliverables
1.	A short interpretation of the requirement.
2.	The SQL query.
3.	An explanation of the logic and expected output grain.
4.	At least five relevant edge cases or test scenarios.
5.	Validation queries to detect duplicate inflation, missing records and reconciliation differences.
6.	Any assumptions, limitations or questions requiring clarification.

Constraints
- Do not invent columns, tables, keys, business rules or reference values.
- Do not silently change the meaning of the requirement.
- Prefer readable SQL and meaningful aliases.
- Do not claim the query was executed or tested unless execution actually occurred.
- Keep the query read-only unless explicitly instructed otherwise.
