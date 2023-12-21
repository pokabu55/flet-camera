import flet as ft


def main(page: ft.Page):
    pass


# デスクトップアプリの場合
# ft.app(target=main)

# Webアプリの場合
ft.app(target=main, view=ft.WEB_BROWSER)
