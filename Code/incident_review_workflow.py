"""Illustrative deterministic incident review workflow.
Uses synthetic input only. No external systems or operational actions.
"""

def review_incident(incident):
    findings = []

    # Deterministic rules
    if incident["error_rate_pct"] >= 5:
        findings.append("HIGH_ERROR_RATE")

    if incident["db_cpu_pct"] >= 90:
        findings.append("HIGH_DATABASE_CPU")

    if incident["queue_depth"] >= 10000:
        findings.append("HIGH_QUEUE_DEPTH")

    if incident["payment_integrity_confirmed"] is False:
        findings.append("PAYMENT_INTEGRITY_UNCONFIRMED")

    # Fixed workflow: same sequence for every incident
    plan = [
        "Review incident timeline",
        "Check application and dependency telemetry",
        "Review queue health",
        "Verify payment reconciliation status",
        "Prepare findings for incident commander",
    ]

    return {
        "incident_id": incident["incident_id"],
        "findings": findings,
        "review_plan": plan,
        "production_changes_authorized": False,
    }


if __name__ == "__main__":
    sample_incident = {
        "incident_id": "INC-5837",
        "error_rate_pct": 6.8,
        "db_cpu_pct": 94,
        "queue_depth": 12600,
        "payment_integrity_confirmed": False,
    }

    result = review_incident(sample_incident)
    print(result)
