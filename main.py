import sqlite3

# Conexão com banco de dados
conn = sqlite3.connect('alunos_phyton.db')

# Criar uma tabela
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT, nota REAL)')

# Inserir dados na tabela = CREATE
cursor.execute('INSERT INTO alunos (nome, nota) VALUES ("Leandro", 8.5)')
cursor.execute('INSERT INTO alunos (nome, nota) VALUES ("Laise", 7.5)')
cursor.execute('INSERT INTO alunos (nome, nota) VALUES ("Michele", 9.5)')
cursor.execute('INSERT INTO alunos (nome, nota) VALUES ("Marcelo", 8.5)')

# Visualizar os dados da tabela = READ
cursor.execute('SELECT * FROM alunos WHERE id = 3')
alunos = cursor.fetchall()
print(alunos)

# Atualizar dados na tabela = UPDATE
cursor.execute('UPDATE alunos SET nota = 9.5 WHERE id = 1')

cursor.execute('SELECT * FROM alunos WHERE id = 1')
alunos = cursor.fetchall()
print(alunos)

# Deletar dados da tabela = DELETE
cursor.execute('DELETE FROM alunos WHERE id = 1')

cursor.execute('SELECT * FROM alunos')
alunos = cursor.fetchall()
print(alunos)  

# Fim do código.
exit