import pandas as pd

def read_dataframe():
    return pd.read_csv("assets/data/DataFrame.csv", delimiter=',', index_col='Unnamed: 0')

def read_time_table():
    return pd.read_csv("assets/data/Time_table.csv", delimiter=';')

def to_csv(df):
    return df.to_csv("assets/data/DataFrame.csv")

def new_dataframe():
    Dataframe = read_dataframe()
    Dataframe.loc[0, 'Number_pause'] = 1
    Dataframe.loc[0, 'Time_period'] = 30
    to_csv(Dataframe)

def take_value(name):
    return read_dataframe().loc[0, name]

def num_pause(time_value):
    df = read_time_table()
    i = df.index[df.Total_time == int(time_value)]
    return df.loc[i[0], 'Number_pause']

def fill_value(type_value, value):
    df = read_dataframe()
    df.loc[0, type_value] = value
    to_csv(df)

def df_fill(box_value):
    Dataframe = read_dataframe()
    TimeTable = read_time_table()
    i = TimeTable.index[TimeTable.Total_time == Dataframe.loc[0, 'Total_time']]
    if box_value or (TimeTable.loc[i[0], 'Number_pause'] == 0):
        Dataframe.loc[0, 'Number_pause'] = 0
        Dataframe.loc[0, 'Time_period'] = Dataframe.loc[0, 'Total_time']
    else:
        Dataframe.loc[0, 'Number_pause'] = TimeTable.loc[i[0], 'Number_pause']
        Dataframe.loc[0, 'Time_period'] = TimeTable.loc[i[0], 'Time_period']
    Dataframe.loc[0, 'Count_period_times'] = 0
    Dataframe.loc[0, 'Mushrooms'] = 0
    to_csv(Dataframe)

def update_count(value):
    df = read_dataframe()
    df.loc[0, value] += 1
    to_csv(df)

def compare_values():
    if read_dataframe().loc[0, 'Count_period_times'] == (read_dataframe().loc[0, 'Number_pause'] + 1):
        return True
    else:
        return False