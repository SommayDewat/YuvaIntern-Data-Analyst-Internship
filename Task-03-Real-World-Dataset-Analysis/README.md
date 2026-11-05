# Task 03 – Real-World Dataset Analysis: Seoul Bike Sharing Demand

## Objective
Explore hourly Seoul bike rentals, assess data quality, identify time and weather relationships, and communicate evidence-based operational insights.

## Dataset
- Source file: `data/SeoulBikeData.csv`
- 8,760 hourly observations and 14 original columns
- Coverage: 1 December 2017 – 30 November 2018

## Project structure
```text
Task-03-Real-World-Dataset-Analysis/
├── data/
│   └── SeoulBikeData.csv
├── notebooks/
│   └── 01_seoul_bike_demand_analysis.ipynb
├── reports/
│   ├── Task3_Real_World_Dataset_Analysis_Report.docx
│   └── Task3_Portal_Submission_Description.txt
└── results/
    ├── cleaned_seoul_bike_data.csv
    ├── data_quality_report.json
    ├── summary CSV files
    ├── chart PNG files
    └── 01_seoul_bike_demand_analysis_executed.ipynb
```

## Methods
Pandas and NumPy are used for inspection, cleaning, feature engineering, descriptive statistics, grouping and correlation. Matplotlib is used for histograms, line charts, bar charts, boxplots, scatterplots and a correlation heatmap. Outliers are flagged using the IQR rule and retained for investigation rather than deleted automatically.

## Main findings
- Total rentals: 6,172,314; mean hourly rentals: 704.60.
- Highest average demand hour: 18:00 (1502.93); lowest: 04:00 (132.59).
- Summer average demand is 4.58 times winter average demand.
- Weekday average demand is 7.8% higher than weekend average.
- Temperature correlation: 0.539; humidity correlation: -0.200.

## Reproducibility
Open the notebook in Jupyter from the project folder and run all cells. It expects the source CSV in `data/` and writes outputs to `results/`. Python packages: pandas, numpy, matplotlib, jupyter, nbclient. The original CSV is not modified.

## Limitations
This is descriptive analysis of one year of aggregate hourly data. Correlation does not imply causation; station-level allocation and predictive performance are outside this project's scope.
