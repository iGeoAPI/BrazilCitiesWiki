import os
import sqlite3
from json import load
from sqlite3 import IntegrityError

try:
    os.remove('database.db')
except FileNotFoundError:
    pass

DATA_BASE = 'database.db'

con = sqlite3.connect(DATA_BASE)
cursor = con.cursor()

try:
    cursor.execute('CREATE TABLE city ('
                   'ibge TEXT NOT NULL,'
                   'name TEXT NOT NULL,'
                   'federative_unit TEXT NOT NULL,'
                   'flag TEXT,'
                   'blazon TEXT,'
                   'motto TEXT,'
                   'anthem TEXT,'
                   'total_area INTEGER,'
                   'zip_range TEXT,'
                   'CONSTRAINT ibge_key UNIQUE (ibge));')
except Exception as e:
    print(e)

with open('cities_data.json') as file:
    data = load(file)
    for k, v in data[0].items():
        for item in v:
            query = f'INSERT INTO city VALUES("{item["ibge"]}", "{item["name"]}", "{item["federative_unit"]}", ' \
                    f'"{item["flag"]}", "{item["blazon"]}", "{item["motto"]}", "{item["anthem"]}", ' \
                    f'"{item["total_area"]}", "{item["zip_range"]}")'

            try:
                cursor.execute(query)
            except IntegrityError as err:
                raise IntegrityError(f'{err}')
    con.commit()
    con.close()
