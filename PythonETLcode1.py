import pandas as pd
import requests
import logging
from sqlalchemy import create_engine

logging.basicConfig(
    filename="ETL1.log",
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s - %(message)s'
)

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info("Data fetched from API")
        return response.json()
    except Exception as e:
        logging.error(f"Error fetching data from API: {e}")


def transform_data(data):
    try:
        df=pd.DataFrame(data)
        df["city"]=df["address"].apply(lambda x:x["city"] if isinstance(x, dict) else x)
        logging.info("city extracted from nested JSON")
        df=df[["id","name","email","city"]]
        return df
    except Exception as e:
        logging.error(f"Error transforming data into DataFrame: {e}")

def store_data(df):
    try:
        engine=create_engine("sqlite:///users.bd")
        with engine.connect() as conn:
            logging.info("engine created")
            df.to_sql("users",conn,if_exists="replace",index=False)
            logging.info("Data stored in DB")
    except Exception as e:
        logging.error(f"Error storing data into DB: {e}")


def run_pipeline():
    url="https://jsonplaceholder.typicode.com/users"
    data=fetch_data(url)
    if data :
        df=transform_data(data)
        store_data(df)
    else:
        logging.info("API unsuccessful")

if __name__ == "__main__":
    run_pipeline()