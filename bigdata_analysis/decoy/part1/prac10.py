import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

makee = da['Make']
air = da['AirBags']

cond1 = makee.str.contains('Chevrolet') | makee.str.contains('Pontiac') | makee.str.contains('Hyundai')
cond2 = (air == "Driver only")

condition = cond1 & cond2

print(da[condition].shape[0])