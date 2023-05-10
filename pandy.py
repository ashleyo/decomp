import pandas as pd
index=["Date","Time","Product","Quantity","OrderValue"]

df = pd.read_csv('SalesRecords.csv', names=index )
print(df.head())


df["ProductType"]=df["Product"].astype("category")
print(df.head())
print(df["ProductType"])


df2 = df[df["ProductType"].isin(["Cod", "Plaice", "Haddock", "Chips (large)", "Chips (small)", "Sausage", "Coke", "Fanta"])]
print(df2)

df2.drop(columns=['Product'],inplace=True)
print(df2)

df2.dropna(inplace=True)
df2["Quantity"]=df2["Quantity"].astype(int)
print(df2)

df2["OrderValue"]=df2["OrderValue"].str.strip(' £')

print(df2)

df2["OrderValue"]=df2["OrderValue"].astype(float, errors="ignore")
df2.dropna(inplace=True)
print(df2)
df2["Check"]=(df2["OrderValue"]/df2["Quantity"]).astype("category")
print(df2["Check"])
print(df2.groupby("Check").size())