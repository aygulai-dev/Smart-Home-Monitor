"""Simulated smart home sensor data."""
import random


def get_sensor_data():
    """Return one random sensor reading."""
    return {
        "temperature": random.randint(18, 40),  # °C
        "humidity": random.randint(15, 80),     # %  (range now includes dry air)
        "energy": random.randint(100, 600),     # W
    }
