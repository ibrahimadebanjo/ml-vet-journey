import pandas as pd
#dataframe basis
df = pd.read_csv('/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/Life_Expectancy_Data.csv')

#Data Exploration 
country = df["Country"]
#describe
summary = country.describe()
print(summary)

#value_counts
print("Value Count")
count = country.value_counts()
print(count)

#Assigning values
df["Country"] = "Ctry"


