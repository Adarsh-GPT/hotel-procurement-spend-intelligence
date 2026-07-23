import os
from src.config import OUTPUT_HTML_PATH

def generate_html_dashboard(output_path: str = OUTPUT_HTML_PATH) -> None:
    """Generate the single-page interactive executive HTML dashboard."""
    print("\n" + "=" * 60)
    print("STEP 9: BUILDING INTERACTIVE SINGLE-PAGE EXECUTIVE HTML DASHBOARD")
    print("=" * 60)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Procurement Spend Intelligence Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text: #0f172a;
            --primary: #1b365d;
            --accent-pepsi: #1f77b4;
            --accent-kc: #d95f02;
            --border: #e2e8f0;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 24px;
        }
        .header {
            background: linear-gradient(135deg, #1b365d 0%, #0f172a 100%);
            color: white;
            padding: 36px;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.12);
            margin-bottom: 32px;
        }
        .header h1 { margin: 0 0 8px 0; font-size: 30px; font-weight: 700; letter-spacing: -0.5px; }
        .header p { margin: 0; opacity: 0.88; font-size: 15px; font-weight: 400; }
        
        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 20px;
            margin-bottom: 32px;
        }
        .kpi-card {
            background: var(--card-bg);
            padding: 24px;
            border-radius: 14px;
            border: 1px solid var(--border);
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .kpi-card:hover { transform: translateY(-3px); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.06); }
        .kpi-title { font-size: 12px; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.6px; }
        .kpi-value { font-size: 26px; font-weight: 700; color: var(--primary); margin-top: 10px; }
        .kpi-sub { font-size: 13px; color: #64748b; margin-top: 6px; }

        .section-title {
            font-size: 22px;
            font-weight: 700;
            color: var(--primary);
            margin: 36px 0 20px 0;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--border);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .charts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(520px, 1fr));
            gap: 28px;
            margin-bottom: 36px;
        }
        .chart-card {
            background: var(--card-bg);
            border-radius: 14px;
            padding: 20px;
            border: 1px solid var(--border);
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
            text-align: center;
        }
        .chart-card img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
        }

        .insights-card {
            background: #ffffff;
            border: 1px solid var(--border);
            border-left: 6px solid var(--primary);
            padding: 28px;
            border-radius: 14px;
            margin-bottom: 36px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.02);
        }
        .insights-card h3 { margin-top: 0; color: var(--primary); font-size: 20px; font-weight: 700; }
        .insights-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .insight-item {
            background: #f8fafc;
            padding: 18px;
            border-radius: 10px;
            border: 1px solid #e2e8f0;
        }
        .insight-item h4 { margin: 0 0 8px 0; color: var(--primary); font-size: 15px; font-weight: 600; }
        .insight-item p { margin: 0; color: #334155; font-size: 13.5px; line-height: 1.5; }
        .source-tag { font-size: 11px; color: #64748b; font-style: italic; margin-top: 8px; display: block; }

        footer {
            text-align: center;
            padding: 24px;
            color: #94a3b8;
            font-size: 13px;
            border-top: 1px solid var(--border);
            margin-top: 40px;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>Hotel Procurement Spend Intelligence Dashboard</h1>
        <p>Consolidated 2019 Spend Analysis & Audited Sourcing Findings Across 4 Hotel Properties</p>
    </div>

    <div class="kpi-grid">
        <div class="kpi-card">
            <div class="kpi-title">Total Procurement Spend</div>
            <div class="kpi-value">INR 133.97 Cr</div>
            <div class="kpi-sub">248,835 Total Orders Processed</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">PepsiCo Spend</div>
            <div class="kpi-value">INR 39.55 Lakh</div>
            <div class="kpi-sub">612 Validated Transactions</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Kimberly-Clark Spend</div>
            <div class="kpi-value">INR 52.39 Lakh</div>
            <div class="kpi-sub">308 Validated Transactions</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Combined Target Share</div>
            <div class="kpi-value">0.69%</div>
            <div class="kpi-sub">Total PepsiCo + KC Procurement Share</div>
        </div>
    </div>

    <div class="insights-card">
        <h3>Audited Procurement Findings & Data Discoveries</h3>
        <div class="insights-grid">
            <div class="insight-item">
                <h4>1. Single-Distributor Reliance per Hotel Property</h4>
                <p>Each hotel sources Pepsi products from exactly one dedicated distributor with zero vendor split: SRI KALYANI FOODS supplies 123 Company (35.2% of group Pepsi spend, INR 13.94L), SMS Commercial supplies LMN Company (30.4%, INR 12.03L), Super Enterprises supplies XYZ Company (28.8%, INR 11.38L), and Premier Catering & Marketing supplies ABC Company (5.6%, INR 2.21L).</p>
                <span class="source-tag">Source: Pepsi_By_Supplier & Pepsi_Hotel_Supplier_CrossTab sheets</span>
            </div>
            <div class="insight-item">
                <h4>2. Heavy Concentration of KC Spend at XYZ Company</h4>
                <p>XYZ Company accounts for 68.2% of total Kimberly-Clark spend across the hotel group (INR 35.75 Lakh of INR 52.39 Lakh total)—more than double LMN Company, the next-highest hotel (23.7%, INR 12.42 Lakh).</p>
                <span class="source-tag">Source: KC_By_Hotel sheet</span>
            </div>
            <div class="insight-item">
                <h4>3. High Proportional KC Spend Share at XYZ & LMN</h4>
                <p>As a percentage of each hotel's own total procurement spend, KC products represent 0.69% at XYZ Company and 0.47% at LMN Company, compared to just 0.07% at 123 Company and 0.09% at ABC Company—roughly 7 to 10 times higher proportionally.</p>
                <span class="source-tag">Source: Hotel_Total_vs_PepsiKC sheet</span>
            </div>
            <div class="insight-item">
                <h4>4. Direct-from-Manufacturer Sourcing Model</h4>
                <p>Kimberly Clark Hygiene Pvt Ltd (the manufacturer itself) is already the single largest KC supplier in the dataset, accounting for INR 21.02 Lakhs (40.1% of KC spend across 144 orders). Direct manufacturer sourcing is already operational for part of the portfolio.</p>
                <span class="source-tag">Source: KC_By_Supplier sheet</span>
            </div>
            <div class="insight-item">
                <h4>5. Low Spend Share of Target Categories</h4>
                <p>Target brands PepsiCo and Kimberly-Clark combined represent only 0.69% of total 2019 procurement spend (INR 91.94 Lakh out of INR 133.97 Crores total across 248,835 orders), indicating vast un-analyzed non-food/beverage spend categories.</p>
                <span class="source-tag">Source: Summary_Dashboard & Hotel_Total_vs_PepsiKC sheets</span>
            </div>
        </div>
    </div>

    <div class="section-title">1. Executive Procurement Overview</div>
    <div class="charts-grid">
        <div class="chart-card"><img src="figures/11_category_total_spend.png" alt="Category Total Spend"></div>
        <div class="chart-card"><img src="figures/12_hotel_total_vs_pepsi_kc.png" alt="Hotel Spend Disparity"></div>
    </div>

    <div class="section-title">2. PepsiCo Spend Intelligence & Portfolio Analysis</div>
    <div class="charts-grid">
        <div class="chart-card"><img src="figures/01_pepsi_spend_by_hotel.png" alt="Pepsi by Hotel"></div>
        <div class="chart-card"><img src="figures/03_pepsi_brand_mix.png" alt="Pepsi Brand Mix"></div>
        <div class="chart-card"><img src="figures/05_top10_pepsi_products.png" alt="Top 10 Pepsi Products"></div>
        <div class="chart-card"><img src="figures/07_pepsi_spend_by_supplier.png" alt="Pepsi by Supplier"></div>
        <div class="chart-card"><img src="figures/09_pepsi_monthly_trend.png" alt="Pepsi Monthly Trend"></div>
    </div>

    <div class="section-title">3. Kimberly-Clark Hygiene & Tissue Spend Intelligence</div>
    <div class="charts-grid">
        <div class="chart-card"><img src="figures/02_kc_spend_by_hotel.png" alt="KC by Hotel"></div>
        <div class="chart-card"><img src="figures/04_kc_brand_mix.png" alt="KC Brand Mix"></div>
        <div class="chart-card"><img src="figures/06_top10_kc_products.png" alt="Top 10 KC Products"></div>
        <div class="chart-card"><img src="figures/08_kc_spend_by_supplier.png" alt="KC by Supplier"></div>
        <div class="chart-card"><img src="figures/10_kc_monthly_trend.png" alt="KC Monthly Trend"></div>
    </div>

    <footer>
        <p>Hotel Group Procurement Spend Intelligence | Strategic Sourcing & Category Management Report</p>
    </footer>

</body>
</html>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"HTML Dashboard successfully written to: {output_path}")
