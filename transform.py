import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def clean_data():
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    
    # Example: Cleaning Japan Sales
    df_sales = pd.read_sql("SELECT * FROM staging_japan_sales_data", engine)
    
    # 1. Strip whitespace
    df_sales = df_sales.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # 2. Convert Dates
    df_sales['date'] = pd.to_datetime(df_sales['date'])
    
    # 3. Currency Normalization (Placeholder logic)
    # If Japan is in JPY and Myanmar is in USD, you could apply a conversion factor here
    
    # Save back to a cleaned table
    df_sales.to_sql("japan_sales_cleaned", engine, if_exists='replace', index=False)
    print("✨ Transformation complete: Japan Sales cleaned.")

if __name__ == "__main__":
    clean_data()
