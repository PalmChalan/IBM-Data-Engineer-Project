from bs4 import BeautifulSoup
import pandas as pd
import requests
from utils import log_progress

def extract(url, table_attribs=None):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    try:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'lxml')

        heading = soup.find('span', string='By market capitalization')
        table = heading.find_parent('h2').find_next_sibling('table')
        rows = table.find_all('tr')
        data = []
        for row in rows[1:]:  # Skip header row
            cols = row.find_all('td')
            if cols:
                row_data = [col.text.strip() for col in cols]
                data.append(row_data)

        # Define column names based on table header
        header_cols = [col.text.strip() for col in rows[0].find_all('th')]
        df = pd.DataFrame(data, columns=header_cols)

        df.rename(columns={'Bank name': 'Name'}, inplace=True)
        if 'Market cap(US$ billion)' in df.columns:
            df['Market cap(US$ billion)'] = df['Market cap(US$ billion)'].str[:-1]  # remove last char
            df['Market cap(US$ billion)'] = df['Market cap(US$ billion)'].astype(float)
            # Rename column
            df.rename(columns={'Market cap(US$ billion)': 'MC_USD_Billion'}, inplace=True)
        log_progress("Data extraction complete. Initiating Transformation process")
    except Exception as e:
        log_progress(f"Data extraction failed - {e}")
        raise e
    return df