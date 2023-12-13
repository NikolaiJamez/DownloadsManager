import flet as ft

def main(page: ft.Page) -> None:
    page.window_height = 600
    page.window_width = 1000
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

ft.app(target = main)