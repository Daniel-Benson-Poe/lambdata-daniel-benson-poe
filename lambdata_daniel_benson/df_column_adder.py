import pandas as pd 

def adder(list, col_name, df):
    list = pd.Series(list)
    df[col_name] = list

    return df



