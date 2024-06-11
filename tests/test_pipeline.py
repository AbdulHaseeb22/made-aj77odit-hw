import pytest
import pandas as pd
import os
import sqlite3
from project.pipeline import download_and_read_csv, filter_and_transform_data, calculate_diff, save_to_sqlite

ANNUAL_SURFACE_TEMP_URL = 'https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv'
FOREST_AND_CARBON_URL = 'https://opendata.arcgis.com/datasets/66dad9817da847b385d3b2323ce1be57_0.csv'
ANNUAL_SURFACE_TEMP_FILENAME = 'test_Annual_Surface_Temperature_Change.csv'
FOREST_AND_CARBON_FILENAME = 'test_Forest_and_Carbon.csv'
TEST_DATA_DIR = '../tests/test_data'
os.makedirs(TEST_DATA_DIR, exist_ok=True)

def test_download_and_read_csv():
    df_annual_temp = download_and_read_csv(ANNUAL_SURFACE_TEMP_URL, ANNUAL_SURFACE_TEMP_FILENAME, TEST_DATA_DIR)
    assert not df_annual_temp.empty
    assert 'Country' in df_annual_temp.columns
    file_path_annual_temp = os.path.join(TEST_DATA_DIR, ANNUAL_SURFACE_TEMP_FILENAME)
    assert os.path.exists(file_path_annual_temp)
    
    df_forest_carbon = download_and_read_csv(FOREST_AND_CARBON_URL, FOREST_AND_CARBON_FILENAME, TEST_DATA_DIR)
    assert not df_forest_carbon.empty
    assert 'Country' in df_forest_carbon.columns
    file_path_forest_carbon = os.path.join(TEST_DATA_DIR, FOREST_AND_CARBON_FILENAME)
    assert os.path.exists(file_path_forest_carbon)

def test_filter_and_transform_data():
    data = {
        'Indicator': ['Temperature change with respect to a baseline climatology, corresponding to the period 1951-1980'] * 2,
        'Country': ['Country1', 'Country2'],
        'F1992': [1.1, 2.2],
        'F1993': [1.2, 2.3]
    }
    df = pd.DataFrame(data)
    years = ['F1992', 'F1993']
    filtered_df = filter_and_transform_data(df, data['Indicator'][0], years)
    assert not filtered_df.empty
    assert 'F1992' in filtered_df.columns

def test_calculate_diff():
    data = {
        'Country': ['Country1', 'Country2'],
        'F1992': [1.1, 2.2],
        'F1993': [1.2, 2.3]
    }
    df = pd.DataFrame(data).set_index('Country')
    diff_df = calculate_diff(df)
    assert not diff_df.empty
    assert 'F1993' in diff_df.columns

def test_save_to_sqlite():
    data = {
        'Country': ['Country1', 'Country2'],
        'F1992': [1.1, 2.2],
        'F1993': [1.2, 2.3]
    }
    df = pd.DataFrame(data)
    db_path = os.path.join(TEST_DATA_DIR, 'test.db')
    save_to_sqlite({'TestTable': df}, db_path)
    conn = sqlite3.connect(db_path)
    saved_df = pd.read_sql('SELECT * FROM TestTable', conn)
    conn.close()
    assert not saved_df.empty
    assert 'F1992' in saved_df.columns
