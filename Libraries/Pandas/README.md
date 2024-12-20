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

------------------------------------------------------------------------
- ##### DATA TRANSFORMATION
------------------------------------------------------------------------
- ##### DATA VISUALIZATION AND INTEGRATION
------------------------------------------------------------------------
- ##### INDEXING AND SELECTION
------------------------------------------------------------------------
- ##### FORMATTING DATA AND ITS CONVERSIONS
------------------------------------------------------------------------
