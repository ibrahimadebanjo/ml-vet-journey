import pandas as pd
#dataframe basis
df = pd.read_csv('/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/Life_Expectancy_Data.csv')
#Iloc 
print(df.iloc[0])
print(df.iloc[:, 3]) #all rows column 3
#Loc
print("Loc")
print(df.loc[2])
#is null
print("Country is null")
country_is_null = df["Country"].isnull()
print(country_is_null)

