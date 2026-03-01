import flet as ft

from slider import gap_slider, time_change, number_pause
from read_dataframe import df_fill, new_dataframe


def menu_content(page: ft.Page):

    def new_page(e):
        df_fill(pass_box.value)
        page.go('/period')

    pass_box = ft.Checkbox(label="Пропустить перерывы", fill_color=ft.colors.GREEN_600, disabled=False)
    new_dataframe()

    return ft.Column(
        [
            ft.Text(
                "Выберите время для продуктивной работы",
                size=18, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,
            ),
            time_change,
            gap_slider(),
            number_pause,
            pass_box,
            ft.ElevatedButton(text='Начать', on_click=new_page),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )


def menu_page(page: ft.Page):
    return ft.Container(
        content=menu_content(page),
        alignment=ft.alignment.center,
        width=350,
        height=350,
        bgcolor=ft.colors.WHITE,
        padding=5,
        border=ft.border.all(1, ft.colors.GREEN_400),
        border_radius=10
    )