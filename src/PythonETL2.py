import requests
import logging
import pandas as pd
from sqlalchemy import create_engine
import config

logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_ecom_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        logging.info("Data fetched successfully from API")
        return response.json()
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return None

def transform_ecom_data(data):
    try:
        df = pd.DataFrame(data["products"])
        # id, title, price, discount_price, category, rating, stock
        df["discount_price"]=df["price"]*(1-(df["discountPercentage"]/100))
        df=df[["id","title","price","discount_price","category","rating","stock"]]
        df=df[df["stock"]>0]
        df=df.sort_values(by="rating",ascending=False)
        # df=df.dropna()
        df=df.dropna(subset=["price","discountPercentage"])
        logging.info("Data transformed successfully")
        return df
    except Exception as e:
        logging.error(f"Error transforming data: {e}")
        return None

def load_ecom_data(df):
    try:
        engine=create_engine(config.DB_PATH)
        with engine.begin() as conn:
            df.to_sql('ETL2', conn, index=False, if_exists='append')
            logging.info("Data loaded successfully")
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None

def run_ecom_pipeline():
    url=config.API_URL
    data=fetch_ecom_data(url)
    if data :
        df=transform_ecom_data(data)
        if df is not None:
            load_ecom_data(df)
            logging.info("Data loaded to DB successfully")
    else:
        logging.info("Data not loaded successfully")

if __name__ == "__main__":
    run_ecom_pipeline()
