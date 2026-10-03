"""Rule-based risk scoring for the smart home monitor."""

# Thresholds are defined in one place so they are easy to change.
TEMP_LIMIT = 30       # °C, above this the room is too hot
ENERGY_LIMIT = 500    # W,  above this energy use is too high
HUMIDITY_LIMIT = 30   # %,  below this the air is too dry


def risk_score(data):
    """Return a risk score from 0 to 3 (one point per violated rule)."""
    score = 0
    if data["temperature"] > TEMP_LIMIT:
        score += 1
    if data["energy"] > ENERGY_LIMIT:
        score += 1
    if data["humidity"] < HUMIDITY_LIMIT:
        score += 1
    return score


def status_label(score):
    """Convert a risk score to a status name."""
    if score == 0:
        return "NORMAL"
    if score == 1:
        return "WARNING"
    return "CRITICAL"
