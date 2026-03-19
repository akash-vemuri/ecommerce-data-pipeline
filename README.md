# 📊 E-commerce Data Pipeline (ETL)

## 🚀 Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python. It fetches product data from an external API, performs data transformations, and loads the processed data into a SQLite database.

---

## 🧩 Pipeline Flow

1. **Extract**

   * Fetch data from API using `requests`

2. **Transform**

   * Convert JSON to Pandas DataFrame
   * Handle nested JSON structure
   * Create new feature: `discount_price`
   * Filter out out-of-stock products
   * Sort by product rating

3. **Load**

   * Store processed data into SQLite database using SQLAlchemy

---

## ⚙️ Technologies Used

* Python
* Pandas
* Requests
* SQLAlchemy
* SQLite

---

## 📂 Project Structure

```
src/            → pipeline code
data/           → database file
logs/           → log files
```

---

## 🔥 Key Features

* Modular pipeline design (Extract, Transform, Load)
* Logging for monitoring pipeline execution
* Exception handling for robustness
* Handles nested JSON data
* Business logic implementation (discount calculation)

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/pipeline.py
```

---

## 💡 Future Improvements

* Add scheduling (cron/Airflow)
* Implement retry mechanism
* Add data validation layer
* Store data in cloud database

---

## 📌 Author

Akash Vemuri
