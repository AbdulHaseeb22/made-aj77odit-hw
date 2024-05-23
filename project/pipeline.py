import pandas as pd
import sqlite3
import os

annual_surface_temp_url = 'https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv'
forest_and_carbon_url = 'https://opendata.arcgis.com/datasets/66dad9817da847b385d3b2323ce1be57_0.csv'

data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
os.makedirs(data_dir, exist_ok=True)

def download_and_read_csv(url, filename):
    print(f"Downloading {url}")
    df = pd.read_csv(url)
    file_path = os.path.join(data_dir, filename)
    df.to_csv(file_path, index=False)
    print(f"Saved {filename} to {file_path}")
    return df

annual_surface_temp = download_and_read_csv(annual_surface_temp_url, 'Annual_Surface_Temperature_Change.csv')
forest_and_carbon = download_and_read_csv(forest_and_carbon_url, 'Forest_and_Carbon.csv')

years_temp = [f'F{year}' for year in range(1992, 2021)]
years_carbon = [f'F{year}' for year in range(1992, 2021)]

temp_change = annual_surface_temp[annual_surface_temp['Indicator'] == 'Temperature change with respect to a baseline climatology, corresponding to the period 1951-1980'].loc[:, ['Country'] + years_temp]
carbon_stocks = forest_and_carbon[forest_and_carbon['Indicator'] == 'Carbon stocks in forests'].loc[:, ['Country'] + years_carbon]

temp_change_filtered = temp_change.dropna().copy()
carbon_stocks_filtered = carbon_stocks.dropna().copy()


temp_change_filtered.loc[:, years_temp] = temp_change_filtered.loc[:, years_temp].apply(pd.to_numeric)
carbon_stocks_filtered.loc[:, years_carbon] = carbon_stocks_filtered.loc[:, years_carbon].apply(pd.to_numeric)


temp_change_filtered.set_index('Country', inplace=True)
carbon_stocks_filtered.set_index('Country', inplace=True)

temp_change_diff_corrected = temp_change_filtered.diff(axis=1).dropna(axis=1)
carbon_stocks_diff_corrected = carbon_stocks_filtered.diff(axis=1).dropna(axis=1)

conn = sqlite3.connect(os.path.join(data_dir, 'climate_data.db'))
print(f"Saving SQLite database to {os.path.join(data_dir, 'climate_data.db')}")

temp_change.to_sql('Annual_Surface_Temperature_Change', conn, if_exists='replace', index=False)
carbon_stocks.to_sql('Forest_and_Carbon', conn, if_exists='replace', index=False)
temp_change_diff_corrected.to_sql('Temp_Change_Diff', conn, if_exists='replace')
carbon_stocks_diff_corrected.to_sql('Carbon_Stocks_Diff', conn, if_exists='replace')

conn.close()
print("Pipeline completed successfully.")
