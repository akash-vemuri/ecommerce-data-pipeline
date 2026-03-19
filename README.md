# 📊 E-commerce Data Pipeline (ETL)

## 🚀 Overview

This project implements a production-style ETL pipeline that extracts product data from a REST API, transforms nested JSON into structured format, and loads it into a SQLite database.

---

## 🧩 Architecture

```
API → Python (Requests) → Pandas (Transform) → SQLite (Storage)
```

---

## 🔄 Pipeline Flow

### 1. Extract

* Fetch product data from API using `requests`
* Handle API failures with exception handling

### 2. Transform

* Convert JSON → Pandas DataFrame
* Handle nested JSON (`products`)
* Create new column: `discount_price`
* Filter out out-of-stock products
* Sort by rating (descending)

### 3. Load

* Store processed data into SQLite database using SQLAlchemy
* Use transaction-safe connection

---

## 📊 Sample Output

| id | title | price | discount_price | category | rating | stock |
| -- | ----- | ----- | -------------- | -------- | ------ | ----- |
| 1  | Phone | 500   | 450            | tech     | 4.5    | 10    |

---

## ⚙️ Tech Stack

* Python
* Pandas
* Requests
* SQLAlchemy
* SQLite

---

## 📂 Project Structure

```
src/            → pipeline logic
data/           → database file (ignored)
logs/           → log files (ignored)
```

---

## 🔥 Key Features

* Modular ETL pipeline (Extract, Transform, Load)
* Logging for monitoring execution
* Exception handling for robustness
* Handles nested JSON data
* Business logic (discount price calculation)
* Data filtering and sorting

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/pipeline.py
```

---

## 🚀 Future Improvements

* Add scheduling (cron / Airflow)
* Implement retry mechanism
* Add data validation layer
* Use cloud database (AWS / GCP)

---

## 👤 Author

Akash
