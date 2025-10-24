# gold_rate_checker/checker.py

from typing import Dict, Any, Optional

def parse_gold_rate(api_response: Dict[str, Any]) -> Optional[float]:
    """
    Parse a JSON-like response and return gold rate as float.
    Example input:
    {"metadata": {"currency": "INR"}, "rates": {"gold_per_gram": "6250.50"}}
    """
    try:
        value = api_response["rates"]["gold_per_gram"]
        return float(value)
    except (KeyError, TypeError, ValueError):
        return None


def should_alert(current_rate: float, threshold: float) -> bool:
    """Return True if rate crosses the threshold (>= threshold)."""
    return current_rate >= threshold
