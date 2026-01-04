import pandas as pd, os

input_file = os.getenv("CSV_FILE", "/data/input.csv")
output_file = os.getenv("PARQUET_FILE", "/data/output.parquet")

print(f"📂 Reading CSV from {input_file}")
df = pd.read_csv(input_file)

print("🔄 Converting to Parquet...")
df.to_parquet(output_file, engine="pyarrow", index=False)

print(f"✅ Parquet file written to {output_file}")
