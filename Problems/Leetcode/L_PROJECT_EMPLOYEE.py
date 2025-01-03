Project Employee
-----------------------

import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # merged tables
    merged_table = pd.merge(project, employee, on ='employee_id', how='left')
    # applied groupby function on project id
    # calculated mean of experience years
    # round mean to two digits
    # renamed existing column: experience years to average years 
    res = merged_table.groupby('project_id')['experience_years'].mean().round(2).rename('average_years').reset_index()
    # return result dataframe
    return res