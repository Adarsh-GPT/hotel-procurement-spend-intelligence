import pandas as pd
from src.config import (
    PEPSI_REGEX, KC_REGEX, SCOTT_FP_REGEX, SCOTT_BENCH_FP_REGEX,
    JACKSON_REGEX, JACKSON_VALID_REGEX,
    get_pepsi_brand, get_kc_brand, normalize_pepsi_sku, normalize_kc_sku
)

def classify_pepsi_products(all_df: pd.DataFrame) -> pd.DataFrame:
    """Classify PepsiCo transactions using regex pattern matching."""
    print("\n" + "=" * 60)
    print("STEP 2: CLASSIFYING PEPSI PRODUCTS")
    print("=" * 60)
    
    all_df['IsPepsi'] = all_df['Product'].str.contains(PEPSI_REGEX, case=False, regex=True)

    pepsi_df = all_df[all_df['IsPepsi']]
    print(f"Pepsi Transactions Found: {len(pepsi_df):,} rows")
    print(f"Total Pepsi Spend: INR {pepsi_df['TotalCost'].sum():,.2f}")
    return all_df

def classify_kc_products(all_df: pd.DataFrame) -> pd.DataFrame:
    """
    Classify Kimberly-Clark (KC) hygiene products with strict false-positive exclusions:
    1. Excludes Scottish salmon, Scotti rice, Scotch whisky.
    2. Excludes Scott bench furniture.
    3. Excludes standalone Jackson items unless description contains nitrile, resp, or glove.
    """
    print("\n" + "=" * 60)
    print("STEP 3: CLASSIFYING KIMBERLY-CLARK (KC) PRODUCTS & HANDLING FALSE POSITIVES")
    print("=" * 60)
    
    all_df['IsKC'] = all_df['Product'].str.contains(KC_REGEX, case=False, regex=True)

    # 1. SCOTT false positives: scottish, scotti, scotch
    scott_fp = all_df['Product'].str.contains(SCOTT_FP_REGEX, case=False, regex=True)
    all_df.loc[scott_fp, 'IsKC'] = False

    # 2. Scott bench furniture
    scott_bench_fp = all_df['Product'].str.contains(SCOTT_BENCH_FP_REGEX, case=False, regex=True)
    all_df.loc[scott_bench_fp, 'IsKC'] = False

    # 3. Jackson safety rule: standalone jackson excluded unless nitrile, resp, or glove is present
    jackson_match = all_df['Product'].str.contains(JACKSON_REGEX, case=False, regex=True)
    jackson_valid = all_df['Product'].str.contains(JACKSON_VALID_REGEX, case=False, regex=True)
    all_df.loc[jackson_match & ~jackson_valid, 'IsKC'] = False

    kc_df = all_df[all_df['IsKC']]
    print(f"KC Transactions Found (after FP exclusions): {len(kc_df):,} rows")
    print(f"Total KC Spend: INR {kc_df['TotalCost'].sum():,.2f}")

    print("\n--- EXCLUDED FALSE POSITIVE CHECK ('scott' substring excluded items) ---")
    scott_all = all_df[all_df['Product'].str.contains(r'scott', case=False, regex=True)]
    excluded_scotts = scott_all[~scott_all['IsKC']]['Product'].unique()
    for item in excluded_scotts:
        print(f"  [EXCLUDED FP] {item}")

    return all_df

def tag_brands_and_skus(all_df: pd.DataFrame) -> pd.DataFrame:
    """Tag canonical Brand and Standard_SKU columns for Pepsi and KC products."""
    print("\n" + "=" * 60)
    print("STEP 4: BRAND-LEVEL TAGGING & SKU STANDARDIZATION")
    print("=" * 60)
    
    all_df['Brand'] = 'Non-Target'
    all_df.loc[all_df['IsPepsi'], 'Brand'] = all_df.loc[all_df['IsPepsi'], 'Product'].apply(get_pepsi_brand)
    all_df.loc[all_df['IsKC'], 'Brand'] = all_df.loc[all_df['IsKC'], 'Product'].apply(get_kc_brand)

    all_df['Standard_SKU'] = 'Non-Target'
    all_df.loc[all_df['IsPepsi'], 'Standard_SKU'] = all_df.loc[all_df['IsPepsi'], 'Product'].apply(normalize_pepsi_sku)
    all_df.loc[all_df['IsKC'], 'Standard_SKU'] = all_df.loc[all_df['IsKC'], 'Product'].apply(normalize_kc_sku)

    print("Pepsi Brand Tagging Breakdown:")
    print(all_df[all_df['IsPepsi']].groupby('Brand')['TotalCost'].agg(['count', 'sum']))
    print("\nKC Brand Tagging Breakdown:")
    print(all_df[all_df['IsKC']].groupby('Brand')['TotalCost'].agg(['count', 'sum']))

    return all_df
