# Retail Sales Performance & Business Insights Analysis

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical_Visualization-4c72b0)
![Status](https://img.shields.io/badge/Status-Completed-success)

## Project Overview

This project analyzes retail sales data to evaluate business performance, identify profitability trends, and generate actionable business insights.

Using the Sample Superstore dataset, the analysis explores sales performance, product categories, regional contribution, customer segments, monthly trends, and the relationship between discount levels and profitability.

The objective is to transform raw transactional data into meaningful business insights that can support data-driven decision-making.

## Business Objectives

- Evaluate overall sales, profit, order volume, and customer activity.
- Analyze product category and sub-category performance.
- Compare sales and profitability across geographic regions.
- Identify monthly sales trends and patterns.
- Examine discount levels and their association with profitability.
- Develop actionable recommendations for business improvement.

## Dataset Overview

| Attribute | Details |
|---|---|
| Dataset | Sample Superstore |
| Total Records | 9,994 |
| Original Columns | 21 |
| Engineered Columns | 4 |
| Total Customers | 793 |
| Distinct Orders | 5,009 |
| Data Format | CSV |

The dataset contains order details, customer information, product categories, geographic locations, sales, quantity, discounts, and profit.

## Technology Stack

- **Programming:** Python 3.11
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Reporting:** Microsoft Word, python-docx
- **Development Environment:** VS Code, PowerShell, Jupyter Notebook
- **Version Control:** Git and GitHub

## Project Workflow

1. **Data Inspection:** Examined dataset structure, dimensions, data types, missing values, and duplicates.
2. **Data Cleaning:** Standardized column names, converted date and numeric fields, validated business records, and checked data quality.
3. **Feature Engineering:** Created order year, order month, month name, and profit margin features.
4. **Business KPI Analysis:** Calculated sales, profit, orders, customers, average order value, and profit margin.
5. **Exploratory Analysis:** Investigated category, regional, sub-category, monthly, customer segment, and discount performance.
6. **Data Visualization:** Created six charts to communicate business trends and findings.
7. **Business Reporting:** Prepared an executive-style report with insights and actionable recommendations.

## Key Business KPIs

| KPI | Result |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Total Orders | 5,009 |
| Total Customers | 793 |
| Quantity Sold | 37,873 |
| Average Order Value | $458.61 |
| Overall Profit Margin | 12.47% |
| Average Discount | 15.62% |

## Business Insights

### 1. Product Category Performance
- Technology generated the highest total profit of $145,454.95.
- Technology achieved a 17.40% profit margin.
- Furniture generated substantial sales but had a comparatively low profit margin of 2.49%.

### 2. Regional Performance
- West was the highest-performing region by sales, generating $725,457.82.
- West also generated the highest regional profit of $108,418.45.
- Central had the lowest regional profit margin at 7.92%.

### 3. Sub-Category Profitability
- Tables recorded the largest loss of $17,725.48.
- Bookcases and Supplies also recorded negative profits.
- These sub-categories require further investigation into pricing, costs, and discount practices.

### 4. Discount Analysis
- No Discount and 1–20% discount groups recorded positive aggregate profit.
- Discount bands above 20% recorded negative aggregate profit.
- The observed relationship highlights the need to review discount policies and their impact on profitability.

**Note:** These are descriptive findings from the available dataset. They do not independently establish causal relationships.

## Data Visualizations

The project includes six visualizations:

| Visualization | File |
|---|---|
| Monthly Sales Trend | `01_monthly_sales_trend.png` |
| Category Sales & Profit | `02_category_sales_profit.png` |
| Regional Sales Performance | `03_regional_sales.png` |
| Sub-Category Profitability | `04_subcategory_profit.png` |
| Discount Profit Analysis | `05_discount_profit_analysis.png` |
| Customer Segment Performance | `06_customer_segment_performance.png` |

All charts are available in `results/charts/`.

## Business Recommendations

1. **Improve Furniture Profitability:** Review product pricing, supplier costs, and discount structures.
2. **Investigate Loss-Making Products:** Examine Tables, Bookcases, and Supplies to identify profitability issues.
3. **Optimize Discount Policies:** Introduce appropriate discount controls and evaluate promotional profitability.
4. **Improve Regional Performance:** Investigate the Central region's lower profit margin.
5. **Monitor Business KPIs:** Regularly track sales, profit, average order value, and profit margin.
6. **Encourage Profitable Growth:** Evaluate revenue growth alongside profitability rather than focusing only on sales.

## Project Structure

```text
Task-05-Analytics-Report-Insights/
│
├── data/
│   ├── Sample - Superstore.csv
│   └── superstore_cleaned.csv
│
├── notebooks/
│
├── src/
│   ├── inspect_dataset.py
│   ├── clean_dataset.py
│   ├── business_analysis.py
│   ├── create_visualizations.py
│   └── generate_report.py
│
├── results/
│   ├── charts/
│   │   ├── 01_monthly_sales_trend.png
│   │   ├── 02_category_sales_profit.png
│   │   ├── 03_regional_sales.png
│   │   ├── 04_subcategory_profit.png
│   │   ├── 05_discount_profit_analysis.png
│   │   └── 06_customer_segment_performance.png
│   │
│   ├── business_kpis.json
│   ├── data_quality_report.json
│   ├── category_performance.csv
│   ├── regional_performance.csv
│   ├── monthly_performance.csv
│   ├── subcategory_performance.csv
│   └── discount_analysis.csv
│
├── reports/
│   ├── Business_Objectives.md
│   └── Task5_Retail_Sales_Performance_Report.docx
│
└── README.md
```

## How to Run the Project

Clone the repository:

```bash
git clone https://github.com/SommayDewat/YuvaIntern-Data-Analyst-Internship.git
```

Navigate to the Task 5 folder:

```bash
cd YuvaIntern-Data-Analyst-Internship/Task-05-Analytics-Report-Insights
```

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn python-docx
```

Run the analysis pipeline:

```bash
python src/inspect_dataset.py
python src/clean_dataset.py
python src/business_analysis.py
python src/create_visualizations.py
python src/generate_report.py
```

## Final Deliverable

**Retail Sales Performance & Business Insights Report**

`reports/Task5_Retail_Sales_Performance_Report.docx`

The report includes:
- Executive Summary
- Business Objectives
- Dataset Overview
- Data Cleaning and Preparation
- KPI Analysis
- Sales and Profitability Analysis
- Regional and Category Performance
- Data Visualizations
- Key Business Insights
- Actionable Business Recommendations
- Conclusion and Limitations

## Conclusion

This project demonstrates an end-to-end data analysis workflow, from raw dataset inspection and cleaning to business KPI development, exploratory analysis, visualization, and professional reporting.

It highlights how Python-based analytics can help identify profitability challenges, understand business performance, and support informed decision-making.

---

**Project Category:** Data Analytics | Business Intelligence | Exploratory Data Analysis

**Internship:** YuvaIntern – Data Analyst Internship

**GitHub:** [SommayDewat](https://github.com/SommayDewat)
