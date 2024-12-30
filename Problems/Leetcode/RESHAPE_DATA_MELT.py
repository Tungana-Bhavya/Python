Reshape Data : Melt
-----------------------

import pandas as pd

df = pd.melt(report, id_vars =['product'],
    var_name ='quarter', value_name ='sales')
    return df