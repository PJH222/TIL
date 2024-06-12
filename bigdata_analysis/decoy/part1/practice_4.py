import pandas as pd

data = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

a = data['Weight']
a_std = (a - min(a))/(max(a) - min(a))
min_std = a_std[a_std < 0.5].var()
max_std = a_std[a_std > 0.5].var()

print(round(min_std - max_std,3))