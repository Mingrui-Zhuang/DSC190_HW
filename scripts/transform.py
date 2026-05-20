import pandas as pd
import os

input_path = "data/clean/events.csv"
output_path = "data/transformed/events.csv"

df = pd.read_csv(input_path)

df["date"] = pd.to_datetime(
    df["timestamp"]
).dt.strftime("%Y-%m-%d")

os.makedirs("data/transformed", exist_ok=True)

df.to_csv(output_path, index=False)

print("Transform stage complete.")