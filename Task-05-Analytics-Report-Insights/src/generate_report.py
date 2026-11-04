
from pathlib import Path
import json
import pandas as pd

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
RESULTS_DIR = PROJECT_DIR / "results"
CHART_DIR = RESULTS_DIR / "charts"
REPORT_DIR = PROJECT_DIR / "reports"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = REPORT_DIR / "Task5_Retail_Sales_Performance_Report.docx"

# Load analysis results
with open(RESULTS_DIR / "business_kpis.json", "r", encoding="utf-8") as file:
    kpis = json.load(file)

category = pd.read_csv(RESULTS_DIR / "category_performance.csv")
region = pd.read_csv(RESULTS_DIR / "regional_performance.csv")
subcategory = pd.read_csv(RESULTS_DIR / "subcategory_performance.csv")
discount = pd.read_csv(RESULTS_DIR / "discount_analysis.csv")

quality = {}
quality_path = RESULTS_DIR / "data_quality_report.json"
if quality_path.exists():
    with open(quality_path, "r", encoding="utf-8") as file:
        quality = json.load(file)

doc = Document()

# Document styling
section = doc.sections[0]
section.top_margin = Inches(0.7)
section.bottom_margin = Inches(0.7)
section.left_margin = Inches(0.8)
section.right_margin = Inches(0.8)

styles = doc.styles
styles["Normal"].font.name = "Calibri"
styles["Normal"].font.size = Pt(10)
styles["Normal"].font.color.rgb = RGBColor(55, 65, 81)

for style_name in ["Heading 1", "Heading 2"]:
    styles[style_name].font.name = "Calibri"
    styles[style_name].font.color.rgb = RGBColor(31, 78, 121)

styles["Heading 1"].font.size = Pt(17)
styles["Heading 2"].font.size = Pt(13)

def add_paragraph(text):
    doc.add_paragraph(text)

def add_bullet(text):
    doc.add_paragraph(text, style="List Bullet")

