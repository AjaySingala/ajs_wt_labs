# Data Track - MASTER CLASS 1 - Lab: SQL Query Generation Challenge

**Tools:**
- Copilot Chat and GitHub Copilot (if required).
- SQL execution must take place in an available, approved SQL environment, if one is provided.

Files:
- PayFlow_Schema_and_Business_Context.md
- customers.csv
- payments.csv
- payment_events.csv
- settlement_batches.csv


# PayFlow: Session 9 SQL Query Generation Challenge

All data is synthetic. PayFlow is fictional and is not an actual WinTrust system.

## Scenario
A data team needs to report payment performance and investigate data-quality exceptions across payment transactions, event history, customer records and settlement batches.

## Tables and grain
### customers: one row per customer
- `customer_id` VARCHAR(20), primary key
- `customer_segment` VARCHAR(20)
- `onboarding_date` DATE
- `country_code` CHAR(2)
- `customer_status` VARCHAR(20)

### payments: one row per payment instruction
- `payment_id` VARCHAR(30), primary key
- `customer_id` VARCHAR(20), references `customers.customer_id`; sample includes missing/unmatched values
- `payment_timestamp` TIMESTAMP
- `payment_amount` DECIMAL(18,2)
- `currency_code` CHAR(3)
- `payment_channel` VARCHAR(20)
- `payment_status` VARCHAR(20)
- `merchant_id` VARCHAR(30), nullable
- `settlement_batch_id` VARCHAR(30), nullable

### payment_events: one or more event records per payment
- `event_id` VARCHAR(30), primary key
- `payment_id` VARCHAR(30), references `payments.payment_id`
- `event_timestamp` TIMESTAMP
- `event_type` VARCHAR(30)
- `event_status` VARCHAR(20)
- `source_system` VARCHAR(30)

### settlement_batches: one row per settlement batch
- `settlement_batch_id` VARCHAR(30), primary key
- `settlement_date` DATE
- `currency_code` CHAR(3)
- `batch_status` VARCHAR(20)
- `expected_total` DECIMAL(18,2)
- `actual_total` DECIMAL(18,2), nullable

## Relationships
- One customer can have many payments.
- One payment can have many payment events.
- A payment may reference a settlement batch.
- A batch may be associated with many payments.

## Important constraints
- Multiple events per payment are normal; do not label them all as duplicates.
- The sample includes:
    - missing customer identifiers, 
    - an unmatched customer reference, 
    - missing currency, 
    - a negative amount, 
    - a nullable merchant, 
    - missing actual settlement totals, 
    - and a repeated event pattern for investigation. 
- The sample deliberately does not define all business rules. 
- Do not invent permitted status codes, success-rate definitions, settlement eligibility rules, amount restrictions or currency policy. 
- Blank CSV fields represent missing values.

## PayFlow Data Engineering Challenge
The data team needs two deliverables.

### Deliverable A: Payment performance analysis
Generate a SQL query that reports payment performance by payment date, payment channel and currency.

The output should include:
- Payment date
- Payment channel
- Currency code
- Number of payment records
- Total payment amount
- Number of distinct customers
- Number of payments in each current status, or an equivalent status breakdown

The query must not multiply payment counts or amounts because a payment has multiple event records. State how NULL amounts and missing customer identifiers are handled.

### Deliverable B: Data-quality investigation
Generate read-only SQL checks to identify:
- Payments with missing customer identifiers
- Payments whose customer identifier has no matching customer record
- Payments with missing or blank currency codes
- Duplicate payment identifiers, if the physical dataset permits their detection
- Payments with multiple event records, distinguishing normal event history from potential duplicate events
- Settlement batches where expected and actual totals cannot be compared because the actual total is missing

For each check, return useful record identifiers, an exception reason and a summary count.

### Constraints
- Use only the supplied schema.
- State the SQL dialect you are targeting.
- Do not invent valid status codes, permitted currencies, amount restrictions or settlement eligibility rules.
- Distinguish a structural anomaly from a confirmed business-rule violation.
- Do not modify source data.
- Include test cases and explain how the queries would be validated.
- Do not claim execution or successful validation unless the queries were actually run.

## Three optional challenges (if time permits)

### Challenge 1

**The join multiplication trap:**
A payment has four event records. What happens if the participant joins payments directly to payment_events and then sums payment_amount?

_Expected insight_: the payment amount may be counted four times. Participants should aggregate at the correct grain or use an appropriate query structure before joining.

### Challenge 2

**The ambiguous status rule:**
The business asks for the payment success rate, but provides no definition of a successful payment.

_Expected insight_: participants should ask which statuses qualify, what the denominator is, and whether the current payment status or event history is authoritative. They should not invent the definition.

### Challenge 3

**The missing settlement amount:**
A settlement batch has an expected_total but a NULL actual_total.

_Expected insight_: this is not automatically a zero-value settlement or a confirmed financial discrepancy. It is an unresolved comparison that should be flagged separately.

