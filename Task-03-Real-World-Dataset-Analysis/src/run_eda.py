from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
RESULTS = BASE / "results"
DATA = RESULTS / "cleaned_seoul_bike_data.csv"
RESULTS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Date"])

# Add analytical time features.
df["Month"] = df["Date"].dt.month
df["Weekday"] = df["Date"].dt.day_name()
df["Day_Type"] = df["Weekday"].map(
    lambda day: "Weekend" if day in ["Saturday", "Sunday"] else "Weekday"
)

# 1. Overall KPIs
kpis = {
    "records": int(len(df)),
    "total_rentals": int(df["Rented_Bike_Count"].sum()),
    "average_hourly_rentals": round(float(df["Rented_Bike_Count"].mean()), 2),
    "median_hourly_rentals": round(float(df["Rented_Bike_Count"].median()), 2),
    "maximum_hourly_rentals": int(df["Rented_Bike_Count"].max()),
    "maximum_rental_date": str(
        df.loc[df["Rented_Bike_Count"].idxmax(), "Date"].date()
    ),
    "maximum_rental_hour": int(
        df.loc[df["Rented_Bike_Count"].idxmax(), "Hour"]
    ),
}
pd.DataFrame([kpis]).to_csv(RESULTS / "overall_kpis.csv", index=False)

# 2. Demand by hour
hourly = df.groupby("Hour", as_index=False)["Rented_Bike_Count"].mean()
hourly.to_csv(RESULTS / "hourly_demand_summary.csv", index=False)

# 3. Demand by season
seasonal = (
    df.groupby("Seasons", as_index=False)
    .agg(
        average_rentals=("Rented_Bike_Count", "mean"),
        total_rentals=("Rented_Bike_Count", "sum"),
        observations=("Rented_Bike_Count", "size"),
    )
    .sort_values("average_rentals", ascending=False)
)
seasonal.to_csv(RESULTS / "seasonal_demand_summary.csv", index=False)

# 4. Demand by day type
day_type = (
    df.groupby("Day_Type", as_index=False)["Rented_Bike_Count"]
    .mean()
    .rename(columns={"Rented_Bike_Count": "average_rentals"})
)
day_type.to_csv(RESULTS / "weekday_weekend_summary.csv", index=False)

# 5. Demand by functioning day
functioning = (
    df.groupby("Functioning_Day", as_index=False)["Rented_Bike_Count"]
    .mean()
    .rename(columns={"Rented_Bike_Count": "average_rentals"})
)
functioning.to_csv(RESULTS / "functioning_day_summary.csv", index=False)

# 6. Correlations of numeric variables
numeric = df.select_dtypes(include="number")
correlations = numeric.corr(numeric_only=True)["Rented_Bike_Count"].drop(
    "Rented_Bike_Count"
).sort_values(ascending=False)
correlations.rename("pearson_correlation_with_rentals").to_csv(
    RESULTS / "rental_correlations.csv"
)

# 7. Visualization: hourly average demand
plt.figure(figsize=(10, 5))
plt.plot(hourly["Hour"], hourly["Rented_Bike_Count"], marker="o")
plt.title("Average Bike Rentals by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Rentals")
plt.xticks(range(0, 24))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(RESULTS / "hourly_demand.png", dpi=150)
plt.close()

# 8. Visualization: seasonal demand
plt.figure(figsize=(8, 5))
plt.bar(seasonal["Seasons"], seasonal["average_rentals"])
plt.title("Average Bike Rentals by Season")
plt.xlabel("Season")
plt.ylabel("Average Rentals per Hour")
plt.tight_layout()
plt.savefig(RESULTS / "seasonal_demand.png", dpi=150)
plt.close()

# 9. Visualization: rental distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Rented_Bike_Count"], bins=40, edgecolor="black")
plt.title("Distribution of Hourly Bike Rentals")
plt.xlabel("Rented Bike Count")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(RESULTS / "rental_distribution.png", dpi=150)
plt.close()

# 10. Visualization: temperature vs rentals
plt.figure(figsize=(8, 5))
plt.scatter(
    df["TemperatureC"],
    df["Rented_Bike_Count"],
    alpha=0.25,
    s=12,
)
plt.title("Temperature vs Bike Rentals")
plt.xlabel("Temperature (°C)")
plt.ylabel("Rented Bike Count")
plt.tight_layout()
plt.savefig(RESULTS / "temperature_vs_rentals.png", dpi=150)
plt.close()

# 11. Correlation heatmap for selected variables
selected = [
    "Rented_Bike_Count", "Hour", "TemperatureC", "Humiditypct",
    "Wind_speed_m_s", "Solar_Radiation_MJ_m2", "Rainfallmm", "Snowfall_cm"
]
corr_matrix = df[selected].corr(numeric_only=True)
fig, ax = plt.subplots(figsize=(10, 7))
image = ax.imshow(corr_matrix, aspect="auto", vmin=-1, vmax=1)
ax.set_xticks(range(len(selected)))
ax.set_yticks(range(len(selected)))
ax.set_xticklabels(selected, rotation=60, ha="right")
ax.set_yticklabels(selected)
ax.set_title("Correlation Matrix of Selected Variables")
fig.colorbar(image, ax=ax, label="Pearson correlation")
fig.tight_layout()
fig.savefig(RESULTS / "correlation_heatmap.png", dpi=150)
plt.close(fig)

print("EDA COMPLETED SUCCESSFULLY")
print("\nOVERALL KPIs")
for key, value in kpis.items():
    print(f"{key}: {value}")

print("\nAVERAGE RENTALS BY HOUR")
print(hourly.loc[hourly["Rented_Bike_Count"].idxmax()].to_string())

print("\nSEASONAL DEMAND")
print(seasonal.round(2).to_string(index=False))

print("\nWEEKDAY VS WEEKEND")
print(day_type.round(2).to_string(index=False))

print("\nTOP CORRELATIONS WITH RENTALS")
print(correlations.head(6).round(3).to_string())

print(f"\nOutputs saved to: {RESULTS}")
