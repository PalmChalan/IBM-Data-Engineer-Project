from etl import extract, load_to_csv, load_to_db, transform
import sqlite3
from utils import log_progress, run_query

def main():
    url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
    log_progress("Preliminaries complete. Initiating ETL process")
    df = extract(url)
    transform(df, "exchange_rate.csv")
    load_to_csv(df, "out.csv")
    log_progress("SQL Connection initiated")
    conn = sqlite3.connect('Banks.db')
    load_to_db(df, conn, 'Largest_banks')
    run_query("SELECT * FROM Largest_banks", conn)
    print("-"*50)
    run_query("SELECT AVG(MC_GBP_Billion) FROM Largest_banks", conn)
    print("-"*50)
    run_query("SELECT Name from Largest_banks LIMIT 5", conn)
    print("-"*50)
    conn.close()
    log_progress("Server Connection closed")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_progress(f"Data extraction failed - {e}")
        raise