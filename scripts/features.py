import pandas as pd
import os

input_path = "data/transformed/events.csv"
output_path = "data/features/events.csv"

df = pd.read_csv(input_path)

df["duration_minutes"] = (
    df["duration_seconds"] / 60
)

df["weekday"] = pd.to_datetime(
    df["date"]
).dt.day_name()

os.makedirs("data/features", exist_ok=True)

df.to_csv(output_path, index=False)

print("Feature stage complete.")