import sqlite3
from json import load

DATA_BASE = 'database.db'

con = sqlite3.connect(DATA_BASE)
cursor = con.cursor()

with open('cities_data.json') as file:
    data = load(file)
    for k, v in data[0].items():
        for item in v:
            query = f'INSERT INTO city VALUES({int(item["ibge"])}, "{item["name"]}", "{k}", "", "", "", "", "", 0)'
            cursor.execute(query)
    con.commit()
    con.close()
