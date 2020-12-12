"""
	ESTE ARQUIVO É UM MÓDULO PERTENCENTE AO PROJETO 'projeto-poo',
	DISPONÍVEL EM 'https://github.com/arthurbryan/projeto-poo'
"""

import sqlite3
import os

diretorio_anterior = os.path.dirname(os.getcwd())

conn = sqlite3.connect(os.path.join(diretorio_anterior, 'database', 'database.db'))
cursor = conn.cursor()

cursor.execute("""create table RESERVAS(
				  	id INTEGER PRIMARY KEY AUTOINCREMENT,
				  	dono varchar(45) not null,
					sala int not null,
					data char(10) not null,
					horario char(5) not null);""")

conn.commit()
conn.close()
