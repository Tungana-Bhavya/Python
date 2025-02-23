Create a Dataframe from List
-----------------------

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    cols = ['student_id','age']
    res = pd.DataFrame(student_data, columns=cols)
    return res