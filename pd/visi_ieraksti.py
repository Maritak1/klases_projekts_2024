import sqlite3
DB = 'sekme.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('''
    SELECT id, vards, uzvards, atzime FROM atzimes
    ORDER BY atzime DESC
''')
ieraksti = cursor.fetchall()
conn.close()
if ieraksti:
    print('DB visi ieraksti:')
    for id_, vards, uzvards, atzime in ieraksti:
        print(f'{id_}   {vards} {uzvards} - {atzime}')
else:
    print('Nav rezultātu.')