import pandas as pd

input_path = "data/clean/events.csv"
output_path = "data/transformed/events.csv"

df = pd.read_csv(input_path)

df["date"] = pd.to_datetime(
    df["timestamp"]
).dt.strftime("%Y-%m-%d")

df.to_csv(output_path, index=False)

print("Transform stage complete.")