#importing library
import sqlite3
import pandas as pd
#read csv 
csv = pd.read_csv('/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/Life_Expectancy_Data.csv')
#read table
tsv = pd.read_table("/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/weather.tsv")
print(tsv)
#read excel
#ex = pd.read_excel("/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/excel_sample.xlsx")

#read sql
print("Sql import and usage in pandas")
conn = sqlite3.connect("/storage/emulated/0/Download/ml-vet-journey/Data_handling_and_processing/cheatsheets_and_data/chinook.db")
df = pd.read_sql("SELECT * FROM  albums LIMIT 5", conn)
print(df)
# JSON import and loading
print("JSON file parsing")
url = "https://api.github.com/users/octocat/repos"
df = pd.read_json(url)
print(df.head())
# Reading dict using pandas
d = {'Name': ['dog', 'cat'], 'Age': [3, 2]}  # column → list
df = pd.DataFrame(d)
print(df)