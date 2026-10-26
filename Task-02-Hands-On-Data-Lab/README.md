# Task 02 - Hands-On Data Lab Implementation

## Project Overview

This project demonstrates practical data analysis using Python. It covers dataset preparation, data quality validation, exploratory data analysis (EDA), sales aggregation, visualization, and reporting.

The project uses a **synthetic retail sales dataset** containing 20 sample orders. The dataset is created for educational purposes and does not represent actual business transactions.

## Objectives

- Prepare and validate a structured retail sales dataset.
- Use Pandas and NumPy for data manipulation and calculations.
- Analyze sales by product category, region, and month.
- Visualize sales patterns using Matplotlib.
- Export cleaned data, summary tables, charts, and a final report.

## Technology Stack

- Python
- Pandas and NumPy
- Matplotlib
- Jupyter Notebook
- CSV and JSON
- Python-docx for report generation

## Project Structure

```text
Task-02-Hands-On-Data-Lab/
├── data/
│   └── retail_sales.csv
├── notebooks/
│   └── 01_retail_sales_analysis.ipynb
├── reports/
│   ├── Task2_Hands_On_Data_Lab_Report.docx
│   └── Task2_Portal_Submission_Description.txt
├── results/
│   ├── cleaned_retail_sales.csv
│   ├── category_sales_summary.csv
│   ├── region_sales_summary.csv
│   ├── monthly_sales_summary.csv
│   ├── data_quality_summary.json
│   ├── sales_by_category.png
│   ├── sales_by_region.png
│   ├── monthly_sales_trend.png
│   └── 01_retail_sales_analysis_executed.ipynb
└── src/
    ├── create_dataset.py
    ├── analyze_sales.py
    └── create_notebook.py
```

## Key Results

| Metric | Result |
|---|---:|
| Orders analyzed | 20 |
| Units sold | 39 |
| Total net sales | ₹273,500 |
| Average order value | ₹13,675 |
| Highest-sales category | Electronics |
| Highest-sales region | North |

### Sales by Category

- Electronics: ₹180,700
- Home: ₹60,300
- Clothing: ₹32,500

### Sales by Region

- North: ₹111,000
- West: ₹86,300
- South: ₹54,400
- East: ₹21,800

### Monthly Sales

- January 2026: ₹82,100
- February 2026: ₹41,100
- March 2026: ₹150,300

These results are calculated from the project's synthetic dataset and are intended for demonstration.

## Data Quality and Analysis

The analysis script validates the dataset, checks for missing values and duplicates, verifies quantity, price, and discount values, and generates cleaned data and summary outputs.

The notebook contains the practical analysis workflow. The executed notebook is saved in the `results/` directory for review.

## Setup

Run the following commands from the master repository root in PowerShell:

```powershell
python -m pip install -r requirements.txt
```

## Run the Analysis

Generate the sample dataset:

```powershell
python .\Task-02-Hands-On-Data-Lab\src\create_dataset.py
```

Run the analysis:

```powershell
python .\Task-02-Hands-On-Data-Lab\src\analyze_sales.py
```

Generated datasets, summaries, and charts are saved in this task's `results/` directory.

## Deliverables

- Retail sales dataset
- Jupyter analysis notebook and executed notebook
- Cleaned dataset and summary CSV files
- Data-quality JSON report
- Three sales visualizations
- Word assessment report
- Portal submission description

## Author

Sommay Dewat
