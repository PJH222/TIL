import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Melanoma.csv")

da1 = da.iloc[:123]
da2 = da.iloc[123:]

avgg = da1['thickness'].mean()
stdd = da1['thickness'].std()

std1 = (da1['thickness'] - avgg) / stdd
std2 = (da2['thickness'] - avgg) / stdd

cond1 = (std1[(std1 > -1) & (std1 < 1)])
cond2 = (std2[(std2 > -1) & (std2 < 1)])

med1 = cond1.median()
med2 = cond2.median()

result = round(med1+med2, 4)
print(result)


