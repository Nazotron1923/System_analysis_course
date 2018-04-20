import pandas as pd
file = pd.read_excel('table_51.xlsx')
print(file)

file.to_csv('test.csv')
