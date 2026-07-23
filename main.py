#!/usr/bin/env python3
"""
Hotel Procurement Spend Intelligence & Audited Sourcing Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Senior Data Analyst Portfolio - CLI Entry Point Runner

Usage:
    python main.py
    python main.py --raw-dir data/raw --reports-dir reports
    python main.py --verify
"""

import os
import sys
import argparse
from src.config import RAW_DATA_DIR, REPORTS_DIR, FIGURES_DIR, OUTPUT_EXCEL_PATH, OUTPUT_HTML_PATH, OUTPUT_METHODOLOGY_PATH
from src.data_loader import load_and_clean_data
from src.classifier import classify_pepsi_products, classify_kc_products, tag_brands_and_skus
from src.analyzer import build_all_analyses
from src.visualizer import generate_all_visualizations
from src.excel_exporter import export_excel
from src.html_reporter import generate_html_dashboard
from src.utils import generate_methodology_doc, verify_all_claims

def parse_args():
    parser = argparse.ArgumentParser(description="Run Hotel Procurement Spend Intelligence Pipeline")
    parser.add_argument("--raw-dir", type=str, default=RAW_DATA_DIR, help="Path to directory containing raw hotel Excel files")
    parser.add_argument("--reports-dir", type=str, default=REPORTS_DIR, help="Path to directory for report outputs")
    parser.add_argument("--figures-dir", type=str, default=FIGURES_DIR, help="Path to directory for chart figure outputs")
    parser.add_argument("--skip-charts", action="store_true", help="Skip generating visual charts")
    parser.add_argument("--skip-excel", action="store_true", help="Skip generating Excel workbook")
    parser.add_argument("--verify-only", action="store_true", help="Run claim verification on existing pipeline")
    return parser.parse_args()

def main():
    args = parse_args()
    
    print("=" * 70)
    print(" HOTEL PROCUREMENT SPEND INTELLIGENCE & AUDITED SOURCING PIPELINE ")
    print("=" * 70)
    
    # Step 1: Ingest & Clean Data
    all_df = load_and_clean_data(raw_dir=args.raw_dir)
    
    # Step 2: Categorization & False Positive Handling
    all_df = classify_pepsi_products(all_df)
    all_df = classify_kc_products(all_df)
    all_df = tag_brands_and_skus(all_df)
    
    # Step 3: Analytical Aggregations
    tables = build_all_analyses(all_df)
    
    # Step 4: Visualizations
    if not args.skip_charts:
        generate_all_visualizations(tables, figures_dir=args.figures_dir)
        
    # Step 5: Excel Report Export
    excel_path = os.path.join(args.reports_dir, "Spend_Analysis_Output.xlsx")
    if not args.skip_excel:
        export_excel(tables, all_df, output_path=excel_path)
        
    # Step 6: HTML Executive Dashboard
    html_path = os.path.join(args.reports_dir, "dashboard.html")
    generate_html_dashboard(output_path=html_path)
    
    # Step 7: Methodology Documentation
    generate_methodology_doc(all_df, output_path=OUTPUT_METHODOLOGY_PATH)
    
    # Step 8: Audited Claim Verification
    verify_all_claims(tables, all_df)
    
    print("\n" + "=" * 70)
    print(" PIPELINE EXECUTION COMPLETE - ALL ENTERPRISE ARTIFACTS GENERATED ")
    print("=" * 70)

if __name__ == '__main__':
    main()
