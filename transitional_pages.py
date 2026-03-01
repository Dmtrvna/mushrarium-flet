import flet as ft


def trans_page_2(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Время отдыха истекло", size=15, weight=ft.FontWeight.BOLD),
                ft.Text("Приготовьтесь к периоду продуктивной работы",
                        size=20, weight=ft.FontWeight.BOLD),
                ft.TextButton("Приступить к работе", on_click=lambda e: page.go('/period'))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center,
        width=300,
        height=300,
        bgcolor=ft.colors.GREEN_50,
        padding=5,
        border=ft.border.all(1, ft.colors.GREEN_900),
        border_radius=10
    )


def trans_page_1(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Вы отлично справлятесь!", size=15, weight=ft.FontWeight.BOLD),
                ft.Text("Пришло время отдохнуть", size=15, weight=ft.FontWeight.BOLD),
                ft.TextButton(text="Отдых", on_click=lambda e: page.go('/pause'))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center,
        width=300,
        height=300,
        bgcolor=ft.colors.WHITE,
        padding=5,
        border=ft.border.all(1, ft.colors.GREEN_900),
        border_radius=10
    )

def end_page(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text('Время продуктивной работы завершено!', size=20, weight=ft.FontWeight.BOLD),
                ft.Image(src='assets/images/myhomor/myhomor image.png', width=150, height=150),
                ft.ElevatedButton(text="Вернуться в меню", on_click=lambda e: page.go("/"))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center,
        width=350,
        height=350,
        bgcolor=ft.colors.WHITE,
        border=ft.border.all(1, ft.colors.GREEN_900),
        border_radius=5
    )