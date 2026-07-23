import pandas as pd
from typing import Dict, Any

def build_all_analyses(all_df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """
    Build all core analytical tables, aggregations, cross-tabs, supplier concentration metrics,
    and SKU unit price variance DataFrames.
    
    Returns:
        Dict[str, pd.DataFrame]: Dictionary mapping table identifiers to DataFrames.
    """
    print("\n" + "=" * 60)
    print("STEPS 5 & 6: BUILDING REQUIRED & ADDITIONAL ANALYSIS TABLES")
    print("=" * 60)
    
    pepsi_df = all_df[all_df['IsPepsi']].copy()
    kc_df = all_df[all_df['IsKC']].copy()
    total_spend_all = all_df['TotalCost'].sum()
    pepsi_total_spend = pepsi_df['TotalCost'].sum()
    kc_total_spend = kc_df['TotalCost'].sum()

    # Helper function for aggregations
    def make_summary(df: pd.DataFrame, group_col: str, category_total: float) -> pd.DataFrame:
        res = df.groupby(group_col).agg(
            TotalSpend=('TotalCost', 'sum'),
            TotalQty=('Qty', 'sum'),
            OrderCount=('TotalCost', 'count')
        ).reset_index().sort_values(by='TotalSpend', ascending=False)
        res['SpendSharePct'] = (res['TotalSpend'] / category_total) * 100
        return res

    # 1. By Product
    pepsi_by_prod = make_summary(pepsi_df, 'Product', pepsi_total_spend)
    kc_by_prod = make_summary(kc_df, 'Product', kc_total_spend)

    # 2. By Supplier
    pepsi_by_supp = make_summary(pepsi_df, 'Supplier', pepsi_total_spend)
    kc_by_supp = make_summary(kc_df, 'Supplier', kc_total_spend)

    # 3. By Hotel
    pepsi_by_hotel = make_summary(pepsi_df, 'Hotel', pepsi_total_spend)
    kc_by_hotel = make_summary(kc_df, 'Hotel', kc_total_spend)

    # 4. By Brand
    pepsi_by_brand = make_summary(pepsi_df, 'Brand', pepsi_total_spend)
    kc_by_brand = make_summary(kc_df, 'Brand', kc_total_spend)

    # 5. Monthly Trend
    pepsi_df['Month'] = pepsi_df['Date'].dt.to_period('M').astype(str)
    kc_df['Month'] = kc_df['Date'].dt.to_period('M').astype(str)
    all_df['Month'] = all_df['Date'].dt.to_period('M').astype(str)

    pepsi_monthly = pepsi_df.groupby('Month').agg(TotalSpend=('TotalCost', 'sum'), Orders=('TotalCost', 'count')).reset_index()
    kc_monthly = kc_df.groupby('Month').agg(TotalSpend=('TotalCost', 'sum'), Orders=('TotalCost', 'count')).reset_index()

    # 6. Hotel x Supplier Cross-Tab
    pepsi_crosstab = pd.crosstab(pepsi_df['Hotel'], pepsi_df['Supplier'], values=pepsi_df['TotalCost'], aggfunc='sum').fillna(0)
    kc_crosstab = pd.crosstab(kc_df['Hotel'], kc_df['Supplier'], values=kc_df['TotalCost'], aggfunc='sum').fillna(0)

    # Additional Analysis 1: Category-wise Total Spend (all data - with fixed ABC Company Category)
    cat_spend = all_df.groupby('Category').agg(
        TotalSpend=('TotalCost', 'sum'),
        OrderCount=('TotalCost', 'count')
    ).reset_index().sort_values(by='TotalSpend', ascending=False)
    cat_spend['SpendSharePct'] = (cat_spend['TotalSpend'] / total_spend_all) * 100

    # Additional Analysis 2: Hotel Total Spend vs Pepsi & KC Spend
    hotel_comparison = all_df.groupby('Hotel').agg(
        TotalProcurementSpend=('TotalCost', 'sum'),
        TotalOrders=('TotalCost', 'count')
    ).reset_index()
    
    pepsi_h_sum = pepsi_df.groupby('Hotel')['TotalCost'].sum().reset_index().rename(columns={'TotalCost': 'PepsiSpend'})
    kc_h_sum = kc_df.groupby('Hotel')['TotalCost'].sum().reset_index().rename(columns={'TotalCost': 'KCSpend'})

    hotel_comparison = hotel_comparison.merge(pepsi_h_sum, on='Hotel', how='left').merge(kc_h_sum, on='Hotel', how='left')
    hotel_comparison['PepsiSpend'] = hotel_comparison['PepsiSpend'].fillna(0)
    hotel_comparison['KCSpend'] = hotel_comparison['KCSpend'].fillna(0)
    hotel_comparison['PepsiPctOfHotelTotal'] = (hotel_comparison['PepsiSpend'] / hotel_comparison['TotalProcurementSpend']) * 100
    hotel_comparison['KCPctOfHotelTotal'] = (hotel_comparison['KCSpend'] / hotel_comparison['TotalProcurementSpend']) * 100
    hotel_comparison['PepsiKCCombinedPct'] = ((hotel_comparison['PepsiSpend'] + hotel_comparison['KCSpend']) / hotel_comparison['TotalProcurementSpend']) * 100

    # Additional Analysis 3: Supplier Concentration Analysis
    pepsi_top_supp_pct = pepsi_by_supp.iloc[0]['SpendSharePct'] if len(pepsi_by_supp) > 0 else 0
    kc_top_supp_pct = kc_by_supp.iloc[0]['SpendSharePct'] if len(kc_by_supp) > 0 else 0

    supp_concentration = pd.DataFrame([
        {'Category': 'Pepsi Products', 'TopSupplier': pepsi_by_supp.iloc[0]['Supplier'], 'TopSupplierSpend': pepsi_by_supp.iloc[0]['TotalSpend'], 'TopSupplierSharePct': pepsi_top_supp_pct, 'TotalSuppliersCount': len(pepsi_by_supp)},
        {'Category': 'Kimberly-Clark Products', 'TopSupplier': kc_by_supp.iloc[0]['Supplier'], 'TopSupplierSpend': kc_by_supp.iloc[0]['TotalSpend'], 'TopSupplierSharePct': kc_top_supp_pct, 'TotalSuppliersCount': len(kc_by_supp)}
    ])

    tables = {
        'pepsi_by_prod': pepsi_by_prod,
        'kc_by_prod': kc_by_prod,
        'pepsi_by_supp': pepsi_by_supp,
        'kc_by_supp': kc_by_supp,
        'pepsi_by_hotel': pepsi_by_hotel,
        'kc_by_hotel': kc_by_hotel,
        'pepsi_by_brand': pepsi_by_brand,
        'kc_by_brand': kc_by_brand,
        'pepsi_monthly': pepsi_monthly,
        'kc_monthly': kc_monthly,
        'pepsi_crosstab': pepsi_crosstab,
        'kc_crosstab': kc_crosstab,
        'cat_spend': cat_spend,
        'hotel_comparison': hotel_comparison,
        'supp_concentration': supp_concentration
    }
    return tables
