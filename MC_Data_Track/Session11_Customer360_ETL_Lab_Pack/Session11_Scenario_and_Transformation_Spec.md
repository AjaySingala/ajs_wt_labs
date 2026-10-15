# Session 11 Lab: Customer 360 Data Product
All records are synthetic. This is a fictional financial-services scenario, not a real WinTrust data model.

## Scenario
Prepare a curated customer-level analytical dataset from customer profiles, account records and interaction events. The transformation must be repeatable, auditable and preserve records that cannot be matched.

## Source files and grain
- `customer_source.csv`: one row per source customer, key `source_customer_id`.
- `account_source.csv`: one row per account, key `account_id`; multiple accounts per customer are possible.
- `interaction_source.csv`: one row per interaction event, key `interaction_id`; multiple interactions per customer are possible.
- `reference_values.csv`: code descriptions by domain. Validate using both code and domain.

## Proposed target: customer_360
One row per customer profile. 

Suggested fields: customer_id, full_name_clean, email_normalized, phone_normalized, customer_status, segment, country_code, account_count, active_account_count, total_account_balance_inr, latest_account_opened_date, interaction_count, latest_interaction_timestamp, successful_interaction_count.

The target is a proposed exercise contract. 
Define assumptions. 
In particular, SUCCESS and COMPLETED are different source statuses. 
Do not combine them as equivalent without clarification.

## Rules
- Keep raw files unchanged.
- Trim text used in comparisons; lowercase email after trimming.
- Do not invent missing email addresses or phone numbers.
- Do not merge profiles based only on matching names or email addresses.
- Send account and interaction records with unknown customer IDs to separate exception outputs, not silent deletion.
- Validate reference codes using both `reference_code` and `reference_domain`.
- Aggregate accounts and interactions independently to customer grain before joining to customer profiles. This avoids row multiplication.
- All sample account balances are INR, but document/validate the assumption before aggregation.
- Flag repeated-looking interaction rows for investigation; do not delete them without an approved deduplication rule.
- A rerun with unchanged inputs and rules should produce the same outputs.
- No source data may be updated in place.

## Deliberate edge cases
- Missing phone; mixed email casing; 
- unknown customer ID in an account; 
- unknown customer ID in an interaction; 
- repeated-looking interactions; 
- multiple accounts/interactions per customer; 
- closed accounts; 
- different interaction statuses.

## Required behaviour
- Inspect schemas and counts; 
- create source-to-target mapping; 
- create one row per source customer; 
- preserve orphan accounts/interactions in exception outputs; 
- report duplicate candidates; 
- reconcile counts; 
- test missing values, 
- multiple child records, 
- unknown IDs and 
- rerun consistency. 

No database dialect is mandated. 
State the chosen dialect or runtime and do not claim execution unless actually run.
