import pandas as pd
index=["Date","Time","Product","Quantity","OrderValue"]

df = pd.read_csv('SalesRecords.csv', )
df.index = index
print(df.head())
