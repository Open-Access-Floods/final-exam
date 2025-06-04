import os
import pandas as pd

# Path to folder containing RS weather station files
folder_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/INMET2024"

# List to collect all monthly summaries
all_dfs = []

for filename in os.listdir(folder_path):
    if filename.endswith(".CSV") and filename.startswith("INMET_S_RS"):
        file_path = os.path.join(folder_path, filename)

        # Extract coordinates from lines 5 and 6 (index 4 and 5)
        with open(file_path, encoding="latin1") as f:
            lines = f.readlines()
            latitude = lines[4].split(";")[-1].strip().replace(",", ".")
            longitude = lines[5].split(";")[-1].strip().replace(",", ".")

        # Load data from row 9 onwards (index 8)
        df = pd.read_csv(file_path, skiprows=8, sep=";", encoding="latin1")

        # Find and rename the precipitation column
        for col in df.columns:
            if "PRECIPITA" in col.upper():
                df.rename(columns={col: "precipitation_mm"}, inplace=True)

        # Parse date and filter valid rows
        df["date"] = pd.to_datetime(df["Data"], errors="coerce", format="%Y/%m/%d")
        df["precipitation_mm"] = pd.to_numeric(df["precipitation_mm"], errors="coerce")
        df.dropna(subset=["date", "precipitation_mm"], inplace=True)

        # Add month column
        df["month"] = df["date"].dt.strftime("%Y-%m")

        # Aggregate precipitation per month
        monthly = df.groupby("month", as_index=False)["precipitation_mm"].sum()

        # Add station info
        monthly["station_file"] = filename
        monthly["latitude"] = float(latitude)
        monthly["longitude"] = float(longitude)

        all_dfs.append(monthly)

# Concatenate all results
final_df = pd.concat(all_dfs, ignore_index=True)

# Save to CSV
output_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_pre_processed/monthly_rainfall_stations_rs.csv"
final_df.to_csv(output_path, index=False)

print("✅ CSV with English headers saved successfully!")