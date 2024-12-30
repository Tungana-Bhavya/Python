Reshape Data : Pivot
-----------------------

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.pivot_table(index ='month', 
    values = 'temperature',
    columns ='city')
    return weather