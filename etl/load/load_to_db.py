from utils import log_progress

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    try:
        cursor = sql_connection.cursor()
        df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
        sql_connection.commit()
        cursor.close()
        log_progress("Data loaded to Database as a table, Executing queries")
    except Exception as e:
        log_progress(f"Data loaded to Database failed - {e}")
        raise e