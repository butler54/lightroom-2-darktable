import pathlib
import sqlite3


import lightroom_2_darktable.console as console

def list_tables(lrcat: pathlib.Path) -> None:
    conn = sqlite3.connect(lrcat)
    cursor = conn.cursor()

    # Execute the query to get all table names
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    console.out.print(tables)
    conn.close()