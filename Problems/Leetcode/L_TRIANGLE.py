Triangle Judement
-----------------------

1. Using Lambda function

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = triangle.apply(
        lambda a: 'Yes' if ((a.x + a.y > a.z) & (a.y + a.z > a.x) & (a.x + a.z > a.y)) 
        else 'No', axis =1)
    return triangle

#2. Using Map function

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = (triangle['x'] + triangle['y'] > triangle['z']) & (triangle['y'] + triangle['z']> triangle['x']) & (triangle['x'] + triangle['z'] > triangle['y'])
    triangle['triangle'] = triangle['triangle'].map({True:'Yes', False:'No'})
    return triangle
