import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv() # Loads variables from .env (DB_URL)

def extract_to_staging():
    """
    Loads raw CSV data into PostgreSQL staging tables.
    """
    # Use your Render Database URL here
    db_url = os.getenv("DATABASE_URL") 
    engine = create_engine(db_url)
    
    # List of files to process
    files = {
        "japan": ["japan_branch.csv", "japan_Customers.csv", "japan_items.csv", "japan_payment.csv", "japan_sales_data.csv"],
        "myanmar": ["myanmar_branch.csv", "myanmar_customers.csv", "myanmar_items.csv", "myanmar_payment.csv", "myanmar_sales_data.csv"]
    }

    for country, file_list in files.items():
        for file in file_list:
            # Clean filename for table naming (e.g., japan_branch)
            table_name = f"staging_{file.replace('.csv', '').lower()}"
            
            # Read CSV - handling the quoted headers seen in your source data
            df = pd.read_csv(file)
            df.columns = [c.replace("'", "").strip() for c in df.columns]
            
            # Load to Postgres
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"✅ Extracted {file} to {table_name}")

if __name__ == "__main__":
    extract_to_staging()
