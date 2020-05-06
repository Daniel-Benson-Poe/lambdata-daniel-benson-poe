import pandas

def null_checker(df):
    num_nulls = df.isnull().sum().sum()

    print("There are", num_nulls, "null values in this dataframe.")

    