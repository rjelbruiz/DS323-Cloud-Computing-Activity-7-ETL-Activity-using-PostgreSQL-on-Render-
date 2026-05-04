from extract import extract_to_staging
from transform import clean_data
from load import load_to_production

if __name__ == "__main__":
    extract_to_staging()
    clean_data()
    load_to_production()
