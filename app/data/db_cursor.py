import sqlite3
from playground import data

DATA_BASE = 'database.db'

con = sqlite3.connect(DATA_BASE)
cursor = con.cursor()

for city in data:
    cursor.execute(f'INSERT INTO TABLE city(, name TEXT, federative_unit TEXT, motto TEXT, zip_range TEXT, '
                   'anthem TEXT, flag TEXT, blazon TEXT, total_area INT)')


cursor.close()
