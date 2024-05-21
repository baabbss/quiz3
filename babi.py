


import json
import requests
import sqlite3

url = "https://www.dnd5eapi.co/api/spells"
r = requests.get(url)
result_json = r.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=4)
print(res_structured)
print(r.status_code)
print(r.headers)

conn = sqlite3.connect('dnd_spells.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS DnDSpells
             (id INTEGER PRIMARY KEY, name TEXT, url TEXT)''')
cursor.executemany("INSERT INTO DnDSpells (name, url) VALUES (?, ?)",
                   [(spell['name'], spell['url']) for spell in res['results']])
conn.commit()
conn.close()
for spell in res['results']:
    print(f"Spell: {spell['name']}")















