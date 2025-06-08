"""Example reporting script.

Connects to the MySQL data warehouse and prints the latest records.
"""

import mysql.connector


def show_latest(limit: int = 10):
    conn = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="dwh",
    )
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, temperature_c FROM observations ORDER BY timestamp DESC LIMIT %s", (limit,))
    for ts, temp in cursor.fetchall():
        print(ts, temp)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    show_latest()
