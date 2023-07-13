import sqlite3
from Creation import *

db = sqlite3.connect(':memory:')
cur = db.cursor()

if __name__ == "__main__":
    print("Begin the Aplication")
    Creation.create_and_populate(cur)
    cur.execute('''SELECT * FROM contact''')
    data = cur.fetchall()
    for e in data:
        print(e)