# Fraud Analysis Report

An exploratory data analysis of **6.3 million financial transactions**, identifying fraud patterns, behavioural signatures, and critical failures in the existing detection system — presented as an interactive, chart-driven report.


 **[View Live Report →](https://p3rmary.github.io/Fraud-Analysis/)**

---

## Overview

This project investigates a large-scale financial transaction dataset to surface how, when, and through which channels fraud occurs. The analysis goes beyond surface-level fraud rates to examine the behavioural mechanics of fraudulent actors — including deliberate exploitation of system transaction caps, overnight automation, and a two-step transfer-then-cashout laundering pattern.

A key finding: the existing automated flagging system has a **true positive rate of just 0.19%**, catching only 16 of 8,213 confirmed fraud cases. This analysis provides the behavioural foundation needed to build a materially better detection model.

---

## Key Findings

| Metric | Value |
|---|---|
| Total transactions analysed | 6,362,620 |
| Confirmed fraud transactions | 8,213 |
| Fraud rate (by count) | 0.13% |
| Total fraud volume | $12.06 billion |
| Fraud rate (by volume) | 1.05% |
| Average fraud amount | $1,467,967 |
| System true positive rate | **0.19%** |

- **Fraud is type-specific** — 100% of fraud occurs in `TRANSFER` and `CASH_OUT` transactions. CASH_IN, DEBIT, and PAYMENT recorded zero fraud.
- **Overnight hours are the highest-risk window** — The 03:00–05:00 period carries fraud rates exceeding 22%, a hallmark of automated, script-driven fraud.
- **The $10M cap is being weaponised** — A significant cluster of transactions hit the maximum single-transaction limit exactly, indicating deliberate exploitation of the system ceiling.
- **The detection system is effectively non-functional** — 8,197 of 8,213 fraudulent transactions went unflagged.

---

## Report Sections

1. **Setup & Data Loading**  Dataset overview and source files
2. **Key Metrics Summary** — KPI dashboard: fraud rate, volume, average amount
3. **Fraud by Transaction Type** — Dual-axis bar chart: volume and fraud rate by type
4. **Hourly Transaction Patterns** — 24-hour fraud rate vs. total transaction volume
5. **Daily Fraud Trends Over Time** — Time-series of fraud volume and count
6. **Fraud Amount Distribution** — Histogram revealing bimodal fraud amount clustering
7. **Balance Analysis: Before vs After Fraud** — Scatter plot of full-drain and cap-hit behaviour
8. **Top 20 Highest-Value Fraud Accounts** — Ranked account pairs by total fraud extracted
9. **Flagged vs Actual Fraud** — System accuracy: true positive vs false negative breakdown
10. **Fraud Heatmap: Hour × Transaction Type** — Cross-dimensional fraud count matrix
11. **Summary & Key Findings** — Consolidated takeaways and recommendations

---

## Data Sources

| File | Description | Rows |
|---|---|---|
| `fraud_data.csv` | Individual fraud transactions | 8,213 |
| `fraud_totals.csv` | Aggregated fraud totals by account pair | 8,213 |
| `hourly.csv` | Hourly transaction volume across 24 hours | 24 |
| `totals.csv` | Daily totals broken down by transaction type | 152 |

---

## Tech Stack

- **Python** — Data processing and analysis
- **Pandas** — Data manipulation and aggregation
- **Plotly** — Interactive charts and visualisations
- **Jupyter Notebook** — Analysis environment
- **GitHub Pages** — Report deployment

---

## Setup & Running Locally

```bash
# Clone the repository
git clone https://github.com/your-username/fraud-analysis.git
cd fraud-analysis

# Install dependencies
pip install pandas plotly jupyter

# Launch the notebook
jupyter notebook fraud_analysis.ipynb
```

To export the report as a standalone HTML file:

```bash
jupyter nbconvert --to html fraud_analysis.ipynb --output index.html
```

---

## Project Structure

```
fraud-analysis/
├── fraud_analysis.ipynb   # Main analysis notebook
├── index.html             # Exported interactive report (GitHub Pages)
├── data/
│   ├── fraud_data.csv
│   ├── fraud_totals.csv
│   ├── hourly.csv
│   └── totals.csv
└── README.md
```

---

## Insights at a Glance

**What does 0.13% fraud rate actually mean $12 billion in losses?**
Because fraud is not spread evenly, it is concentrated in a small number of extremely high-value transactions. The average fraudulent transaction is nearly $1.5 million, over 100× the average legitimate transaction size. Count-based fraud rates are misleading; volume-based rates tell the real story.

**Why is 03:00–05:00 so dangerous?**
Legitimate transaction volume is lowest overnight, meaning even a flat absolute count of fraud transactions produces an extreme fraud rate. Fraudsters appear to time their activity deliberately to exploit reduced monitoring windows.

**What does the detection failure mean in practice?**
A 0.19% true positive rate means for every 1 fraud case caught, 512 others go undetected. The patterns identified in this analysis, overnight timing, maximum-value amounts, and `TRANSFER → CASH_OUT` sequences — provide a concrete signal set for building a rule-based or ML-driven detection layer that would dramatically outperform the current system.
