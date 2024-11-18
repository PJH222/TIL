import pandas as pd
import numpy as np

ex = pd.read_csv('C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv')

# cnt_rpm = ex.groupby(['Type','Man_trans_avail'])['RPM'].count()
# sum_rpm = ex.groupby(['Type','Man_trans_avail'])['RPM'].sum()
# med_rpm = ex.groupby(['Type','Man_trans_avail'])['RPM'].median()

# result = sum(med_rpm - sum_rpm / cnt_rpm)
# answer = round(result,0)
# print(answer)

# ex['RPM'] = ex['RPM'].fillna(ex['RPM'].mean())

# ex['RPM'] = (ex['RPM'] - ex['RPM'].mean())/ex['RPM'].std()

# ex['Wheelbase'] = (ex['Wheelbase'] - ex['Wheelbase'].mean()) / ex['Wheelbase'].std() * -36
# a = (ex['Wheelbase'] - ex['RPM']).std()
# print(round(a,3))

ex1 = ex.copy()
ex2 = ex.copy()

ex1['Price'] = ex1['Price'].fillna(ex1['Price'].mean())
menn = ex1[['Max_Price','Min_Price']].mean(axis=1)
# print(ex1[['Max_Price','Min_Price','meann']])

sub_df = ex1[ex1['Price'] < menn]
gb_df = sub_df.groupby('Origin')['Price'].sum()
print(gb_df)

med = ex2['Price'].median()
ex2['Price'] = ex2['Price'].fillna(med)






