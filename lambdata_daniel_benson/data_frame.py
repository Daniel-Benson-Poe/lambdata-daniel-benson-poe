import pandas as pd
import numpy as np
from lambdata_daniel_benson.null_checker import null_checker
from lambdata_daniel_benson.df_column_adder import adder

df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [5, 6, 7, np.nan]})

null_checker(df)

list = [3, 7, 1]
adder(list, 'c', df)
print(df)

