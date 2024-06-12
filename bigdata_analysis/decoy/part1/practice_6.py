import pandas as pd

data = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

cnt = data.groupby(['Type','Man_trans_avail'])['RPM'].count()
summ = data.groupby(['Type','Man_trans_avail'])['RPM'].sum()
medd = data.groupby(['Type','Man_trans_avail'])['RPM'].median()

# print(cnt, summ, medd)

result = sum(medd - summ/cnt)
print(round(result,0))