import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Boston.csv")

da['cutt'] = pd.cut(da['medv'], bins = [0,10,20,30,40,50,60])
cutt = da['cutt']
mode = cutt.value_counts().idxmax()

cond = (cutt == mode)

medi = da['dis'][cond].median()
result = round(medi,2)

print(result)