import pandas as pd

data = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

max_price = data['Max_Price'].sort_values(ascending = False, ignore_index = True)
min_price = data['Min_Price'].sort_values(ignore_index = True)
a = max_price - min_price
print(round(a.std(),3))


# print(max_price, min_price)