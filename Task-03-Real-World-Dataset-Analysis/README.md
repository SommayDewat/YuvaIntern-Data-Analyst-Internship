# Task 3: Real-World Dataset Analysis — Seoul Bike Sharing Demand

**YuvaIntern | Data Analyst Internship**

## 1. Project Overview

This project focuses on analyzing a real-world dataset to understand the factors associated with bike-sharing demand. The analysis uses the Seoul Bike Sharing Demand dataset, which contains hourly rental information alongside weather conditions, calendar information, and operational indicators.

The primary objective is to demonstrate a complete data analysis workflow, including dataset inspection, data quality assessment, cleaning, exploratory data analysis (EDA), visualization, statistical summaries, and business insight generation.

The project emphasizes converting raw data into meaningful findings that can support operational planning and data-driven decision-making.

## 2. Project Objectives

- Identify a reliable, publicly available real-world dataset.
- Understand the dataset's structure, variables, and data types.
- Assess missing values, duplicate records, invalid values, and potential outliers.
- Clean and standardize the dataset while preserving valid observations.
- Explore hourly, seasonal, and weekday-versus-weekend rental patterns.
- Examine relationships between weather variables and bike rentals.
- Create clear visualizations and summarize key findings.
- Document the analysis in a Jupyter Notebook and a Word report.

## 3. Dataset Information

| Attribute | Details |
|---|---|
| Dataset name | Seoul Bike Sharing Demand |
| Source | UCI Machine Learning Repository |
| Original observations | 8,760 hourly records |
| Original features | 14 columns |
| Geographic coverage | Seoul, South Korea |
| Time period | December 2017 – November 2018 |
| Data frequency | Hourly |
| License | CC BY 4.0 |

