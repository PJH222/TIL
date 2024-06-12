import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

price = da['Price'].copy()
minn = da['Min_Price'].copy()
maxx = da['Max_Price'].copy()
typee = da['Type'].copy()

na = price.isna()
price[na] = (minn[na] + maxx[na]) / 2

cond1 = price < 14.7
cond2 = (price > 25.3) & (typee == "Large")
condition = cond1 | cond2

result = da[condition]
# print(result.count()) # 각 원소의 개수를 뜻하는듯...
# print(result.shape)
print(result.shape[0])
# print(result)
