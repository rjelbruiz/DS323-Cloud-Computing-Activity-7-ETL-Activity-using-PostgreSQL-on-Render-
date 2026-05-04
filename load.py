import pandas as pd
from sqlalchemy import create_engine

def load_to_production(db_url):
    engine = create_engine(db_url)
    # Consolidate cleaned tables into the 'BIG TABLE' equivalent
    jp = pd.read_sql("SELECT * FROM japan_sales_cleaned", engine)
    # (Repeat for Myanmar...)
    
    final_df = jp # Simplified for example
    final_df.to_sql("fact_sales_consolidated", engine, if_exists='replace', index=False)
    return "Load Complete"
