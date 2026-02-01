import os
from utils import log_progress

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    current_dir = os.path.dirname(os.path.abspath(__file__))
    out_file_path = os.path.join(current_dir, '..', '..', 'data', output_path)
    os.makedirs(os.path.dirname(out_file_path), exist_ok=True)
    try:
        df.to_csv(out_file_path)
        log_progress("Data saved to CSV file")
    except Exception as e:
        log_progress(f"Saving to CSV failed - {e}")
        raise e