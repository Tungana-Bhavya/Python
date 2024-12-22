#### EXPLORATORY DATA ANALYSIS (EDA)
------------------------------------
- ##### IMPORTING LIBRARIES
1. <b>How to import pandas library with alias name</b><br>
import pandas as pd
------------------------------------
- ##### LOADING DATA INTO DATAFRAME
1. <b>How to read csv file ?</b> <br>
df = pd.read_csv('filename.csv')

2. <b>How to read excel file ?</b> <br>
df = pd.read_excel('filename.xlsx')

3. <b>How to read sql database file ?</b><br>
df = pd.read_sql(query, connection)
------------------------------------
- ##### INSPECTION OF DATA
1. <b> How to display index, columns and data ?</b><br>
df.info()

2. <b> How to get top rows?</b><br>
df.head()

3. <b> How to get top ten rows ?</b><br>
df.head(10)

4. <b> How to get botton rows ?</b><br>
df.tail()

5. <b> How to get bottom ten rows ?</b><br>
df.tail(10)

6. <b> How to get statistical summary of data ?</b><br>
df.describe()

7. <b> How to get datatypes of data ?</b><br>
df.dtypes()
------------------------------------
- ##### DATA CLEANING

1. <b> How to check for missing values in dataframe ? </b><br>
df.isnull().sum()

3. <b>How to fill missing values ?</b><br>
df.fillna(value)

4. <b>How to drop missing values ?</b><br>
df.dropna()

5. <b>How to Rename Columns ?</b><br>
df.rename(columns={'old_name':'new_name'})

6. <b>How to drop Columns</b><br>
df.drop(columns=['col1',col2',...,'coln'])
------------------------------------------------------------------------
- ##### DATA TRANSFORMATION
1. <b>How to concatenate dataframes ?</b><br>
df.concat([df1,df2])

2. <b>How to merge dataframes ?</b><br>
pd.merge(df1,df2, on='column')
------------------------------------------------------------------------
- ##### DATA VISUALIZATION AND INTEGRATION
------------------------------------------------------------------------
- ##### INDEXING AND SELECTION
1. <b>How to select column</b><br>
df['column']

2. <b>How to select multiple columns ?</b><br>
method 1 : By using square brackets<br>
df[['col1','col2','col3']]

method 2 : By using loc method<br>
df.loc[[:,['col1','col2','col3]]

method 3 : By using integer loc method<br>
df.iloc[[:,[0,1,2]]

3. <b>How to select rows by its position ?</b><br>
df.iloc[0:4]

4. <b>How to select rows by its label ?</b><br>
df.loc[0:7]

5. <b>How to select column with condition ?</b><br>
df[df['col']>value]

6. <b>How to select columns with multiple conditions ?</b><br>
df[(df['col1'] > 4) & (df['col2'] =='abc')]

------------------------------------------------------------------------
- ##### FORMATTING DATA AND ITS CONVERSIONS
------------------------------------------------------------------------
