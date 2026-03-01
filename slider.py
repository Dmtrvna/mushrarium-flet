import flet as ft

from read_dataframe import num_pause, fill_value

time_change = ft.Text(value='30 минут', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)
number_pause = ft.Text(value='Количество перерывов: 1', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)

def change_value(e):
    if time_change.page is not None:  # Проверяем, добавлен ли элемент на страницу
        time_change.value = f'{int(e.control.value)} минут'
        fill_value('Total_time', int(e.control.value))
        time_change.update()
        number_pause.value = f'Количество перерывов: {num_pause(e.control.value)}'
        number_pause.update()

def gap_slider():
    return ft.Slider(
        min=10,
        max=240,
        divisions=46,
        value=30,
        label="{value}",
        active_color=ft.colors.GREEN_400,
        inactive_color=ft.colors.GREEN_200,
        thumb_color=ft.colors.GREEN_400,
        width=290,
        on_change_end=change_value
    )

def add_controls_to_page(page):
    # Добавляем элементы управления на страницу
    page.controls.append(time_change)
    page.controls.append(gap_slider())
    page.update()
