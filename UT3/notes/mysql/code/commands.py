from mysql import DB

db = DB('aragorn', 'arazorn', 'commands')

cmd = input('Introduzca el comando: ')
desc = input('Introduzca la descripción: ')

sql = f"insert into commands values ('{cmd}', '{desc}')"
db.run(sql)

sql = 'select * from commands order by name'
print(db.run(sql))
