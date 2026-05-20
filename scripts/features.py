import pandas as pd

input_path = "data/transformed/events.csv"
output_path = "data/features/events.csv"

df = pd.read_csv(input_path)

df["duration_minutes"] = (
    df["duration_seconds"] / 60
)

df["weekday"] = pd.to_datetime(
    df["date"]
).dt.day_name()

df.to_csv(output_path, index=False)

print("Feature stage complete.")