import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def load_to_production():
    """
    Consolidates Japan and Myanmar cleaned tables into one master table.
    """
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    
    # Pull cleaned datasets
    jp_sales = pd.read_sql("SELECT * FROM japan_sales_cleaned", engine)
    mm_sales = pd.read_sql("SELECT * FROM myanmar_sales_cleaned", engine)
    
    # Add country identifiers
    jp_sales['country_origin'] = 'Japan'
    mm_sales['country_origin'] = 'Myanmar'
    
    # Union the datasets
    master_sales = pd.concat([jp_sales, mm_sales], ignore_index=True)
    
    # Load into final production table
    master_sales.to_sql("fact_sales_consolidated", engine, if_exists='replace', index=False)
    print("🚀 Final Load complete: 'fact_sales_consolidated' is ready on Render.")

if __name__ == "__main__":
    load_to_production()
