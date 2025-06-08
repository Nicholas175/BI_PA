"""Simple ETL example.

This script demonstrates loading raw CSV data, converting Fahrenheit to Celsius,
and inserting the results into a MySQL table.
"""

import csv
from pathlib import Path

import mysql.connector

RAW_FILE = Path(__file__).resolve().parents[1] / "rawdata" / "sample_data.csv"

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5.0 / 9.0

def run_etl():
    conn = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="dwh",
    )
    cursor = conn.cursor()

    with RAW_FILE.open() as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            temp_c = fahrenheit_to_celsius(float(row["temperature_f"]))
            cursor.execute(
                "INSERT INTO observations (timestamp, temperature_c) VALUES (%s, %s)",
                (row["timestamp"], temp_c),
            )
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    run_etl()
