import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

ips = [
    "192.0.2.10",
    "198.51.100.20",
    "203.0.113.15",
    "192.0.2.25",
    "198.51.100.30"
]

events = [
    "Successful Login",
    "Failed Login",
    "File Access",
    "Permission Denied",
    "Server Error"
]

logs = []
start = datetime(2026, 10, 25, 9, 0, 0)

# Generate 100 synthetic security events
for i in range(100):
    ip = random.choice(ips)
    event = random.choice(events)
    status = "INFO"
    message = event

    # Simulate repeated failed login attempts
    if i in range(10, 18):
        ip = "203.0.113.15"
        event = "Failed Login"
        status = "WARNING"
        message = "Repeated failed login attempt"

    elif event == "Permission Denied":
        status = "WARNING"

    elif event == "Server Error":
        status = "ERROR"

    elif event == "Failed Login":
        status = "WARNING"

    logs.append({
        "timestamp": (
            start + timedelta(minutes=i * 2)
        ).isoformat(),
        "ip_address": ip,
        "event_type": event,
        "status": status,
        "message": message
    })

# Convert logs into a DataFrame
df = pd.DataFrame(logs)

# Save logs as a CSV file
df.to_csv("synthetic_logs.csv", index=False)

print("Synthetic logs generated successfully!")
print(df.head())
print("\nTotal log events:", len(df))

