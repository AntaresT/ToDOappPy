import sqlite3


#Conexão com o Banco de Dados
conn = sqlite3.connect('todolist.db')
#definindo cursor - interador que permite navegar e manipular os registros do bd.
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE todolist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        dtcriacao DATE NOT NULL,
        descricao TEXT,
        concluido INTEGER,
        dtconcluido DATE
    );
""")

print("Tabela criada com sucesso")
#desconecta do banco
conn.close()