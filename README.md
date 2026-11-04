# YuvaIntern – Data Analyst Internship

<p align="center">
  <img src="https://img.shields.io/badge/Internship-Data%20Analytics-blue?style=for-the-badge" alt="Data Analytics Internship">
  <img src="https://img.shields.io/badge/Program-8%20Weeks-informational?style=for-the-badge" alt="8 week program">
  <img src="https://img.shields.io/badge/Tools-Python%20%7C%20Pandas%20%7C%20SQL%20%7C%20Visualization-success?style=for-the-badge" alt="Tools">
</p>

<p align="center">
  A structured portfolio of data analytics tasks completed as part of the YuvaIntern Data Analyst Internship.
</p>

---

## About the Internship

This repository documents practical work completed during an **8-week Data Analyst Internship** running from **4 October 2026 to 29 November 2026**. The program focuses on applying analytical methods to business datasets, translating findings into useful insights, and communicating recommendations through clear reports and visualizations.

The repository is organized task by task. Each task folder contains its relevant analysis files, documentation, scripts, datasets (where appropriate), visual outputs, and report deliverables.

> **Progress note (4 November 2026):** The internship portal showed 4 of 6 tasks evaluated. Tasks 1, 2, and 4 had passed evaluation; Task 3 required revision and resubmission. Task 5 analysis and its redesigned Word report have been prepared for submission. Task 6 is pending.

## Internship Objectives

- Understand business problems and translate them into analytical questions.
- Inspect, clean, validate, and prepare datasets for analysis.
- Perform exploratory data analysis (EDA) and identify meaningful patterns.
- Apply segmentation and analytical techniques to understand business performance.
- Build clear visualizations that communicate findings to stakeholders.
- Prepare professional reports, executive summaries, and actionable recommendations.
- Explain analytical assumptions, limitations, and business implications.

## Repository Structure

```text
YuvaIntern-Data-Analyst-Internship/
│
├── Task-01-.../
│   └── Task 1 files and documentation
│
├── Task-02-.../
│   └── Task 2 files and documentation
│
├── Task-03-.../
│   └── Task 3 analysis and revised submission materials
│
├── Task-04-.../
│   └── Task 4 files and documentation
│
├── Task-05-Analytics-Report-Insights/
│   ├── data/
│   │   ├── Sample - Superstore.csv
│   │   └── superstore_cleaned.csv
│   ├── reports/
│   │   ├── Business_Objectives.md
│   │   └── Task5_Retail_Sales_Performance_Report_Redesigned.docx
│   ├── results/
│   │   ├── charts/
│   │   ├── business_kpis.json
│   │   ├── data_quality_report.json
│   │   ├── category_performance.csv
│   │   ├── regional_performance.csv
│   │   ├── subcategory_performance.csv
│   │   ├── monthly_performance.csv
│   │   └── discount_analysis.csv
│   └── src/
│       ├── inspect_dataset.py
│       ├── clean_dataset.py
│       ├── business_analysis.py
│       ├── create_visualizations.py
│       └── generate_report.py
│
├── README.md
└── requirements.txt
```

*Folder names and individual filenames may vary slightly as the internship work evolves. The Task 5 report filename shown above should match the final file committed to this repository.*

## Task-wise Progress

| Task | Topic | Work focus | Portal status (as of 4 Nov 2026) |
|---|---|---|---|
| 01 | Dataset Understanding | Understand dataset structure, fields, business context, and initial data quality | Evaluated – 56.5/100 |
| 02 | Data Cleaning & Preparation | Identify quality issues, apply cleaning rules, and document assumptions | Evaluated – 61.1/100 |
| 03 | Exploratory Data Analysis | Explore distributions, relationships, patterns, and business-relevant findings | Revision required – 27/100; resubmission pending |
| 04 | Customer / Business Analysis | Perform analytical breakdowns and communicate findings through analysis and visuals | Evaluated – 58/100 |
| 05 | Analytics Report & Insights Documentation | Define business objectives, analyze results, visualize findings, write an executive summary, and recommend actions | Analysis and redesigned Word report prepared; portal submission pending |
| 06 | Final internship task | To be completed according to the task brief | Upcoming / brief pending |

**Important:** “Prepared” means the work files have been developed; it does not mean the internship portal has accepted or evaluated the submission.

## Task 5 – Analytics Report & Insights Documentation

### Project: Retail Sales Performance Analysis

Task 5 uses the **Sample Superstore** retail dataset to assess sales, profitability, category performance, regional performance, subcategory performance, and discount patterns. The work follows a business-reporting workflow: define the questions, inspect and prepare the data, calculate KPIs, analyze performance, visualize findings, and translate the results into practical recommendations.

### Business questions

- What are the overall sales, profit, order volume, customer count, and profit margin?
- Which product categories contribute most to sales and profit?
- Which regions perform strongly or need attention?
- Which subcategories show negative profitability?
- How do observed discount bands relate to average and total profit?
- What actions should stakeholders investigate to improve profitability?

### Dataset and preparation

| Item | Result |
|---|---:|
| Source dataset | Sample Superstore |
| Original records | 9,994 |
| Original columns | 21 |
| Records in cleaned dataset | 9,994 |
| Columns after feature engineering | 25 |
| Missing values after preparation | 0 |
| Duplicate records identified | 0 |

