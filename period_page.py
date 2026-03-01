import flet as ft

from timer import period_text_time, mush_image
from read_dataframe import take_value, update_count

def period_content(page: ft.Page):
    update_count('Count_period_times')

    return ft.Column(
        [

            ft.Text(f'Период продуктивной работы ({take_value('Count_period_times')} из {take_value('Number_pause')+1})',
                    size=20, weight=ft.FontWeight.BOLD),
            period_text_time,
            mush_image,
            ft.Row(
                [
                    ft.ElevatedButton(text="Вернуться в меню", on_click=lambda e: page.go("/")),
                    ft.ElevatedButton(text="Пропустить период", on_click=lambda e: page.go("/pause"))
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )


def period_page(page: ft.Page):
    return ft.Container(
        content=period_content(page),
        alignment=ft.alignment.center,
        width=450,
        height=450,
        bgcolor=ft.colors.GREEN_50,
        border=ft.border.all(1, ft.colors.GREEN_900),
        border_radius=5
    )