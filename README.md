# Hotel Procurement Spend Intelligence & Strategic Sourcing Engine

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Enterprise Data Analyst](https://img.shields.io/badge/code%20style-production--ready-brightgreen.svg)]()

An enterprise-grade procurement data analytics engine designed to analyze, standardize, classify, and audit **2019 purchase transaction data across 4 hotel properties** (*123 Company*, *ABC Company*, *LMN Company*, and *XYZ Company*).

This project performs full-spectrum ETL, regex-driven product classification with false-positive filtering, brand standardization, multi-tab Excel reporting, interactive HTML dashboard creation, and enterprise cloud scaling architecture.

---

## 📊 Executive Key Performance Indicators (2019)

| Metric | Audited Value | Benchmark Notes |
| :--- | :--- | :--- |
| **Total Consolidated Procurement Spend** | **INR 133.97 Crores** | `INR 133,96,64,278.72` across 248,835 total orders |
| **PepsiCo Category Spend** | **INR 39.55 Lakhs** | `INR 39,55,136.14` across 612 orders |
| **Kimberly-Clark Category Spend** | **INR 52.39 Lakhs** | `INR 52,39,288.25` across 308 orders |
| **Combined Target Brand Share** | **0.69%** | Represents 0.69% of total hotel group spend |

---

## 🔍 Key Audited Procurement Discoveries

### 1. Single-Distributor Reliance per Property (Zero Supplier Competition)
Each hotel property relies on **a single dedicated distributor** for >99% of its PepsiCo beverage purchases with zero vendor splitting across properties:
- **123 Company**: *SRI KALYANI FOODS* (INR 13.94 Lakhs \| **35.2%** of Pepsi spend \| 196 orders)
- **LMN Company**: *SMS Commercial* (INR 12.03 Lakhs \| **30.4%** of Pepsi spend \| 117 orders)
- **XYZ Company**: *Super Enterprises* (INR 11.38 Lakhs \| **28.8%** of Pepsi spend \| 279 orders)
- **ABC Company**: *Premier Catering & Marketing* (INR 2.21 Lakhs \| **5.6%** of Pepsi spend \| 20 orders)

### 2. Kimberly-Clark Spend Concentration at XYZ Company
XYZ Company accounts for **68.2% of total Kimberly-Clark spend** across the hotel group (INR 35.75 Lakhs of INR 52.39 Lakhs total across 128 orders) — more than double LMN Company (**23.7%**, INR 12.42 Lakhs).

### 3. Operational Direct-from-Manufacturer Sourcing Model
`Kimberly Clark Hygiene Pvt Ltd` (the manufacturer itself) is already the single largest supplier of KC hygiene products in the dataset, accounting for **INR 21.02 Lakhs** (**40.1%** of total KC spend across 144 orders). Direct manufacturer contracting is already proven operational.

---

## 📁 Repository Architecture

```text
Marriott-Procurement-Spend-Intelligence/
├── data/
│   ├── raw/                                    # Raw vendor purchase sheets & product lists
│   │   ├── 123 Company.xlsx
│   │   ├── ABC Company.xlsx
│   │   ├── LMN Company.xlsx
│   │   ├── XYZ Company.xlsx
│   │   ├── Pepsi Product List.xlsx
│   │   └── KC Product List.pdf
│   └── processed/                              # Processed output datasets / staging
├── docs/                                       # Business documentation & methodology
│   ├── Methodology.md                          # Data dictionary, regex logic, audited findings
│   └── Submission.docx                         # Formal executive report
├── reports/                                    # Executive deliverables & visual assets
│   ├── dashboard.html                          # Standalone single-page interactive HTML dashboard
│   ├── Hotel Procurement and Spend Analysis 2019.pbix # Power BI report file
│   └── figures/                                # 12 publication-quality charts (PNG)
│       ├── 01_pepsi_spend_by_hotel.png
│       ├── 02_kc_spend_by_hotel.png
│       └── ...
├── src/                                        # Modular production analytics engine
│   ├── __init__.py                             # Package initializer
│   ├── config.py                               # Paths, schemas, regex rules, theme constants
│   ├── data_loader.py                          # Multi-hotel ETL & schema unification
│   ├── classifier.py                           # Regex categorization & false-positive filters
│   ├── analyzer.py                             # Aggregations, cross-tabs, price variance metrics
│   ├── visualizer.py                           # Matplotlib/Seaborn chart generation engine
│   ├── excel_exporter.py                       # openpyxl executive workbook generator
│   ├── html_reporter.py                        # Dynamic HTML dashboard builder
│   └── utils.py                                # Logging & numeric claim verification harness
├── main.py                                     # Command Line Interface (CLI) runner
├── requirements.txt                            # Production dependency specifications
├── pyproject.toml                              # Modern Python packaging configuration
├── .gitignore                                  # Comprehensive Git ignore pattern rules
└── README.md                                   # Executive portfolio README
```

---

## 🛠️ Technology Stack

- **Core Analytics Engine**: Python 3.9+, Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn
- **Excel Engineering**: openpyxl
- **Interactive Reporting**: HTML5 / CSS3 (Inter Typography, Glassmorphism Cards)
- **Business Intelligence**: Power BI (`.pbix`)

---

## 🚀 Quickstart Guide

### 1. Environment Setup
Clone the repository and install dependencies:
```bash
git clone https://github.com/adarshkore/Marriott-Procurement-Spend-Intelligence.git
cd Marriott-Procurement-Spend-Intelligence

python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Execution
Run the full automated end-to-end data pipeline:
```bash
python main.py
```

### 3. Pipeline Output Artifacts
Executing `python main.py` automatically generates:
- **`reports/Spend_Analysis_Output.xlsx`**: Styled executive Excel workbook with 18 formatted tabs.
- **`reports/dashboard.html`**: Single-page executive HTML dashboard.
- **`reports/figures/`**: 12 high-resolution publication charts.
- **`docs/Methodology.md`**: Complete methodology and data dictionary document.

---

## 🏗️ Enterprise Scaling Blueprint (400+ Hotel Network)

To scale spend intelligence across a nationwide enterprise network of **400+ hotel properties**, keyword-based Python scripts are migrated into a modern **Cloud Data Lakehouse Architecture**:

```
[400+ Hotel ERP / POS Systems] 
       │
       ▼ (Automated Daily Ingestion via Azure Data Factory / AWS Glue)
[Master Data Management (MDM) / Master SKU Dictionary]
       │ (Levenshtein Fuzzy Matching & ML Text Classification)
       ▼
[Cloud Data Warehouse: Snowflake / Databricks / BigQuery]
       │
       ▼
[Power BI / Tableau Live Executive Dashboards]
```

### Strategic Pillars:
1. **Canonical Master SKU Catalog**: Automated fuzzy matching maps fragmented raw invoice strings to canonical Global SKU IDs.
2. **Automated Contract & Compliance Gates**: Real-time validation alerts procurement managers to unauthorized vendor splittings or unapproved distributors.
3. **Group Volume Bundling**: Consolidating purchase volume directly with primary manufacturers (e.g., PepsiCo India, Kimberly-Clark Hygiene) unlocks estimated **12-18% annual procurement cost savings**.

---

## 📄 Author & License

- **Author**: Adarsh Kore
- **License**: MIT License
