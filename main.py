from fastapi import FastAPI
import os
from extract import extract_to_staging
from transform import clean_data
from load import load_to_production

app = FastAPI()
DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/")
def home():
    return {"message": "ETL Service is Running. Go to /run-pipeline to start."}

@app.get("/run-pipeline")
def run_pipeline():
    # Execute the steps in order
    s1 = extract_to_staging(DATABASE_URL)
    s2 = clean_data(DATABASE_URL)
    s3 = load_to_production(DATABASE_URL)
    return {"steps": [s1, s2, s3], "status": "Success"}
