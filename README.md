# YuvaIntern Data Analyst Internship

A portfolio of practical data science and data analytics tasks completed as part of the YuvaIntern internship. The repository demonstrates Python programming, statistical analysis, data cleaning, exploratory data analysis (EDA), visualization, and technical reporting.

## Project Structure

```text
YuvaIntern-Data-Analyst-Internship/
├── Task-01-Data-Science-Fundamentals/
│   ├── notebooks/
│   ├── results/
│   ├── reports/
│   ├── README.md
│   └── requirements.txt
├── Task-02-Hands-On-Data-Lab/
│   ├── data/
│   ├── notebooks/
│   ├── results/
│   ├── reports/
│   └── src/
├── .gitignore
├── README.md
└── requirements.txt
```

## Task 01 - Data Science Fundamentals Assessment

Key activities:
- Python fundamentals and statistical calculations
- NumPy, SciPy, and Pandas exercises
- DataFrame analysis and visualization
- Data cleaning and validation
- Cleaned customer dataset and data-quality summary
- Jupyter Notebook and Word assessment report

## Task 02 - Hands-On Data Lab Implementation

Key activities:
- Python and Jupyter Notebook environment setup
- Retail sales data preparation and validation
- Exploratory data analysis using Pandas and NumPy
- Sales analysis by product category, region, and month
- Data visualization using Matplotlib
- CSV summaries, data-quality report, and Word report

### Task 02 - Sample Results

The project uses a **synthetic retail sales dataset** containing 20 sample orders. These figures are for demonstration and are not actual business results.

| Metric | Result |
|---|---:|
| Orders analyzed | 20 |
| Units sold | 39 |
| Total net sales | ₹273,500 |
| Average order value | ₹13,675 |
| Highest-sales category | Electronics |
| Highest-sales region | North |

Generated outputs include:
- Cleaned retail sales dataset
- Category, regional, and monthly sales summaries
- Data-quality summary in JSON format
- Sales-by-category chart
- Sales-by-region chart
- Monthly sales trend chart
- Executed Jupyter Notebook
- Word report and portal submission description

## Technology Stack

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- SciPy
- Jupyter Notebook
- Python-docx
- CSV and JSON data formats

## Environment Setup

Run these commands from the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Running Task 02

Generate the sample dataset:

```powershell
python .\Task-02-Hands-On-Data-Lab\src\create_dataset.py
```

Run the sales analysis:

```powershell
python .\Task-02-Hands-On-Data-Lab\src\analyze_sales.py
```

Review the notebook in the `Task-02-Hands-On-Data-Lab/notebooks/` directory and the generated outputs in its `results/` directory.

## Repository Notes

- The Task 02 retail dataset is synthetic and intended for learning and demonstration.
- The `.venv/` directory and local environment files are excluded through `.gitignore`.
- Reports, notebooks, charts, and analysis outputs are organized within their respective task folders.

## Author

Sommay Dewat
