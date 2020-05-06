import pandas as pd
import numpy as np
from lambdata_daniel_benson.null_checker import null_checker

df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [5, 6, 7, np.nan]})

null_checker(df)