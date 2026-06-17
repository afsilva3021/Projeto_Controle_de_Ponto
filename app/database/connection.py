import sqlite3

DB_NAME = "ponto.db"


def conectar():
    return sqlite3.connect(DB_NAME)


def criarTable():
    conexao = conectar()
    curso = conexao.cursor()

    curso.execute("""
        CREATE TABLE IF NOT EXISTS pontos (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  tipo TEXT NOT NULL,
                  data_hora TEXT NOT NULL,
                  latitude REAL,
                  logitude REAL,
                  sincronizado INTEGER DEFAULT 0
                  );
    """)

    conexao.commit()
    conexao.close()