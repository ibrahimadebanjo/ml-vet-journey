import pandas as pd
#dataframe basis
df = pd.read_csv('/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/Life_Expectancy_Data.csv', index_col = 0)
#datatype of each column
col_types = df.dtypes
print(col_types)
#dimension of a dataframe
print("Shape of a dataframe")
dims = df.shape
print(dims)
#selectimg data in a dataframe
print(df["Polio"])
print(["Year", "Status"])
print("head of the dataframe")
print(df.head())