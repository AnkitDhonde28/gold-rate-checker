# tests/test_checker.py
import pytest
from gold_rate_checker.checker import parse_gold_rate, should_alert

def test_parse_gold_rate_valid():
    resp = {"metadata": {"currency": "INR"}, "rates": {"gold_per_gram": "6250.50"}}
    assert parse_gold_rate(resp) == 6250.50

def test_parse_gold_rate_invalid():
    resp = {"no": "value"}
    assert parse_gold_rate(resp) is None

def test_should_alert_true():
    assert should_alert(7000.0, 6500.0) is True

def test_should_alert_false():
    assert should_alert(6000.0, 6500.0) is False
