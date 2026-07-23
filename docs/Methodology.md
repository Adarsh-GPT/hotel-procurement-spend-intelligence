# Hotel Procurement Spend Analysis & Audited Sourcing Report

## Executive Summary
This document provides the end-to-end data engineering methodology, regex classification logic, false-positive mitigation, strictly audited data findings, and enterprise scaling architecture for the 2019 procurement spend dataset of 4 hotel properties (*123 Company*, *ABC Company*, *LMN Company*, and *XYZ Company*).

---

## 1. Data Consolidation & Schema Standardization
The raw procurement data comprised 4 distinct Excel workbooks with un-standardized column headers, varied date formats, and missing calculated fields:
- **123 Company**: 70,996 rows (`Received date`, `Extension`).
- **ABC Company**: 35,117 rows (`Bill Date`, `Total Cost`). Standardized `Store` column mapped directly to `Category` (e.g., PERISHABLE, DIRECT, FOOD, BUTCHERY, ENGINEERING, BEVERAGE, TOBACO).
- **LMN Company**: 53,396 rows (`Purchase Date`, `Total Cost`). Contained both numeric `Product` code and text `Product Description`. The numeric `Product` column was dropped prior to renaming to avoid schema conflicts.
- **XYZ Company**: 89,326 rows (`Received date`, `Rec'd ext amt`).

### Consolidated Metrics
- **Total Consolidated Transactions**: **248,835 orders**
- **Total Procurement Spend**: **INR 133,96,64,278.72** (~INR 133.97 Crores)
- **Schema**: `[Hotel, Date, Supplier, Category, Product, UOM, Qty, UnitPrice, TotalCost, IsPepsi, IsKC, Brand, Standard_SKU]`

---

## 2. Classification Logic & False-Positive Exclusions

### PepsiCo Classification
- **Regex Pattern**: `r'(?:pepsi|mirinda|7\s?up|mountain\s?dew|dukes?|lehar)'` (Case-Insensitive).
- **Results**: **612 orders** | **INR 39,55,136.14** (~INR 39.55 Lakhs).

### Kimberly-Clark (KC) Classification & False Positive Filtering
- **Regex Pattern**: `r'(?:kleenex|kimsoft|kimtech|wypall|micromist|kleen\s?guard|k\.?c\.?\s?professional|kcp|scott)'` (Case-Insensitive).
- **Results**: **308 orders** | **INR 52,39,288.25** (~INR 52.39 Lakhs).

#### Explicit False Positive Exclusions Enforced:
1. **Scott Word Exclusions**: Excluded non-hygiene items containing `scottish`, `scotti`, or `scotch`:
   - `Scottish Salmon Fresh Whole` & `Fish Scottish Salmon Fillet` (Seafood) -> EXCLUDED
   - `Rice Arborio Scotti 1kg` & `Rice Carnaroli Scotti` (Grains) -> EXCLUDED
   - `Scottish Leader Whisky 75cl` (Liquor) -> EXCLUDED
2. **Scott Furniture Exclusion**: Excluded `SCOTT BENCH ELEMENT BENCHES` (Furniture).
3. **Jackson Safety Rule**: Standalone `jackson` tagged as KC **only if** description also contains `nitrile`, `resp`, or `glove` (eliminates Kendall-Jackson wine false positives).

---

## 3. Audited Real-World Data Findings

All metrics in this section are directly verified against the computed DataFrames and output sheets in `Spend_Analysis_Output.xlsx`:

### Finding 1: Single-Distributor Reliance per Hotel Property
Each hotel property relies on a single dedicated distributor for over 99% of its PepsiCo products, with zero inter-property vendor sharing:
- **123 Company**: SRI KALYANI FOODS (INR 13.94 Lakh, **35.2%** of group Pepsi spend across 196 orders)
- **LMN Company**: SMS Commercial (INR 12.03 Lakh, **30.4%** of group Pepsi spend across 117 orders)
- **XYZ Company**: Super Enterprises (INR 11.38 Lakh, **28.8%** of group Pepsi spend across 279 orders)
- **ABC Company**: Premier Catering & Marketing (INR 2.21 Lakh, **5.6%** of group Pepsi spend across 20 orders)
*(Source: `Pepsi_By_Supplier` & `Pepsi_Hotel_Supplier_CrossTab` sheets)*

### Finding 2: Heavy Concentration of KC Spend at XYZ Company
XYZ Company accounts for **68.2%** of total Kimberly-Clark spend across the hotel group (INR 35.75 Lakh of INR 52.39 Lakh total across 128 orders)—more than double LMN Company, the next-highest hotel (23.7%, INR 12.42 Lakh across 120 orders).
*(Source: `KC_By_Hotel` sheet)*

### Finding 3: High Proportional KC Spend Share at XYZ & LMN
As a percentage of each hotel property's own total procurement spend:
- **XYZ Company**: KC products represent **0.69%** of total procurement (INR 35.75 Lakh of INR 52.03 Crores).
- **LMN Company**: KC products represent **0.47%** of total procurement (INR 12.42 Lakh of INR 26.45 Crores).
- **123 Company**: KC products represent **0.07%** of total procurement (INR 2.85 Lakh of INR 40.73 Crores).
- **ABC Company**: KC products represent **0.09%** of total procurement (INR 1.37 Lakh of INR 14.76 Crores).
*(Source: `Hotel_Total_vs_PepsiKC` sheet)*

### Finding 4: Operational Direct-from-Manufacturer Sourcing Model
"Kimberly Clark Hygiene Pvt Ltd" (the manufacturer itself) is already the single largest KC supplier in the dataset, accounting for **INR 21.02 Lakhs** (**40.1%** of total KC spend across 144 orders). Direct-from-manufacturer sourcing is already operational for part of the hygiene portfolio.
*(Source: `KC_By_Supplier` sheet)*

### Finding 5: Target Category Proportion of Total Procurement
Combined PepsiCo and Kimberly-Clark spend equals **INR 91.94 Lakhs** (Pepsi INR 39.55L + KC INR 52.39L) out of **INR 133.97 Crores** total consolidated procurement spend across 248,835 orders—representing **0.69%** of total spend.
*(Source: `Summary_Dashboard` & `Hotel_Total_vs_PepsiKC` sheets)*

---

## 4. Enterprise Architecture: Scaling to 400+ Hotels

To scale spend analytics across an enterprise network of 400+ hotel properties, keyword-based scripts should be replaced by a cloud data warehouse architecture:

```
[400+ Property Management / ERP Systems] 
       │
       ▼ (Automated Daily Ingestion via Azure Data Factory / AWS Glue)
[Master Data Management (MDM) / Master SKU Dictionary]
       │ (Fuzzy String Matching & ML Text Classification)
       ▼
[Cloud Data Warehouse: Snowflake / Databricks / BigQuery]
       │
       ▼
[Power BI / Tableau Live Executive Dashboards]
```

### Key Pillars:
1. **Master SKU Catalog**: Automated fuzzy matching (Levenshtein distance) maps incoming raw invoice descriptions to canonical Global SKU IDs.
2. **Automated ETL Pipelines**: Scheduled cloud pipelines ingest daily POS/ERP data into Snowflake/Databricks.
3. **Automated Price Audit Gates**: Real-time validation flags any invoice where unit price exceeds contract baseline by >5%.
4. **Interactive BI Layer**: Power BI / Tableau dashboards provide property-level drilldowns with automated executive alert feeds.
