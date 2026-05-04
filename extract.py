import pandas as pd
from sqlalchemy import create_engine
import os

def extract_to_staging(db_url):
    engine = create_engine(db_url)
    # Define your source files
    files = ["japan_sales_data.csv", "myanmar_sales_data.csv"] 
    for file in files:
        df = pd.read_csv(file)
        # Clean headers (handling those single quotes from your source files)
        df.columns = [c.replace("'", "").strip() for c in df.columns]
        table_name = f"staging_{file.split('.')[0]}"
        df.to_sql(table_name, engine, if_exists='replace', index=False)
    return "Extraction Complete"
