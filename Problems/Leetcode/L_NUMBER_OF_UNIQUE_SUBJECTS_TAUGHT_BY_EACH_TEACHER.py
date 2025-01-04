Number of Unique Subjects Taught by Each Teacher
-----------------------

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # applied groupby function on teacherid
    # calculated count with unique values for subject_id
    df = teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index()
    # renamed existing column from subject_id to cnt as per output
    df = df.rename({'subject_id':'cnt'},axis=1)
    # returned dataframe result df
    return df