# Data Science Fundamentals Assessment

**Internship Task 1 | Data Analyst**

## Overview
This project demonstrates core data science foundations through reproducible Python exercises: basic Python syntax and data structures, descriptive statistics with NumPy/SciPy, data exploration and grouping with Pandas, a simple Matplotlib visualization, and data-quality checks.

> **Data note:** The datasets in this repository are synthetic learning examples. They do not contain real customer information.

## Learning objectives
- Work with Python variables, built-in functions, lists, dictionaries, and conditional logic.
- Calculate mean, median, mode, range, variance, and standard deviation.
- Inspect tabular data using Pandas and summarize groups.
- Create a clear chart with Matplotlib.
- Detect missing values, exact duplicate rows, and invalid values.
- Apply documented cleaning choices and validation assertions.
- Save outputs so results can be reviewed and reproduced.

## Repository structure
```text
Data-Science-Fundamentals/
├── notebooks/
│   └── 01_data_science_fundamentals.ipynb
├── reports/
│   └── Data_Science_Fundamentals_Assessment_Report.docx
├── results/
│   ├── cleaned_customer_data.csv
│   └── data_quality_summary.json
├── src/
├── README.md
└── requirements.txt
```

## Run the notebook
Recommended: Python 3.10 or 3.11.

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter notebook
```

Open `notebooks/01_data_science_fundamentals.ipynb` and run the cells from top to bottom.

## Methods
1. **Python fundamentals:** variables, collections, calculations, and conditional statements.
2. **Statistics:** descriptive measures calculated on a small sample.
3. **Pandas:** DataFrame construction, shape and data-type inspection, descriptive statistics, and group means.
4. **Visualization:** a labelled bar chart comparing sample student marks.
5. **Data quality:** detect missing values and duplicate rows, treat an invalid age, impute selected missing values using medians, and validate key constraints.

## Data-cleaning decisions
The teaching dataset contains a duplicated record, missing values, and an implausible age. Exact duplicate rows are removed; ages outside 0–100 are marked missing; remaining missing age and purchase amounts are filled using their column medians. These choices are for demonstration only. In real business work, the analyst should investigate the reason for missingness, business rules, and the impact of imputation before selecting a method.

## Outputs
- `results/cleaned_customer_data.csv` — cleaned synthetic dataset.
- `results/data_quality_summary.json` — validation summary.
- `reports/Data_Science_Fundamentals_Assessment_Report.docx` — report for the internship portal.

## Limitations
The data is small and synthetic. It is suitable for demonstrating workflow and basic methods, not for drawing conclusions about real customers or making business decisions.

## Author
Sommay Dewat

## License
Educational portfolio project. Add a license if you want to define reuse terms.
