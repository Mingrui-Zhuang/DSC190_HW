import pandas as pd
import os

VALID_EVENTS = {
    "click",
    "view",
    "purchase",
    "login",
    "logout"
}

input_path = "data/raw/events.csv"
output_path = "data/clean/events.csv"

df = pd.read_csv(input_path)

# Drop missing rows
df = df.dropna()

# Positive durations only
df = df[df["duration_seconds"] > 0]

df["duration_seconds"] = (df["duration_seconds"].astype(int))

# Valid event type
df = df[df["event_type"].isin(VALID_EVENTS)]

# Normalize timestamp
df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

df = df.dropna(subset=["timestamp"])

df["timestamp"] = (
    df["timestamp"]
    .dt.strftime("%Y-%m-%dT%H:%M:%S")
)

os.makedirs("data/clean", exist_ok=True)

df.to_csv(output_path, index=False)

print("Clean stage complete.")