**Official dataset:** [UCI Seoul Bike Sharing Demand](https://archive.ics.uci.edu/dataset/560/seoul%2Bbike%2Bsharing%2Bdemand)

The dataset includes bike rental counts, date and hour information, temperature, humidity, wind speed, visibility, solar radiation, rainfall, snowfall, season, holiday status, and functioning-day information.

## 4. Tools and Technologies

- **Python:** Main programming language for data analysis.
- **Pandas:** Data manipulation, cleaning, grouping, and aggregation.
- **NumPy:** Numerical operations and feature derivation.
- **Matplotlib:** Data visualization.
- **Jupyter Notebook:** Interactive analysis and documentation.
- **python-docx:** Generation of the Word analysis report.
- **Git and GitHub:** Version control and project documentation.

## 5. Project Workflow

### Step 1 — Dataset Inspection

The original dataset was inspected to understand its dimensions, columns, data types, statistical characteristics, and data quality.

### Step 2 — Data Cleaning

The cleaning process included:

- Standardizing column names for easier analysis.
- Parsing date information into a suitable date format.
- Checking missing values and duplicate records.
- Checking duplicate date-hour combinations.
- Validating values against expected data domains.
- Identifying potential outliers in rental counts.

The cleaning checks did not identify missing values, exact duplicate rows, duplicate date-hour keys, or domain validity issues. All 8,760 records were retained.

Potential outliers were flagged for investigation rather than automatically removed, because unusually high demand can represent genuine rental activity.

### Step 3 — Exploratory Data Analysis

The analysis examined:

- Overall rental demand and summary statistics.
- Average demand by hour of the day.
- Seasonal differences in bike rentals.
- Weekday and weekend demand.
- Correlations between rental counts and numerical variables.
- The relationship between temperature and rental demand.
- The distribution of rental counts and potential outliers.

### Step 4 — Visualization and Reporting

Charts and summary tables were generated to communicate patterns clearly. The findings were documented in a Jupyter Notebook and a standalone Word report.

## 6. Key Findings

### Overall Demand

- **Total rentals:** 6,172,314
- **Average hourly rentals:** Approximately 704.6
- **Median hourly rentals:** 504.5
- **Highest recorded hourly rentals:** 3,556
- **Peak recorded hour:** 18:00 on 19 June 2018

The difference between the mean and median indicates that rental demand is not evenly distributed across all hours.

### Hourly Demand

The highest average rental demand occurred at **18:00**, with approximately 1,503 rentals per hour. This suggests that evening travel periods are important when planning bike availability.

### Seasonal Demand

| Season | Average hourly rentals |
|---|---:|
| Summer | 1,034.07 |
| Autumn | 819.60 |
| Spring | 730.03 |
| Winter | 225.54 |

Summer recorded the highest average demand, while winter recorded the lowest. This seasonal variation may help operators plan fleet availability and maintenance schedules.

### Weekday vs. Weekend

- **Weekday average:** 719.45 rentals per hour
- **Weekend average:** 667.34 rentals per hour

Average demand was higher on weekdays than weekends in this dataset. This pattern may be useful for staffing and bike redistribution planning.

### Correlation Analysis

The strongest positive correlations with rental counts among the examined variables were:

| Variable | Correlation with rentals |
|---|---:|
| Temperature | 0.539 |
| Hour | 0.410 |
| Dew point temperature | 0.380 |
| Solar radiation | 0.262 |
| Visibility | 0.199 |
| Month | 0.134 |

Temperature showed the strongest positive correlation among these variables. However, correlation does not establish causation, and hourly or seasonal patterns may also influence demand.

## 7. Visualizations

The project generates the following visualizations:

- `hourly_demand.png` — Average bike rentals by hour.
- `seasonal_demand.png` — Seasonal differences in demand.
- `weekday_weekend_summary.csv` — Summary of weekday and weekend demand.
- `temperature_vs_rentals.png` — Relationship between temperature and rental counts.
- `rental_distribution.png` — Distribution of rental counts.
- `correlation_heatmap.png` — Correlations among numerical variables.

Additional CSV summary tables and a JSON data quality report are included in the results directory.

## 8. Business Implications

The findings suggest several practical opportunities for a bike-sharing operator:

1. **Peak-hour planning:** Prepare for higher demand during the evening, especially around 18:00.
2. **Seasonal resource allocation:** Consider greater bike availability during summer and lower demand during winter.
3. **Weather-aware planning:** Include temperature and weather conditions in demand monitoring and future forecasting models.
4. **Operational scheduling:** Use weekday and weekend demand patterns to support redistribution and staffing decisions.
5. **Outlier investigation:** Review unusually high rental counts before removing them, as they may represent genuine demand peaks.

These are recommendations based on exploratory patterns, not proven causal effects.

## 9. Project Structure

```text
Task-03-Real-World-Dataset-Analysis/
├── data/
│   └── SeoulBikeData.csv
├── notebooks/
│   └── 01_seoul_bike_demand_analysis.ipynb
├── src/
│   ├── inspect_dataset.py
│   ├── clean_dataset.py
│   ├── run_eda.py
│   └── create_deliverables.py
├── results/
│   ├── cleaned_seoul_bike_data.csv
│   ├── data_quality_report.json
│   ├── overall_kpis.csv
│   ├── hourly_demand.png
│   ├── seasonal_demand.png
│   ├── temperature_vs_rentals.png
│   ├── rental_distribution.png
│   ├── correlation_heatmap.png
│   └── 01_seoul_bike_demand_analysis_executed.ipynb
└── reports/
    ├── Task3_Real_World_Dataset_Analysis_Report.docx
    └── Task3_Portal_Submission_Description.txt
```

## 10. How to Run the Analysis

Run the following commands from the main repository directory in PowerShell, with the project's virtual environment activated.

**Inspect the dataset:**

```powershell
python ".\Task-03-Real-World-Dataset-Analysis\src\inspect_dataset.py"
```

**Clean the dataset:**

```powershell
python ".\Task-03-Real-World-Dataset-Analysis\src\clean_dataset.py"
```

**Run exploratory data analysis:**

```powershell
python ".\Task-03-Real-World-Dataset-Analysis\src\run_eda.py"
```

**Generate the notebook, Word report, and portal description:**

```powershell
python ".\Task-03-Real-World-Dataset-Analysis\src\create_deliverables.py"
```

To execute the notebook, change into the Task 3 directory first:

```powershell
Set-Location ".\Task-03-Real-World-Dataset-Analysis"
python -m nbconvert --to notebook --execute ".\notebooks\01_seoul_bike_demand_analysis.ipynb" --output "01_seoul_bike_demand_analysis_executed.ipynb" --output-dir ".\results"
```

## 11. Deliverables

- Cleaned dataset.
- Data quality report.
- Exploratory analysis and visualization outputs.
- Jupyter Notebook containing the analysis.
- Word report documenting the findings and business implications.
- Portal submission description.

## 12. Limitations

- The dataset represents a specific city and a limited historical period.
- Observed associations do not prove that weather or time variables cause changes in demand.
- Correlation analysis alone cannot isolate the independent effect of each variable.
- The analysis is exploratory and does not constitute a validated forecasting model.
- Potential outliers were flagged for review and retained rather than removed automatically.

## 13. Conclusion

This project demonstrates an end-to-end exploratory data analysis workflow using a real-world bike-sharing dataset. The analysis identified hourly and seasonal demand patterns, compared weekday and weekend activity, examined relationships between weather variables and rental counts, and assessed data quality.

The results provide practical insights for demand monitoring and operational planning while highlighting the limitations of descriptive and correlation-based analysis.

**Dataset attribution:** Seoul Bike Sharing Demand dataset, UCI Machine Learning Repository, licensed under CC BY 4.0.

**Repository:** [YuvaIntern Data Analyst Internship](https://github.com/SommayDewat/YuvaIntern-Data-Analyst-Internship)
