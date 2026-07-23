import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from typing import Dict, Any
from src.config import FIGURES_DIR

# Set clean aesthetic style for matplotlib charts
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 10})

def generate_all_visualizations(tables: Dict[str, pd.DataFrame], figures_dir: str = FIGURES_DIR) -> None:
    """Generate 14 publication-quality high-resolution charts."""
    print("\n" + "=" * 60)
    print("STEP 7: GENERATING 12 HIGH-IMPACT VISUAL CHARTS")
    print("=" * 60)
    
    os.makedirs(figures_dir, exist_ok=True)
    
    # 1. Bar Chart - Pepsi spend by hotel
    fig, ax = plt.subplots(figsize=(9, 5))
    df = tables['pepsi_by_hotel']
    bars = ax.bar(df['Hotel'], df['TotalSpend'] / 1e5, color='#1b365d', edgecolor='black', alpha=0.9, width=0.55)
    ax.set_title('PepsiCo Procurement Spend by Hotel Property', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel('Total Spend (INR Lakhs)', fontsize=12, fontweight='bold')
    ax.set_ylim(0, max(df['TotalSpend']/1e5) * 1.25)
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'INR {height:.2f}L', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', fontweight='bold', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '01_pepsi_spend_by_hotel.png'), dpi=300)
    plt.close()

    # 2. Bar Chart - KC spend by hotel
    fig, ax = plt.subplots(figsize=(9, 5))
    df = tables['kc_by_hotel']
    bars = ax.bar(df['Hotel'], df['TotalSpend'] / 1e5, color='#d95f02', edgecolor='black', alpha=0.9, width=0.55)
    ax.set_title('Kimberly-Clark Procurement Spend by Hotel Property', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel('Total Spend (INR Lakhs)', fontsize=12, fontweight='bold')
    ax.set_ylim(0, max(df['TotalSpend']/1e5) * 1.25)
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'INR {height:.2f}L', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', fontweight='bold', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '02_kc_spend_by_hotel.png'), dpi=300)
    plt.close()

    # 3. Donut chart - Pepsi brand mix
    fig, ax = plt.subplots(figsize=(8, 6))
    df = tables['pepsi_by_brand']
    wedges, texts, autotexts = ax.pie(
        df['TotalSpend'],
        autopct='%1.1f%%',
        pctdistance=0.72,
        startangle=140,
        colors=sns.color_palette("Blues_r", len(df)),
        wedgeprops=dict(width=0.42, edgecolor='white', linewidth=2.5)
    )
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_weight('bold')
        autotext.set_fontsize(11)
    ax.legend(wedges, df['Brand'], title="Brand", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), frameon=True, fontsize=10)
    ax.set_title('PepsiCo Portfolio Brand Spend Mix (% Share)', fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '03_pepsi_brand_mix.png'), dpi=300)
    plt.close()

    # 4. Donut chart - KC brand mix
    fig, ax = plt.subplots(figsize=(8, 6))
    df = tables['kc_by_brand']
    wedges, texts, autotexts = ax.pie(
        df['TotalSpend'],
        autopct='%1.1f%%',
        pctdistance=0.72,
        startangle=140,
        colors=sns.color_palette("YlOrBr_r", len(df)),
        wedgeprops=dict(width=0.42, edgecolor='white', linewidth=2.5)
    )
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_weight('bold')
        autotext.set_fontsize(10)
    ax.legend(wedges, df['Brand'], title="Brand", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), frameon=True, fontsize=10)
    ax.set_title('Kimberly-Clark Portfolio Brand Spend Mix (% Share)', fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '04_kc_brand_mix.png'), dpi=300)
    plt.close()

    # 5. Horizontal bar chart - Top 10 Pepsi products
    fig, ax = plt.subplots(figsize=(11, 6))
    df = tables['pepsi_by_prod'].head(10).sort_values(by='TotalSpend', ascending=True)
    bars = ax.barh(df['Product'], df['TotalSpend'] / 1e5, color='#1b365d', edgecolor='black', alpha=0.85, height=0.65)
    ax.set_title('Top 10 Pepsi Products by Procurement Spend', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Total Spend (INR Lakhs)', fontsize=12, fontweight='bold')
    ax.set_xlim(0, max(df['TotalSpend']/1e5) * 1.2)
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'INR {width:.2f}L', xy=(width, bar.get_y() + bar.get_height()/2),
                    xytext=(6, 0), textcoords="offset points", ha='left', va='center', fontweight='bold', fontsize=9.5)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '05_top10_pepsi_products.png'), dpi=300)
    plt.close()

    # 6. Horizontal bar chart - Top 10 KC products
    fig, ax = plt.subplots(figsize=(11, 6))
    df = tables['kc_by_prod'].head(10).sort_values(by='TotalSpend', ascending=True)
    bars = ax.barh(df['Product'], df['TotalSpend'] / 1e5, color='#d95f02', edgecolor='black', alpha=0.85, height=0.65)
    ax.set_title('Top 10 Kimberly-Clark Products by Procurement Spend', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Total Spend (INR Lakhs)', fontsize=12, fontweight='bold')
    ax.set_xlim(0, max(df['TotalSpend']/1e5) * 1.2)
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'INR {width:.2f}L', xy=(width, bar.get_y() + bar.get_height()/2),
                    xytext=(6, 0), textcoords="offset points", ha='left', va='center', fontweight='bold', fontsize=9.5)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '06_top10_kc_products.png'), dpi=300)
    plt.close()

    # 7. Bar chart - Pepsi spend by supplier
    fig, ax = plt.subplots(figsize=(10, 5.5))
    df = tables['pepsi_by_supp'].head(8)
    bars = ax.bar(df['Supplier'], df['TotalSpend'] / 1e5, color='#3182bd', edgecolor='black', alpha=0.85, width=0.55)
    ax.set_title('Pepsi Spend Distribution Across Suppliers', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel('Total Spend (INR Lakhs)', fontsize=12, fontweight='bold')
    ax.set_ylim(0, max(df['TotalSpend']/1e5) * 1.25)
    plt.xticks(rotation=25, ha='right', fontsize=9.5)
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'INR {height:.2f}L', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', fontweight='bold', fontsize=9.5)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '07_pepsi_spend_by_supplier.png'), dpi=300)
    plt.close()

    # 8. Bar chart - KC spend by supplier
    fig, ax = plt.subplots(figsize=(10, 5.5))
    df = tables['kc_by_supp'].head(8)
    bars = ax.bar(df['Supplier'], df['TotalSpend'] / 1e5, color='#e66101', edgecolor='black', alpha=0.85, width=0.55)
    ax.set_title('Kimberly-Clark Spend Distribution Across Suppliers', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel('Total Spend (INR Lakhs)', fontsize=12, fontweight='bold')
    ax.set_ylim(0, max(df['TotalSpend']/1e5) * 1.25)
    plt.xticks(rotation=25, ha='right', fontsize=9.5)
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'INR {height:.2f}L', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', fontweight='bold', fontsize=9.5)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '08_kc_spend_by_supplier.png'), dpi=300)
    plt.close()

    # 9. Line chart - Pepsi monthly spend trend
    fig, ax = plt.subplots(figsize=(10, 5))
    df = tables['pepsi_monthly'].sort_values(by='Month')
    ax.plot(df['Month'], df['TotalSpend'] / 1e5, marker='o', color='#1f77b4', linewidth=2.5, markersize=8)
    ax.set_title('2019 Pepsi Monthly Procurement Spend Seasonality', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel('Spend (INR Lakhs)', fontsize=12, fontweight='bold')
    ax.set_ylim(0, max(df['TotalSpend']/1e5) * 1.25)
    plt.xticks(rotation=45)
    for i, row in df.iterrows():
        ax.annotate(f"INR {row['TotalSpend']/1e5:.1f}L", (row['Month'], row['TotalSpend']/1e5),
                    textcoords="offset points", xytext=(0,8), ha='center', fontsize=8.5, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '09_pepsi_monthly_trend.png'), dpi=300)
    plt.close()

    # 10. Line chart - KC monthly spend trend
    fig, ax = plt.subplots(figsize=(10, 5))
    df = tables['kc_monthly'].sort_values(by='Month')
    ax.plot(df['Month'], df['TotalSpend'] / 1e5, marker='s', color='#ff7f0e', linewidth=2.5, markersize=8)
    ax.set_title('2019 Kimberly-Clark Monthly Procurement Spend Seasonality', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel('Spend (INR Lakhs)', fontsize=12, fontweight='bold')
    ax.set_ylim(0, max(df['TotalSpend']/1e5) * 1.25)
    plt.xticks(rotation=45)
    for i, row in df.iterrows():
        ax.annotate(f"INR {row['TotalSpend']/1e5:.1f}L", (row['Month'], row['TotalSpend']/1e5),
                    textcoords="offset points", xytext=(0,8), ha='center', fontsize=8.5, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '10_kc_monthly_trend.png'), dpi=300)
    plt.close()

    # 11. Bar chart - Category-wise total spend
    fig, ax = plt.subplots(figsize=(11, 6.5))
    df = tables['cat_spend'].head(15).sort_values(by='TotalSpend', ascending=True)
    bars = ax.barh(df['Category'], df['TotalSpend'] / 1e7, color='#2c3e50', edgecolor='black', alpha=0.85, height=0.65)
    ax.set_title('Top 15 Procurement Categories Across All Hotels (INR Crores)', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Total Spend (INR Crores)', fontsize=12, fontweight='bold')
    ax.set_xlim(0, max(df['TotalSpend']/1e7) * 1.2)
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'INR {width:.2f}Cr', xy=(width, bar.get_y() + bar.get_height()/2),
                    xytext=(6, 0), textcoords="offset points", ha='left', va='center', fontweight='bold', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '11_category_total_spend.png'), dpi=300)
    plt.close()

    # 12. Grouped bar chart - Hotel Total Spend vs Pepsi vs KC
    fig, ax1 = plt.subplots(figsize=(11, 6))
    df = tables['hotel_comparison']
    x = np.arange(len(df['Hotel']))
    width = 0.35

    ax1.bar(x - width/2, df['TotalProcurementSpend'] / 1e8, width, label='Total Procurement (INR Cr)', color='#1b365d', alpha=0.9)
    ax1.set_ylabel('Total Hotel Spend (INR Crores)', fontsize=12, fontweight='bold', color='#1b365d')
    ax1.set_xticks(x)
    ax1.set_xticklabels(df['Hotel'], fontweight='bold', fontsize=11)

    ax2 = ax1.twinx()
    ax2.bar(x + width/2, df['KCSpend'] / 1e5, width, label='KC Brand Spend (INR Lakhs)', color='#d95f02', alpha=0.9)
    ax2.set_ylabel('Target Brand Spend (INR Lakhs)', fontsize=12, fontweight='bold', color='#d95f02')

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', frameon=True)

    plt.title('Hotel Property Total Procurement vs Target Brand Spend Disparity', fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, '12_hotel_total_vs_pepsi_kc.png'), dpi=300)
    plt.close()

    print(f"All 12 visual charts successfully generated and saved to: {figures_dir}")
