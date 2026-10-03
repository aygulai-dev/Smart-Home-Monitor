"""Simple tests for the rule-based logic. Run with: python test_rules.py"""
from rules import risk_score, status_label


def test_normal():
    assert risk_score({"temperature": 22, "humidity": 50, "energy": 300}) == 0


def test_one_rule():
    assert risk_score({"temperature": 35, "humidity": 50, "energy": 300}) == 1


def test_all_rules():
    assert risk_score({"temperature": 35, "humidity": 20, "energy": 550}) == 3


def test_boundaries_are_not_violations():
    # exactly on the limit must NOT count as a violation
    assert risk_score({"temperature": 30, "humidity": 30, "energy": 500}) == 0


def test_status_labels():
    assert status_label(0) == "NORMAL"
    assert status_label(1) == "WARNING"
    assert status_label(2) == "CRITICAL"
    assert status_label(3) == "CRITICAL"


if __name__ == "__main__":
    test_normal()
    test_one_rule()
    test_all_rules()
    test_boundaries_are_not_violations()
    test_status_labels()
    print("All tests passed ✅")
