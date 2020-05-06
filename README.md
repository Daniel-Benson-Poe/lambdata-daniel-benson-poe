# lambdata-daniel-benson-poe

## Installation

Fork this repo, then download your own copy of it. Then navigate into this direcctory from the command line.

Then activate the virtual environment:

```sh
pip install -i https://test.pypi.org/simple/ lambdata-poe
pip install -i https://test.pypi.org/simple/ lambdata-daniel-benson
```

## Usage
```
py
from lambdata_poe.my_mod import enlarge
from lambdata_daniel_benson.null_checker import null_checker
from lambdata_daniel_benson.df_column_adder import adder

print(enlarge(9))
print(null_checker(df))
print(adder(list, col_name, df))
```