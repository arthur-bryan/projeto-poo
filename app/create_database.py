import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


cursor.execute("""create table RESERVAS(
				  	id INTEGER PRIMARY KEY AUTOINCREMENT,
				  	dono varchar(45) not null,
					sala int not null,
					data char(10) not null,
					horario char(5) not null);""")



