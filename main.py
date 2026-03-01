import flet as ft

from timer import period_timer, pause_timer
from slider import add_controls_to_page
from mushrooms import random_choise

from menu_page import menu_page
from period_page import period_page
from pause_page import pause_page
from transitional_pages import trans_page_1, trans_page_2, end_page


def main(page: ft.Page) -> None:
    page.title = "Mushrarium"
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = ft.Theme(color_scheme_seed=ft.colors.GREEN_900)

    audio = ft.Audio(src="assets/audio/natural.mp3", autoplay=True, volume=100)

    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()

        """Главное меню"""
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    menu_page(page)
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        """Период"""
        if page.route == "/period":
            page.views.append(
                ft.View(
                    route="/period",
                    controls=[
                        period_timer(random_choise(), page),
                        period_page(page)
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        """Пауза"""
        if page.route == "/pause":
            page.views.append(
                ft.View(
                    route="/pause",
                    controls=[
                        pause_timer(page),
                        pause_page(page)
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        """Переходная страница 1"""
        if page.route == "/trans_page_1":
            page.views.append(
                ft.View(
                    route="/trans_page_1",
                    controls=[
                        audio,
                        trans_page_1(page)
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        """Переходная страница 2"""
        if page.route == "/trans_page_2":
            page.views.append(
                ft.View(
                    route="/trans_page_2",
                    controls=[
                        audio,
                        trans_page_2(page)
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        """Конечная страница"""
        if page.route == "/end_page":
            page.views.append(
                ft.View(
                    route="/end_page",
                    controls=[
                        audio,
                        end_page(page)
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        # Добавляем элементы управления слайдера на страницу после настройки маршрутов
        add_controls_to_page(page)

        page.update()

    def view_pop(page: ft.Page, e: ft.ViewPopEvent) -> None:
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)