def add_table(headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Light Shading Accent 1"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = str(header)
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

    for row in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = str(value)
            cells[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

    doc.add_paragraph()
    return table

def add_chart(filename, caption):
    path = CHART_DIR / filename
    if path.exists():
        doc.add_picture(str(path), width=Inches(6.1))
        paragraph = doc.add_paragraph(caption)
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in paragraph.runs:
            run.italic = True
            run.font.size = Pt(9)
    else:
        add_paragraph(f"Chart unavailable: {filename}")

def money(value):
    return f"${value:,.2f}"

# COVER PAGE
title = doc.add_heading("RETAIL SALES PERFORMANCE", 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

subtitle = doc.add_paragraph("Business Analytics Report & Insights Documentation")
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph()
p = doc.add_paragraph("Sample Superstore Dataset")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

p = doc.add_paragraph("Prepared as part of the Data Analyst Internship")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph()
p = doc.add_paragraph("Focus: Sales | Profitability | Regional Performance | Business Recommendations")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_page_break()

# 1. EXECUTIVE SUMMARY
doc.add_heading("1. Executive Summary", level=1)

add_paragraph(
    "This report presents an analysis of retail sales performance using the "
    "Sample Superstore dataset. The objective is to understand sales trends, "
    "profitability, category performance, regional results, customer segments, "
    "and discount patterns to identify potential business improvement areas."
)

add_paragraph(
    f"The dataset records {kpis['total_orders']:,} distinct orders from "
    f"{kpis['total_customers']:,} customers. Total sales were "
    f"{money(kpis['total_sales'])}, generating a total profit of "
    f"{money(kpis['total_profit'])}. The overall profit margin was "
    f"{kpis['profit_margin_percent']:.2f}%."
)

add_paragraph(
    "Technology was the leading category by total profit, while Furniture "
    "recorded a comparatively low profit margin. The West region generated "
    "the highest sales and profit among the four regions. Several high-discount "
    "bands recorded negative aggregate profit, indicating an area that merits "
    "further investigation."
)

# 2. BUSINESS OBJECTIVES
doc.add_heading("2. Business Objectives", level=1)

add_paragraph(
    "The analysis was designed to support business decision-making through "
    "the following objectives:"
)

for item in [
    "Measure overall sales, profit, order volume, and customer activity.",
    "Evaluate sales and profitability across product categories and sub-categories.",
    "Compare performance across geographic regions.",
    "Examine monthly sales patterns and customer segment performance.",
    "Explore the relationship between discount levels and profitability.",
    "Develop practical recommendations based on the observed results."
]:
    add_bullet(item)

# 3. DATASET OVERVIEW
doc.add_heading("3. Dataset Overview", level=1)

add_paragraph(
    "The analysis uses the Sample Superstore retail dataset. It contains "
    "transaction-level information about orders, customers, products, "
    "geographic regions, sales, quantity, discount, and profit."
)

add_table(
    ["Dataset Attribute", "Value"],
    [
        ["Original records", f"{quality.get('original_rows', 9994):,}"],
        ["Original columns", str(quality.get("original_columns", 21))],
        ["Cleaned columns", str(quality.get("cleaned_columns", 25))],
        ["Distinct orders", f"{kpis['total_orders']:,}"],
        ["Distinct customers", f"{kpis['total_customers']:,}"],
        ["Total quantity sold", f"{kpis['total_quantity_sold']:,}"],
    ]
)

# 4. DATA CLEANING
doc.add_heading("4. Data Cleaning and Preparation", level=1)

add_paragraph(
    "The dataset was inspected and prepared using Python and Pandas. "
    "Column names were standardized, date fields were converted into "
    "datetime format, and numeric fields were checked for valid values."
)

for item in [
    "Checked missing values and duplicate records.",
    "Removed duplicate records and rows with missing essential fields where applicable.",
    "Validated sales, quantity, and discount values.",
    "Created order year, order month, and month name features.",
    "Calculated profit margin as an additional analytical feature.",
    "Saved the cleaned dataset for subsequent analysis."
]:
    add_bullet(item)

add_table(
    ["Data Quality Check", "Result"],
    [
        ["Original rows", str(quality.get("original_rows", "Not available"))],
        ["Cleaned rows", str(quality.get("cleaned_rows", "Not available"))],
        ["Exact duplicates before cleaning", str(quality.get("exact_duplicates_before", "Not available"))],
        ["Rows removed for missing essential fields", str(quality.get("rows_removed_for_missing_essential_fields", "Not available"))],
        ["Invalid business records removed", str(quality.get("invalid_business_records_removed", "Not available"))],
        ["Remaining missing values", str(quality.get("remaining_missing_values", "Not available"))],
        ["Remaining duplicates", str(quality.get("remaining_duplicates", "Not available"))],
    ]
)

# 5. KPIs
doc.add_heading("5. Key Performance Indicators", level=1)

add_table(
    ["KPI", "Value"],
    [
        ["Total Sales", money(kpis["total_sales"])],
        ["Total Profit", money(kpis["total_profit"])],
        ["Total Orders", f"{kpis['total_orders']:,}"],
        ["Total Customers", f"{kpis['total_customers']:,}"],
        ["Quantity Sold", f"{kpis['total_quantity_sold']:,}"],
        ["Average Order Value", money(kpis["average_order_value"])],
        ["Profit Margin", f"{kpis['profit_margin_percent']:.2f}%"],
        ["Average Discount", f"{kpis['average_discount_percent']:.2f}%"],
    ]
)

add_paragraph(
    "Average order value is calculated as total sales divided by distinct "
    "order IDs. Average discount is the arithmetic mean of transaction-level "
    "discount values and is not weighted by sales."
)

# 6. CATEGORY ANALYSIS
doc.add_heading("6. Product Category Performance", level=1)

category_rows = []
for _, row in category.iterrows():
    category_rows.append([
        row["category"],
        money(row["sales"]),
        money(row["profit"]),
        f"{row['profit_margin_percent']:.2f}%"
    ])

add_table(
    ["Category", "Sales", "Profit", "Profit Margin"],
    category_rows
)

add_chart(
    "02_category_sales_profit.png",
    "Figure 1. Sales and profit comparison across product categories."
)

add_paragraph(
    "Technology generated the highest total profit, followed by Office Supplies. "
    "Furniture generated substantial sales but had a much lower profit margin "
    "of 2.49%. This suggests that Furniture profitability deserves closer review."
)

# 7. REGIONAL ANALYSIS
doc.add_heading("7. Regional Performance", level=1)

region_rows = []
for _, row in region.iterrows():
    region_rows.append([
        row["region"],
        money(row["sales"]),
        money(row["profit"]),
        f"{row['profit_margin_percent']:.2f}%"
    ])

add_table(
    ["Region", "Sales", "Profit", "Profit Margin"],
    region_rows
)

add_chart(
    "03_regional_sales.png",
    "Figure 2. Total sales across the four geographic regions."
)

add_paragraph(
    "The West region recorded the highest sales and total profit, with a "
    "profit margin of 14.94%. The Central region had the lowest profit margin "
    "at 7.92%. Regional differences may reflect variations in product mix, "
    "discounting, customer demand, and operating conditions."
)

# 8. MONTHLY SALES TREND
doc.add_heading("8. Monthly Sales Trend", level=1)

add_chart(
    "01_monthly_sales_trend.png",
    "Figure 3. Monthly sales trend over the available dataset period."
)

add_paragraph(
    "The monthly sales visualization helps identify changes in sales volume "
    "over time and potential seasonal patterns. Monthly performance should be "
    "reviewed alongside profit to distinguish revenue growth from profitable growth."
)

# 9. SUB-CATEGORY ANALYSIS
doc.add_heading("9. Sub-Category Profitability", level=1)

add_chart(
    "04_subcategory_profit.png",
    "Figure 4. Profit and loss performance across product sub-categories."
)

bottom = subcategory.sort_values("profit").head(5)

add_table(
    ["Sub-Category", "Sales", "Profit"],
    [
        [row["sub_category"], money(row["sales"]), money(row["profit"])]
        for _, row in bottom.iterrows()
    ]
)

add_paragraph(
    "Tables recorded the largest loss among the listed sub-categories, "
    "at $17,725.48. Bookcases and Supplies also recorded negative profit. "
    "These products should be investigated for pricing, discounting, product "
    "cost, and fulfillment-related issues."
)

# 10. DISCOUNT ANALYSIS
doc.add_heading("10. Discount and Profitability Analysis", level=1)

add_chart(
    "05_discount_profit_analysis.png",
    "Figure 5. Total profit across discount bands."
)

discount_rows = []
for _, row in discount.iterrows():
    band = str(row["discount_band"])
    discount_rows.append([
        band,
        f"{int(row['records']):,}",
        money(row["average_sales"]),
        money(row["average_profit"]),
        money(row["total_profit"])
    ])

add_table(
    ["Discount Band", "Records", "Avg. Sales", "Avg. Profit", "Total Profit"],
    discount_rows
)

add_paragraph(
    "The no-discount and 1–20% discount groups generated positive aggregate "
    "profit. The higher discount bands recorded negative total profit. "
    "This is an observed association in the dataset and does not, by itself, "
    "establish that discounting caused the losses."
)

# 11. CUSTOMER SEGMENT ANALYSIS
doc.add_heading("11. Customer Segment Performance", level=1)

add_chart(
    "06_customer_segment_performance.png",
    "Figure 6. Sales and profit by customer segment."
)

add_paragraph(
    "The customer segment visualization compares sales and profit across "
    "the available customer groups. Segment-level results can help guide "
    "marketing priorities and customer retention strategies."
)

# 12. KEY INSIGHTS
doc.add_heading("12. Key Business Insights", level=1)

insights = [
    "Overall sales reached $2.30 million, with total profit of approximately $286,397.",
    "Technology generated the highest category profit at $145,454.95.",
    "Furniture had a low profit margin of 2.49% despite generating approximately $742,000 in sales.",
    "The West region led in both sales and total profit.",
    "The Central region recorded the lowest regional profit margin at 7.92%.",
    "Tables recorded a loss of $17,725.48, making it the weakest sub-category by profit.",
    "Discount bands above 20% recorded negative total profit in this dataset."
]

for item in insights:
    add_bullet(item)

# 13. RECOMMENDATIONS
doc.add_heading("13. Actionable Business Recommendations", level=1)

recommendations = [
    (
        "Review Furniture pricing and costs",
        "Investigate the low Furniture margin by reviewing supplier costs, "
        "pricing, shipping expenses, and discount practices."
    ),
    (
        "Investigate loss-making sub-categories",
        "Review Tables, Bookcases, and Supplies at product level to identify "
        "items with consistently negative margins."
    ),
    (
        "Introduce discount guardrails",
        "Evaluate approval thresholds for high discounts and assess whether "
        "promotional offers generate enough incremental profit."
    ),
    (
        "Study Central region performance",
        "Compare the Central region's product mix, discount levels, and order "
        "economics with stronger-performing regions."
    ),
    (
        "Learn from the West region",
        "Investigate the West region's product and customer mix to identify "
        "practices that may be applicable elsewhere."
    ),
    (
        "Monitor profitable growth",
        "Track sales and profit together through a recurring KPI dashboard "
        "rather than evaluating revenue alone."
    )
]

for heading, description in recommendations:
    doc.add_heading(heading, level=2)
    add_paragraph(description)

# 14. LIMITATIONS
doc.add_heading("14. Analysis Limitations", level=1)

for item in [
    "The findings describe the available Sample Superstore dataset and should not automatically be generalized to all retail businesses.",
    "The analysis is primarily descriptive and does not establish causal relationships.",
    "The dataset may not contain all operating costs needed for a complete assessment of business profitability.",
    "Further analysis would be required to test the statistical significance of observed patterns and evaluate future performance."
]:
    add_bullet(item)

# 15. CONCLUSION
doc.add_heading("15. Conclusion", level=1)

add_paragraph(
    "The analysis provides an overview of retail sales and profitability "
    "across products, regions, customer segments, and discount levels. "
    "The business generated substantial sales and positive overall profit, "
    "but performance varied across categories and regions."
)

add_paragraph(
    "The findings highlight opportunities to review low-margin Furniture "
    "products, investigate loss-making sub-categories, evaluate high-discount "
    "transactions, and study practices in stronger-performing regions. "
    "Regular monitoring of sales, profit, and margin KPIs can help support "
    "more informed business decisions."
)

# FOOTER
for sec in doc.sections:
    footer = sec.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run("Retail Sales Performance & Business Insights | Data Analyst Internship")

doc.save(OUTPUT_FILE)

print("\n========================================")
print("FINAL REPORT GENERATED SUCCESSFULLY")
print("========================================")
print(f"Report: {OUTPUT_FILE}")
print(f"Charts included: 6")
print(f"File exists: {OUTPUT_FILE.exists()}")
