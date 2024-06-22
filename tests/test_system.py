import os
import subprocess
import sqlite3

def test_data_pipeline():
    script_dir = os.path.dirname(__file__)
    project_dir = os.path.abspath(os.path.join(script_dir, '..', 'project'))
    script_path = os.path.join(project_dir, 'pipeline.py')
    data_dir = os.path.abspath(os.path.join(script_dir, '..', 'data'))
    db_path = os.path.join(data_dir, 'climate_data.db')

    print(f"Script directory: {script_dir}")
    print(f"Project directory: {project_dir}")
    print(f"Script path: {script_path}")
    print(f"Data directory: {data_dir}")
    print(f"Database path: {db_path}")

    subprocess.run(["python", script_path], check=True)

    db_path = os.path.join('..', 'data', 'climate_data.db')
    assert os.path.exists(db_path), f"Database file does not exist at {db_path}"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()

    expected_tables = {'Annual_Surface_Temperature_Change', 'Forest_and_Carbon', 'Temp_Change_Diff', 'Carbon_Stocks_Diff'}
    retrieved_tables = set(table[0] for table in tables)
    print(f"Expected tables: {expected_tables}")
    print(f"Retrieved tables: {retrieved_tables}")

    assert expected_tables.issubset(retrieved_tables), f"Missing tables: {expected_tables - retrieved_tables}"

if __name__ == "__main__":
    test_data_pipeline()
