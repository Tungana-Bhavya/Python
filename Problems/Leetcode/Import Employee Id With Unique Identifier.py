 Repalce Employee Id with Unique Identifier
-----------------------

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employees, employee_uni, on = 'id', how='left')
    res = merged[['unique_id','name']]
    return res