import os
import pandas as pd
from src.config import RAW_DATA_DIR, HOTEL_FILES, STANDARD_COLUMNS

def load_and_clean_data(raw_dir: str = RAW_DATA_DIR) -> pd.DataFrame:
    """
    Ingest, harmonize schema, clean, and consolidate purchase data across 4 hotel properties.
    
    Parameters:
        raw_dir (str): Directory path containing raw Excel files.
        
    Returns:
        pd.DataFrame: Consolidated procurement DataFrame with standard columns.
    """
    print("=" * 60)
    print("STEP 1: LOADING & CONSOLIDATING PURCHASE DATA")
    print("=" * 60)
    
    # 1. 123 Company
    path_123 = os.path.join(raw_dir, HOTEL_FILES['123 Company'])
    df1 = pd.read_excel(path_123)
    df1['Hotel'] = '123 Company'
    df1 = df1.rename(columns={
        'Received date': 'Date',
        'Supplier name': 'Supplier',
        'Category name': 'Category',
        'Product name': 'Product',
        'UOM': 'UOM',
        "Rec'd qty": 'Qty',
        'Unit price': 'UnitPrice',
        'Extension': 'TotalCost'
    })[STANDARD_COLUMNS]

    # 2. ABC Company (Map Store to Category instead of assigning 'Uncategorized')
    path_abc = os.path.join(raw_dir, HOTEL_FILES['ABC Company'])
    df2 = pd.read_excel(path_abc)
    df2['Hotel'] = 'ABC Company'
    df2 = df2.rename(columns={
        'Bill Date': 'Date',
        'Vendor Name': 'Supplier',
        'Store': 'Category',
        'Product Description': 'Product',
        'UOM': 'UOM',
        'Qty': 'Qty',
        'Unit Cost': 'UnitPrice',
        'Total Cost': 'TotalCost'
    })[STANDARD_COLUMNS]

    # 3. LMN Company (Drop numeric Product code prior to rename to prevent collision)
    path_lmn = os.path.join(raw_dir, HOTEL_FILES['LMN Company'])
    df3 = pd.read_excel(path_lmn)
    if 'Product' in df3.columns and 'Product Description' in df3.columns:
        df3 = df3.drop(columns=['Product'])
    df3['Hotel'] = 'LMN Company'
    df3 = df3.rename(columns={
        'Purchase Date': 'Date',
        'Vendor Name': 'Supplier',
        'Category': 'Category',
        'Product Description': 'Product',
        'Purchase Unit': 'UOM',
        'Quantity': 'Qty',
        'Unit Cost': 'UnitPrice',
        'Total Cost': 'TotalCost'
    })[STANDARD_COLUMNS]

    # 4. XYZ Company
    path_xyz = os.path.join(raw_dir, HOTEL_FILES['XYZ Company'])
    df4 = pd.read_excel(path_xyz)
    df4['Hotel'] = 'XYZ Company'
    df4 = df4.rename(columns={
        'Received date': 'Date',
        'Supplier name': 'Supplier',
        'Category name': 'Category',
        'Product name': 'Product',
        'UOM': 'UOM',
        "Rec'd qty": 'Qty',
        'Unit price': 'UnitPrice',
        "Rec'd ext amt": 'TotalCost'
    })[STANDARD_COLUMNS]

    # Concatenate all datasets
    all_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

    # Standardize data types
    all_df['Date'] = pd.to_datetime(all_df['Date'], errors='coerce')
    all_df['Qty'] = pd.to_numeric(all_df['Qty'], errors='coerce')
    all_df['UnitPrice'] = pd.to_numeric(all_df['UnitPrice'], errors='coerce')
    all_df['TotalCost'] = pd.to_numeric(all_df['TotalCost'], errors='coerce')

    # Recompute missing TotalCost where Qty and UnitPrice exist
    missing_tc = all_df['TotalCost'].isna() & all_df['Qty'].notna() & all_df['UnitPrice'].notna()
    all_df.loc[missing_tc, 'TotalCost'] = all_df.loc[missing_tc, 'Qty'] * all_df.loc[missing_tc, 'UnitPrice']

    # Clean text strings
    for col in ['Supplier', 'Category', 'Product', 'UOM']:
        all_df[col] = all_df[col].astype(str).str.strip()
    all_df['Category'] = all_df['Category'].replace({'nan': 'Uncategorized / General', 'NaN': 'Uncategorized / General', 'None': 'Uncategorized / General', '': 'Uncategorized / General'})

    print(f"Total Consolidated Rows: {len(all_df):,}")
    print("\nRow Counts Per Hotel:")
    for hotel, count in all_df['Hotel'].value_counts().items():
        print(f"  - {hotel}: {count:,} rows")
    print(f"\nTotal Procurement Spend: INR {all_df['TotalCost'].sum():,.2f}")

    return all_df
