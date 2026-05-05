import pandas as pd
from sqlalchemy import create_engine

def load_to_production(db_url):
    engine = create_engine(db_url)
    
    # Combine both datasets into the "BIG TABLE"
    jp = pd.read_sql("SELECT * FROM japan_cleaned", engine)
    mm = pd.read_sql("SELECT * FROM myanmar_cleaned", engine)
    
    jp['country'] = 'Japan'
    mm['country'] = 'Myanmar'
    
    big_table = pd.concat([jp, mm], ignore_index=True)
    big_table.to_sql("fact_sales_consolidated", engine, if_exists='replace', index=False)
    
    return "Final Load Successful!"
