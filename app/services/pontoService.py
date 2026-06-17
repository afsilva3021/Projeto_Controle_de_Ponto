from datetime import datetime

from app.database.connection import conectar
from app.models.Ponto import Ponto

class PontoSerivce:
    
    def registrarPronto(self, tipo: str) -> Ponto:
        agora = datetime.now().strftime("%d/%m/%y %H:%M:%S")

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO pontos (tipo, data_hora)
            VALUES (?, ?)
        """, (tipo, agora))

        conexao.commit()
        conexao.close()

        return Ponto(tipo, agora)