from utils import log_progress

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    try:
        cursor = sql_connection.cursor()
        cursor.execute(query_statement)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        log_progress("Process Complete")
    except Exception as e:
        log_progress(f"Failed - {e}")
        raise e    
    cursor.close()