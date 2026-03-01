import flet as ft

from timer import pause_text_time

def pause_content(page: ft.Page):

    return ft.Column(
        [
            ft.Text('Перерыв', size=20, weight=ft.FontWeight.BOLD),
            pause_text_time,
            ft.Image(src='assets/images/Sleep_homak.png', width=250, height=250),
            ft.Row(
                [
                    ft.ElevatedButton(text="Вернуться в меню", on_click=lambda e: page.go("/")),
                    ft.ElevatedButton(text="Пропустить отдых", on_click=lambda e: page.go("/period"))
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

def pause_page(page: ft.Page):
    return ft.Container(
        content=pause_content(page),
        alignment=ft.alignment.center,
        width=450,
        height=450,
        bgcolor=ft.colors.WHITE,  # если убрать, не будет фона
        border=ft.border.all(1, ft.colors.GREEN),
        border_radius=5
    )