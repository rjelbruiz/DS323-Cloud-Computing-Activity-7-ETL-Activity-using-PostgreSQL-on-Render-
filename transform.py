import pandas as pd
from sqlalchemy import create_engine

def clean_data(db_url):
    engine = create_engine(db_url)
    
    # Clean Japan Data
    df_jp = pd.read_sql("SELECT * FROM staging_japan_sales", engine)
    df_jp['date'] = pd.to_datetime(df_jp['date'])
    df_jp.to_sql("japan_cleaned", engine, if_exists='replace', index=False)
    
    # Clean Myanmar Data
    df_mm = pd.read_sql("SELECT * FROM staging_myanmar_sales", engine)
    df_mm['date'] = pd.to_datetime(df_mm['date'])
    df_mm.to_sql("myanmar_cleaned", engine, if_exists='replace', index=False)
    
    return "✨ Transformation Successful"
