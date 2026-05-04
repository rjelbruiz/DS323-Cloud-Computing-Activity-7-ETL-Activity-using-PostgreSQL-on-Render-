import pandas as pd
from sqlalchemy import create_engine

def clean_data(db_url):
    engine = create_engine(db_url)
    # Pull from Postgres staging instead of SQLite
    df = pd.read_sql("SELECT * FROM staging_japan_sales_data", engine)
    
    # Perform your cleaning (whitespace, date conversion, etc.)
    df['date'] = pd.to_datetime(df['date'])
    
    # Save back to Postgres
    df.to_sql("japan_sales_cleaned", engine, if_exists='replace', index=False)
    return "Transformation Complete"
