from datetime import datetime
import os

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    current_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(current_dir, '..', 'log', 'code_log.txt')
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file_path, "a") as log:
        log.write(f"{time} : {message}\n")