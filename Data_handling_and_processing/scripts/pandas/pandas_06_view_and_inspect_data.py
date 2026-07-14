import pandas as pd
#dataframe basis
df = pd.read_csv('/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/Life_Expectancy_Data.csv')
#head(n)
print(df.head(10))
#tail(n)
print(df.tail(5))
#shape
print(df.shape)
#info()
df.info()
#describe()
df.describe()
#value_counts
print(df.value_counts(dropna = False))