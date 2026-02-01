# 🏦 Global Banks ETL Pipeline
A data engineering pipeline that automates the extraction of global banking market capitalization data, transforms currency values, and loads the processed data into a local Data Warehouse.

Completed as part of the **IBM Data Engineering Professional Certificate**.


## 📋 Project Overview
This project implements a modular **ETL (Extract, Transform, Load)** process:

1. **Extract**: Scrapes raw HTML data from Wikipedia ("List of largest banks") using `BeautifulSoup`.

2. **Transform**: Cleans the data and converts Market Capitalization from USD to GBP, EUR, and INR using exchange rates via `Pandas`.

3. **Load**: Saves the processed data into two targets:
    - **CSV File**: For quick auditing and local analysis.
    - **SQLite Database**: Simulating a persistent Data Warehouse layer.

**Logging**: Tracks every stage of the pipeline execution in `project/log/code_log.txt`.

## 🛠️ Tech Stack
- Language: Python
- Libraries: `pandas`, `numpy`, `requests`, `beautifulsoup4`, `sqlite3`
- Architecture: Modular ETL design

## 📂 Project Structure
The code is organized into logical modules for maintainability:

    ├── etl/                    # Core ETL logic
    │   ├── __init__.py
    │   ├── extract.py          # Web scraping functions
    │   ├── transform.py        # Data cleaning & currency conversion
    │   └── load/               # Loading modules
    │       ├── load_to_csv.py
    │       └── load_to_db.py
    ├── data/                   # Output csv (auto-generated)
    ├── logs/                   # Execution logs (auto-generated)
    ├── utils/
    │   └── __init__.py         
    │   └── log.py              # Logging function
    │   └── run_query.py        # Querying function
    ├── exchange_rate.csv       # Currency rate (used for conversion)
    ├── main.py                 # Entry point (Orchestrator)
    ├── requirements.txt        # Project dependencies
    └── README.md               # Documentation

## 🚀 Setup & Installation
**1. Clone the repository**
```
git clone https://github.com/PalmChalan/IBM-Data-Engineer-Project.git
```
**2. Create a Virtual Environment**: It is recommended to use a virtual environment to avoid conflicts.
```
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```
**3. Install Dependencies**
```
pip install -r requirements.txt
```

## ⚙️ Usage
To run the entire pipeline, execute the main script from the root directory:
```
python main.py
```

**Expected Output:**

1. A new file `out.csv` will be created inside data folder.
2. A SQLite database `Banks.db` will be updated.
3. Progress will be logged to `/log/code_log.txt`.

## 📝 Logging
The pipeline implements an auditing mechanism. Example log output:

```
2026-02-01 14:30:00 : Preliminaries complete. Initiating ETL process.
2026-02-01 14:30:05 : Data extraction complete. Initiating Transformation process.
2026-02-01 14:30:08 : Data transformation complete. Initiating Loading process.
2026-02-01 14:30:10 : Process Complete.
```

## 👤 Author
### [Chalantorn Chuamkaew](https://www.linkedin.com/in/palmchalan/)