The analysis retained all 9,994 records. Four additional analytical features were created. Data preparation decisions and quality checks are documented in the Task 5 project files.

### Key performance indicators

| KPI | Result |
|---|---:|
| Total sales | $2,297,200.86 |
| Total profit | $286,397.02 |
| Orders | 5,009 |
| Customers | 793 |
| Quantity sold | 37,873 |
| Average order value (AOV) | $458.61 |
| Overall profit margin | 12.47% |
| Average row-level discount | 15.62% |

### Selected findings

**Category performance**

| Category | Sales | Profit | Profit margin |
|---|---:|---:|---:|
| Technology | $836,154.03 | $145,454.95 | 17.40% |
| Furniture | $741,999.80 | $18,451.27 | 2.49% |
| Office Supplies | $719,047.03 | $122,490.80 | 17.04% |

Technology generated the highest sales and profit among the three categories. Furniture generated substantial sales but a comparatively low profit margin, making it an important area for further investigation.

**Regional performance**

| Region | Sales | Profit | Profit margin |
|---|---:|---:|---:|
| Central | $501,239.89 | $39,706.36 | 7.92% |
| East | $678,781.24 | $91,522.78 | 13.48% |
| South | $391,721.91 | $46,749.43 | 11.93% |
| West | $725,457.82 | $108,418.45 | 14.94% |

The West region led in sales and profit, while the Central region had the lowest regional profit margin in this dataset.

**Subcategory profitability**

- Tables recorded a loss of **$17,725.48**.
- Bookcases recorded a loss of **$3,472.56**.
- Supplies recorded a loss of **$1,189.10**.

These results identify subcategories that warrant deeper review of pricing, discounting, product costs, and sales mix.

**Discount analysis**

The 21–40%, 41–60%, and 61–80% discount bands showed negative total profit in the analyzed data. This is a descriptive association, not proof that discounts alone caused the losses. Product mix, order characteristics, costs, and other factors may also contribute.

### Visualizations and deliverables

The Task 5 project includes visual analysis of:

- Category performance
- Regional performance
- Subcategory performance
- Discount and profitability patterns
- Monthly sales patterns
- Customer-segment performance

The project also includes KPI and data-quality outputs, supporting CSV summaries, Python scripts, business objectives documentation, and a detailed redesigned Word report. Interpretations are limited to the numerical outputs available in the analysis; charts without supporting summary tables are not assigned invented values.

### Recommendations highlighted for business review

1. Review pricing, costs, and discount policies for low-margin Furniture products.
2. Investigate loss-making subcategories, especially Tables and Bookcases, at product and order level.
3. Examine the Central region for differences in product mix, discounting, shipping, and operating costs.
4. Evaluate discount effectiveness using profit and contribution measures, not sales volume alone.
5. Monitor category, regional, subcategory, and discount KPIs over time to assess whether corrective actions improve profitability.

These are analytical recommendations for further business investigation, not claims of proven causal effects.

## Tools & Technologies

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-4C72B0?style=flat" alt="Seaborn">
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white" alt="SQL">
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black" alt="Power BI">
  <img src="https://img.shields.io/badge/Microsoft%20Excel-217346?style=flat&logo=microsoftexcel&logoColor=white" alt="Excel">
  <img src="https://img.shields.io/badge/Microsoft%20Word-2B579A?style=flat&logo=microsoftword&logoColor=white" alt="Microsoft Word">
</p>

- **Programming & analysis:** Python, Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Data & querying:** CSV, SQL / MySQL
- **Reporting:** Jupyter Notebook, Microsoft Word, Excel
- **Version control:** Git and GitHub

## How to Run the Task 5 Analysis

### 1. Clone the repository

```bash
git clone https://github.com/SommayDewat/YuvaIntern-Data-Analyst-Internship.git
cd YuvaIntern-Data-Analyst-Internship
```

### 2. Set up the Python environment

Use the internship repository's existing environment and root `requirements.txt` where available. From the repository root:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run Task 5 scripts

Run the scripts from the Task 5 folder, in the order required by the project:

```bash
cd Task-05-Analytics-Report-Insights
python src/inspect_dataset.py
python src/clean_dataset.py
python src/business_analysis.py
python src/create_visualizations.py
python src/generate_report.py
```

If a script expects a particular working directory or input path, follow the instructions in that task folder's README and script configuration.

## Data, Assumptions & Limitations

- The Task 5 analysis is based on the included Sample Superstore dataset.
- Reported KPI values describe this dataset and should not be interpreted as current market-wide retail benchmarks.
- The discount analysis identifies observed associations; it does not establish causation.
- The repository's CSV summaries and JSON outputs should be treated as the source of calculated metrics.
- Monthly and customer-segment chart interpretations should be checked against their source summaries before making specific numerical claims.
- The internship portal's evaluation status is separate from the presence of files in this GitHub repository.

## Author

**Sommay Dewat**  
BBA Graduate | Data Analytics & Business Intelligence Enthusiast

- **LinkedIn:** [linkedin.com/in/sommay-dewat](https://www.linkedin.com/in/sommay-dewat/)
- **GitHub:** [github.com/SommayDewat](https://github.com/SommayDewat)

---

<p align="center">
  Built as part of the YuvaIntern Data Analyst Internship – learning through practical analysis, business interpretation, and structured reporting.
</p>
