import sqlite3
DB = 'sekmes.db'
#savienojuma izveide ar db
conn =sqlite3.connect(DB)
#kursora izveide (gruzchiks)
cursor = conn.cursor()
#pieprasījums, kas veido tabulu DB
cursor.execute('''
    CREATE TABLE IF NOT EXISTS atzimes (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
               vards TEXT NOT NULL,
               uzvards TEXT NOT NULL,
               atzime INTEGER NOT NULL
               )
''')
#saglabā izmaiņas
conn.commit()
conn.close()
print('Tabula Atzīme izveidota')