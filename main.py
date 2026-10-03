"""Smart Home Monitor - live simulation with CSV logging."""
import csv
import os
import time
from datetime import datetime

from data import get_sensor_data
from rules import risk_score, status_label

LOG_FILE = "readings.csv"
INTERVAL_SECONDS = 2
ICONS = {"NORMAL": "🟢", "WARNING": "🟡", "CRITICAL": "🔴"}


def print_reading(data, status):
    print("\n" + "=" * 35)
    print("SMART HOME MONITOR (LIVE)")
    print("=" * 35)
    print(f"Temperature: {data['temperature']}°C")
    print(f"Humidity:    {data['humidity']}%")
    print(f"Energy:      {data['energy']}W")
    print(f"{ICONS[status]} Status: {status}")
    print("=" * 35)


def main():
    is_new_file = not os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if is_new_file:
            writer.writerow(
                ["time", "temperature", "humidity", "energy", "risk", "status"]
            )

        try:
            while True:
                data = get_sensor_data()
                risk = risk_score(data)
                status = status_label(risk)

                print_reading(data, status)

                writer.writerow([
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    data["temperature"], data["humidity"], data["energy"],
                    risk, status,
                ])
                f.flush()

                time.sleep(INTERVAL_SECONDS)
        except KeyboardInterrupt:
            print(f"\nStopped by user. Readings saved to {LOG_FILE}")


if __name__ == "__main__":
    main()
