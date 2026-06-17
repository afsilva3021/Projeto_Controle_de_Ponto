import flet as ft
import asyncio
from datetime import datetime

from app.services.pontoService import PontoSerivce

async def homeView(page: ft.Page):
    Ponto_serivce = PontoSerivce()

    horaAtual = ft.Text(
        value = datetime.now().strftime("%H:%M:%S"),
        size = 30,
        weight = ft.FontWeight.BOLD
    )

    status = ft.Text("Nenhum ponto registrado")

    async def atualizarRelogio():
        while True:
            horaAtual.value = datetime.now().strftime("%H:%M:%S")
            horaAtual.update()
            await asyncio.sleep(1)

    def marcarPonto(e):
        ponto = Ponto_serivce.registrarPronto("PONTO")

        status.value = f"Pronto registrado em: {ponto.dataHora}"
        status.update()

    page.add(
        ft.Column(
            controls = [
                ft.Text(
                    "Controle de Ponto",
                    size = 24,
                    weight = ft.FontWeight.BOLD
                ),
                horaAtual,
                ft.ElevatedButton(
                    "Marcar Ponto",
                    on_click = marcarPonto
                ),
                status,
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        )
    )

    page.run_task(atualizarRelogio)