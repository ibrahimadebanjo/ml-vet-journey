import pandas as pd
df = pd.read_csv('/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/Life_Expectancy_Data.csv')
#creating matirrx of features
print("matrix of features")
x = df.iloc[ : , : -1].values
print(x)
print("dependent variables")
# creating dependent variable
y = df.iloc[ : , -1 ].values
print(y)