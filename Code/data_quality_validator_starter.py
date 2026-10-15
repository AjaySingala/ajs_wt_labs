from dataclasses import dataclass

@dataclass
class Transaction:
    transaction_id: str
    customer_id: str
    transaction_date: str
    product_code: str
    currency_code: str
    amount: float
    status: str

VALID_CURRENCIES = {"INR", "USD", "EUR"}
VALID_PRODUCTS = {"PAY", "DAT", "OPS", "SEC", "ANL"}

def validate_transaction(tx: Transaction) -> list[dict]:
    """Return deterministic validation findings."""
    raise NotImplementedError
