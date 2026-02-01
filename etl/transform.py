import numpy as np
from utils import log_progress

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    curr = dict()
    try:
        with open(csv_path, "r") as exchange:
            for line in exchange:
                ex = line.strip().split(",")
                curr[ex[0]] = ex[1]
        df['MC_GBP_Billion'] = [np.round(x*float(curr['GBP']),2) for x in df['MC_USD_Billion']]
        df['MC_EUR_Billion'] = [np.round(x*float(curr['EUR']),2) for x in df['MC_USD_Billion']]
        df['MC_INR_Billion'] = [np.round(x*float(curr['INR']),2) for x in df['MC_USD_Billion']]
        log_progress("Data transformation complete. Initiating Loading process")
    except Exception as e:
        log_progress(f"Data transformation failed - {e}")
        raise e
    return df