import flet as ft


from app.views.homeView import homeView
from app.database.connection import criarTable

async def main(page: ft.Page):
    page.title = "Controle de Ponto"

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    criarTable()

    await homeView(page)

ft.app(target=main)