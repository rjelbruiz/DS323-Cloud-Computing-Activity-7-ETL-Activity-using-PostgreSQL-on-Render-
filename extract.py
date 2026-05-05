import pandas as pd
from sqlalchemy import create_engine

def extract_to_staging(db_url):
    engine = create_engine(db_url)
    # File paths for both Japan and Myanmar source data
    files = {
        "japan_sales": "japan_sales_data.csv",
        "myanmar_sales": "myanmar_sales_data.csv"
    }
    
    for table_name, file_path in files.items():
        df = pd.read_csv(file_path)
        # For quoted headers like 'invoice_id'
        df.columns = [c.replace("'", "").strip() for c in df.columns]
        # Upload to Postgres
        df.to_sql(f"staging_{table_name}", engine, if_exists='replace', index=False)
    
    return "Extraction Successful!"
