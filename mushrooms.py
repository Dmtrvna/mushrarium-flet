import random
from read_dataframe import take_value


def up_time():
    return take_value('Time_period')//6


def random_choise():
    return random.choice([myhomor, lisichka])


myhomor = ['files/myhomor/stage_1.png', 'files/myhomor/stage_2.png', 'files/myhomor/stage_3.png',
           'files/myhomor/stage_4.png', 'files/myhomor/stage_5.png', 'files/myhomor/stage_6.png']

lisichka = ['files/lisichka/stage_1.png', 'files/lisichka/stage_2.png', 'files/lisichka/stage_3.png',
           'files/lisichka/stage_4.png', 'files/lisichka/stage_5.png', 'files/lisichka/stage_6.png']
