# Data Science Tool Mastery Project

## Overview
A practical project demonstrating Python data science tools through
dataset inspection, cleaning, statistical analysis, feature engineering,
and visualization.

## Objectives
- Inspect dataset structure and quality.
- Clean duplicate and invalid records.
- Analyze numerical data with Pandas and NumPy.
- Create visualizations with Matplotlib and Seaborn.
- Document findings in Jupyter Notebook and a Word report.

## Dataset
The project uses Seaborn's built-in `tips` dataset, a small educational
dataset containing restaurant bills, tips, party size, day, meal time,
and customer attributes.

## Technology Stack
- Python 3.11
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- python-docx

## Key Results
- Original dataset: 244 rows and 7 columns.
- Exact duplicate rows removed: 1.
- Cleaned dataset: 243 rows.
- Missing values in original data: 0.
- Mean total bill: 19.81 dataset units.
- Mean tip: 3.00 dataset units.
- Aggregate tip-to-bill ratio: 15.15%.

## Project Structure
```text
Task-04-Data-Science-Tool-Mastery/
├── data/
├── notebooks/
├── src/
├── results/
│   └── charts/
├── reports/
├── requirements.txt
└── README.md
```

## How to Run
Activate the existing root virtual environment and move to this folder.

```powershell
& "..\.venv\Scripts\Activate.ps1"
python .\src\inspect_dataset.py
python .\src\clean_and_analyze.py
python .\src\create_visualizations.py
python .\src\create_report.py
```

Open the Jupyter Notebook in the `notebooks` directory to explore the
analysis interactively.

## Limitations
This small educational dataset is not representative of all restaurants.
Associations do not establish causation, and unusual observations require
investigation before removal.

## Deliverables
- Python scripts
- Jupyter Notebook
- Cleaned CSV dataset
- Statistical summary and inspection report
- Five charts
- Word report
