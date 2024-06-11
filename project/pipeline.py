import pandas as pd
import sqlite3
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

annual_surface_temp_url = 'https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv'
forest_and_carbon_url = 'https://opendata.arcgis.com/datasets/66dad9817da847b385d3b2323ce1be57_0.csv'

data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
os.makedirs(data_dir, exist_ok=True)

def download_and_read_csv(url, filename, directory=data_dir):
    try:
        logging.info(f"Downloading {url}")
        df = pd.read_csv(url)
        file_path = os.path.join(directory, filename)
        df.to_csv(file_path, index=False)
        logging.info(f"Saved {filename} to {file_path}")
        return df
    except Exception as e:
        logging.error(f"Failed to download or save {filename}: {e}")
        raise

def filter_and_transform_data(df, indicator, years):
    try:
        filtered_df = df[df['Indicator'] == indicator].loc[:, ['Country'] + years]
        filtered_df = filtered_df.dropna().copy()
        filtered_df.loc[:, years] = filtered_df.loc[:, years].apply(pd.to_numeric)
        filtered_df.set_index('Country', inplace=True)
        return filtered_df
    except Exception as e:
        logging.error(f"Error in filtering and transforming data: {e}")
        raise

def calculate_diff(df):
    try:
        diff_df = df.diff(axis=1).dropna(axis=1)
        return diff_df
    except Exception as e:
        logging.error(f"Error in calculating differences: {e}")
        raise

def save_to_sqlite(df_dict, db_path):
    try:
        conn = sqlite3.connect(db_path)
        logging.info(f"Saving SQLite database to {db_path}")
        for table_name, df in df_dict.items():
            df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
    except Exception as e:
        logging.error(f"Error saving to SQLite database: {e}")
        raise

def process_data():
    try:
        annual_surface_temp = download_and_read_csv(annual_surface_temp_url, 'Annual_Surface_Temperature_Change.csv')
        forest_and_carbon = download_and_read_csv(forest_and_carbon_url, 'Forest_and_Carbon.csv')

        years = [f'F{year}' for year in range(1992, 2021)]

        temp_change = filter_and_transform_data(
            annual_surface_temp,
            'Temperature change with respect to a baseline climatology, corresponding to the period 1951-1980',
            years
        )
        
        carbon_stocks = filter_and_transform_data(
            forest_and_carbon,
            'Carbon stocks in forests',
            years
        )

        temp_change_diff_corrected = calculate_diff(temp_change)
        carbon_stocks_diff_corrected = calculate_diff(carbon_stocks)

        save_to_sqlite({
            'Annual_Surface_Temperature_Change': temp_change,
            'Forest_and_Carbon': carbon_stocks,
            'Temp_Change_Diff': temp_change_diff_corrected,
            'Carbon_Stocks_Diff': carbon_stocks_diff_corrected
        }, os.path.join(data_dir, 'climate_data.db'))

        logging.info("Pipeline completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during data processing: {e}")
        raise

if __name__ == "__main__":
    process_data()
