import pandas as pd
data = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

a = data[['Manufacturer', 'Origin']].drop_duplicates()
b = a.shape

data['str'] = data['Manufacturer'].str[:2]

c = data[['Origin', 'str']].drop_duplicates()

result = a.shape[0] - c.shape[0]

print(result)
