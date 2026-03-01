import flet as ft
from flet_timer.flet_timer import Timer
from functools import partial

from read_dataframe import take_value, compare_values, update_count, fill_value
from mushrooms import up_time

timer_time = int(take_value('Time_period'))
period_text_time = ft.Text(value=f"{(timer_time//60):02}:{(timer_time%60):02}:00", color=ft.colors.BLACK, size=30)
pause_text_time = ft.Text(value="00:05:00", color=ft.colors.BLACK, size=30)
mush_image = ft.Image('files/myhomor/stage_1.png', width=300, height=300, visible=True)

def period_timer(mush, page):
    fill_value('Mushrooms', 0)
    seconds = ft.Text(value=str(5)) #
    count = ft.Text(value=str(0))

    def update_image():
        update_count('Mushrooms')
        mush_image.src = mush[int(take_value('Mushrooms'))]
        mush_image.update()

    def timer_over(page):
        if compare_values():
            Timer(name="timer", interval_s=1, callback=page.go('/end_page')).start()
        else:
            Timer(name="timer", interval_s=1, callback=page.go('/trans_page_1')).start()

    def timer(page):
        if (int(count.value) % up_time() == 0) and (take_value('Mushrooms') < 6):
            update_image()
        if int(seconds.value) == 0:
            timer_over(page)
        seconds.value = f"{int(seconds.value) - 1}"
        count.value = f"{int(count.value) - 1}"
        period_text_time.value = f"{(int(seconds.value) // 3600):02}:{(int(seconds.value) // 60 % 60):02}:{(int(seconds.value) % 60):02}"
        period_text_time.update()

    return Timer(name='period_timer', interval_s=1, callback=partial(timer, page))


def pause_timer(page):

    seconds = ft.Text(value=str(5)) #5*60

    def timer_over(page):
        print("time over")
        Timer(name="timer", interval_s=1, callback=page.go('/trans_page_2')).start()

    def timer(page):
        if int(seconds.value) == 0:
            timer_over(page)
        seconds.value = f"{int(seconds.value) - 1}"
        pause_text_time.value = f"{(int(seconds.value) // 3600):02}:{(int(seconds.value) // 60 % 60):02}:{(int(seconds.value) % 60):02}"
        pause_text_time.update()

    return Timer(name='pause_timer', interval_s=1, callback=partial(timer, page))


