import pathlib
import sqlite3
import ray
from ray.exceptions import RayTaskError

import lightroom_2_darktable.console as console

def list_tables(lrcat: pathlib.Path) -> None:
    conn = sqlite3.connect(lrcat)
    cursor = conn.cursor()

    # Execute the query to get all table names
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    console.out.print(tables)
    conn.close()


def print_db_size(lrcat: pathlib.Path) -> None:
    
    def conn_factory():
        return sqlite3.connect(lrcat)
    
    with sqlite3.connect(lrcat) as conn:
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")  # [5][8]
        table_names = [row[0] for row in cursor.fetchall()]


    for table in table_names:
        try:
            ds = ray.data.read_sql(f"SELECT * FROM {table}", conn_factory)  # [1][3]
            row_count = ds.count()
            print(f"Table '{table}' has {row_count} rows.")
        except RayTaskError:
            print(f"Error processing: {table}")
            continue