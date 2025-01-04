Biggest Single Count
-----------------------

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
   largest_unique_value = my_numbers.drop_duplicates(['num'], keep=False).max().to_frame(name ='num')
   # max(my_numbers['num'].unique())
   return largest_unique_value
