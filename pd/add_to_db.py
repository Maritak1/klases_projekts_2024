import sqlite3
DB = 'sekmes.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
dati = []
for i in range(7):
    print(f'\nIevadi {i+1}. ierakstu:')
    vards = input('Vārds: ')
    uzvards = input('Uzvārds: ')
    atzime = int(input('Atzīme: '))
    dati.append((vards, uzvards, atzime))
cursor.executemany('''
    INSERT INTO atzimes (vards, uzvards, atzime)
    VALUES (?, ?, ?)               
''', dati)
conn.commit()
conn.close()
print('Tika pievienoti 7 ieraksti.')