import pandas as pd

def check_columns(output_df, output_df_name, required_columns):
    results = []
    for col in required_columns:
        exists = col in output_df.columns
        results.append({'Dataset': output_df_name, 'Column': col, 'Exists': '✅' if exists else '❌'})
    return results

def safe_check(output_df_name, required_columns):
    results = []
    if output_df_name in globals():
        obj = globals()[output_df_name]
        if isinstance(obj, pd.DataFrame):
            results.extend(check_columns(obj, output_df_name, required_columns))
        elif isinstance(obj, str) and ("SELECT" in obj.upper() or "FROM" in obj.upper()):
            results.append({'Dataset': output_df_name, 'Column': '—', 'Exists': 'ℹ️ SQL query string'})
        else:
            results.append({'Dataset': output_df_name, 'Column': '—', 'Exists': '❌ Not a DataFrame or query'})
    else:
        results.append({'Dataset': output_df_name, 'Column': '—', 'Exists': '❌ Variable not defined'})
    return results

requirements = {
    'missing_year': ['missing_year'],
    'clean_data': ['product_id', 'product_type', 'brand', 'weight', 'price', 'average_units_sold', 'year_added', 'stock_location'],
    'min_max_product': ['product_type', 'min_price', 'max_price'],
    'average_price_product': ['product_id', 'price', 'average_units_sold']    
}

all_results = []
for output_df_name, cols in requirements.items():
    all_results += safe_check(output_df_name, cols)

check_results_df = pd.DataFrame(all_results)

print(check_results_df)