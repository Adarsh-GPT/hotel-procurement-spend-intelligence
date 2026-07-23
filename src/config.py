import os
import re

# Base Directory Paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(PROJECT_ROOT, 'data', 'raw')
PROCESSED_DATA_DIR = os.path.join(PROJECT_ROOT, 'data', 'processed')
REPORTS_DIR = os.path.join(PROJECT_ROOT, 'reports')
FIGURES_DIR = os.path.join(REPORTS_DIR, 'figures')
DOCS_DIR = os.path.join(PROJECT_ROOT, 'docs')

# Target Output File Paths
OUTPUT_EXCEL_PATH = os.path.join(REPORTS_DIR, 'Spend_Analysis_Output.xlsx')
OUTPUT_HTML_PATH = os.path.join(REPORTS_DIR, 'dashboard.html')
OUTPUT_METHODOLOGY_PATH = os.path.join(DOCS_DIR, 'Methodology.md')

# Raw Hotel Data File Names
HOTEL_FILES = {
    '123 Company': '123 Company.xlsx',
    'ABC Company': 'ABC Company.xlsx',
    'LMN Company': 'LMN Company.xlsx',
    'XYZ Company': 'XYZ Company.xlsx'
}

# Standard Output Schema Columns
STANDARD_COLUMNS = ['Hotel', 'Date', 'Supplier', 'Category', 'Product', 'UOM', 'Qty', 'UnitPrice', 'TotalCost']

# Regex Patterns for Target Product Classification
PEPSI_REGEX = r'\b(?:pepsi|mirinda|7\s?up|mountain\s?dew|dukes?|lehar)\b'
KC_REGEX = r'\b(?:kleenex|kimsoft|kimtech|wypall|micromist|kleen\s?guard|k\.?c\.?\s?professional|kcp|\bscott\b)\b'

# False Positive Regex Rules
SCOTT_FP_REGEX = r'scottish|scotti|scotch'
SCOTT_BENCH_FP_REGEX = r'scott\s+bench'
JACKSON_REGEX = r'\bjackson\b'
JACKSON_VALID_REGEX = r'nitrile|resp|glove'

def get_pepsi_brand(product_name: str) -> str:
    """Map raw product description to canonical PepsiCo brand."""
    p = str(product_name).lower()
    if 'mirinda' in p:
        return 'Mirinda'
    if re.search(r'7\s?up', p):
        return '7Up'
    if 'mountain' in p and 'dew' in p:
        return 'Mountain Dew'
    if 'everess' in p or 'lehar' in p:
        return 'Lehar Everess Soda'
    if 'duke' in p:
        return "Duke's Soda & Tonic"
    if 'pepsi' in p:
        return 'Pepsi'
    return 'Other Pepsi'

def get_kc_brand(product_name: str) -> str:
    """Map raw product description to canonical Kimberly-Clark brand."""
    p = str(product_name).lower()
    if 'kleenex' in p:
        return 'Kleenex'
    if 'kimsoft' in p:
        return 'Kimsoft'
    if 'kimtech' in p:
        return 'Kimtech'
    if 'wypall' in p:
        return 'Wypall'
    if 'kleen' in p and 'guard' in p:
        return 'KleenGuard'
    if 'micromist' in p:
        return 'Micromist'
    if 'kcp' in p or 'kc professional' in p:
        return 'KC Professional'
    if 'jackson' in p:
        return 'Jackson Safety'
    if 'scott' in p:
        return 'Scott'
    return 'Other KC'

def normalize_pepsi_sku(product_name: str) -> str:
    """Normalize raw PepsiCo product description into a canonical Standard SKU."""
    p = str(product_name).lower()
    if 'diet' in p and 'can' in p:
        return 'Pepsi Diet Can 330ml'
    if 'diet' in p or 'black' in p:
        return 'Pepsi Diet / Black 300ml'
    if '7' in p and 'can' in p:
        return '7Up Can 330ml'
    if '7' in p:
        return '7Up Glass Bottle 300ml'
    if 'mirinda' in p and 'can' in p:
        return 'Mirinda Can 330ml'
    if 'mirinda' in p:
        return 'Mirinda Glass Bottle 300ml'
    if 'everess' in p or 'lehar' in p:
        return 'Everess / Lehar Soda 300ml'
    if 'tonic' in p:
        return 'Dukes Tonic Water 300ml'
    if 'duke' in p:
        return 'Dukes Soda 300ml'
    if 'can' in p:
        return 'Pepsi Can 330ml'
    if 'pepsi' in p:
        return 'Pepsi Glass Bottle 300ml'
    return 'Other Pepsi SKU'

def normalize_kc_sku(product_name: str) -> str:
    """Normalize raw Kimberly-Clark product description into a canonical Standard SKU."""
    p = str(product_name).lower()
    if 'kleenex' in p and ('facial' in p or 'box' in p or '1295' in p or '1282' in p or 'ft' in p):
        return 'Kleenex Facial Tissue (Box)'
    if 'kleenex' in p and ('bath' in p or 'roll' in p or '1272' in p or '1308' in p):
        return 'Kleenex Bathroom Tissue (Roll)'
    if 'kleenex' in p and 'napkin' in p:
        return 'Kleenex Dinner / Cocktail Napkin'
    if 'kleenex' in p and 'hand' in p:
        return 'Kleenex Executive Hand Towel'
    if 'scott' in p and ('m/fold' in p or 'multifold' in p or 'm-fold' in p or 'm fold' in p or '28620' in p):
        return 'Scott Multifold Towel (M-Fold)'
    if 'scott' in p and ('hrt' in p or 'hand roll' in p or 'roll towel' in p or 'slimroll' in p):
        return 'Scott Hand Roll Towel (HRT)'
    if 'scott' in p and 'napkin' in p:
        return 'Scott Interfold Napkin'
    if 'kimsoft' in p and ('bath' in p or 'tissue' in p or '01212' in p or '04003' in p):
        return 'Kimsoft Bathroom Tissue'
    if 'kimsoft' in p:
        return 'Kimsoft Hand Roll Towel'
    if 'kimtech' in p or 'wypall' in p:
        return 'Kimtech / Wypall Industrial Wiper'
    if 'micromist' in p:
        return 'Micromist Air Freshener Refill'
    if 'glove' in p or 'nitrile' in p or 'guard' in p or 'resp' in p or 'jackson' in p:
        return 'KC Safety (Gloves / Respirators)'
    return 'Other KC Hygiene SKU'
