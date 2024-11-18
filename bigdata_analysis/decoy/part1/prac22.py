import pandas as pd
import numpy as np

ex = pd.read_csv('C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv')

# # print(ex.columns)

# whe = ex['Wheelbase']
# stdd = whe.std()
# menn = whe.mean()

# pp_15 = menn + 1.5*stdd
# mm_15 = menn - 1.5*stdd
# pp_20 = menn + 2*stdd
# mm_20 = menn - 2*stdd
# pp_25 = menn + 2.5*stdd
# mm_25 = menn - 2.5*stdd

# a1 = whe[(whe > mm_15)&(whe < pp_15)].mean()
# a2 = whe[(whe > mm_20)&(whe < pp_20)].mean()
# a3 = whe[(whe > mm_25)&(whe < pp_25)].mean()

# result = menn * 3 - a1 - a2 - a3
# answer = round(result,4)
# print(answer)

# ex['rank'] = ex['Length'].rank(method = 'average')
# aa = ex['Length'][ex['rank'] < 30].std()
# answer = round(aa,3)
# print(answer)

# minn = ex['Min_Price'].sort_values(ascending = True, ignore_index = True)
# maxx = ex['Max_Price'].sort_values(ascending = False, ignore_index = True)

# aa = (maxx - minn).std()
# answer = round(aa, 3)
# print(answer)

# ex['minmax'] = (ex['Weight'] - ex['Weight'].min()) / (ex['Weight'].max() - ex['Weight'].min())
# # minmax = ex['minmax']
# a1 = ex['minmax'][ex['minmax'] < 0.5].var()
# a2 = ex['minmax'][ex['minmax'] > 0.5].var()


# result = abs(a2 - a1)
# # print(result)
# # 
# answer = round(result, 3)
# print(answer)

# onlyy = ex[['Manufacturer','Origin']].drop_duplicates()

# print(onlyy.shape[0])

# ex['22'] = ex['Manufacturer'].str[:2]
# onlyy2 = ex[['22','Origin']].drop_duplicates()

# print(onlyy2.shape[0])
# answer = 4

# a = ex.groupby(['Type','Man_trans_avail'])['RPM'].count()
# b = ex.groupby(['Type','Man_trans_avail'])['RPM'].sum()
# c = ex.groupby(['Type','Man_trans_avail'])['RPM'].median()

# answer = sum(c - b / a)
# print(round(answer,0))

# print(ex['RPM'].isna().sum())
# menn = ex['RPM'].mean()

# ex['RPM'] = ex['RPM'].fillna(menn)
# ex['z_Wheelbase'] = (ex['Wheelbase'] - ex['Wheelbase'].mean()) / ex['Wheelbase'].std()
# ex['z_RPM'] = (ex['RPM'] - ex['RPM'].mean()) / ex['RPM'].std()

# ex['z_Wheelbase'] = ex['z_Wheelbase'] * -36
# result = (ex['z_Wheelbase'] - ex['z_RPM']).std()
# answer = round(result, 3)
# print(answer)

# pri = ex['Price']
# ex2 = ex.copy()

# ex['Price'] = ex['Price'].fillna(pri.mean())
# ex['menn'] = (ex['Max_Price'] + ex['Min_Price']) / 2

# aa = ex[ex['Price'] < ex['menn']]
# bb = aa.groupby(['Origin'])['Price'].sum()


# ex2['Price'] = ex2['Price'].fillna(ex2['Price'].median())
# # a1 = ex2['Price'].quantile(0.25)
# # a2 = ex2['Price'].quantile(.5)
# a3 = ex2['Min_Price'].quantile(.75)
# cc = ex2[ex2['Price'] < a3]
# dd = cc.groupby(['Origin'])['Price'].sum()

# result = dd + bb
# answer = int(max(result))
# print(answer)

# pri_isna = ex['Price'].isna()
# a1 = ex['Price'].copy()
# a2 = ex['Max_Price'].copy()
# a3 = ex['Min_Price'].copy()

# a1[pri_isna] = (a2[pri_isna] + a3[pri_isna]) / 2
# ex['Price'] = a1

# pri = ex['Price']
# typ = ex['Type']

# cond1 = pri < 14.7
# cond2 = (pri > 25.3) & (typ == 'Large')

# print(ex[cond1 | cond2 ].shape[0])

mak = ex['Make'].copy()

# print(mak)
mak2 = mak.copy().str.strip()
cond1 = mak.str.startswith(('Chevrolet','Pontiac','Hyundai'))
cond11 = mak2.str.startswith(('Chevrolet','Pontiac','Hyundai'))
print(mak[cond1].shape)
print(mak2[cond1].shape)
air = ex['AirBags']
cond2 = (air == "Driver only")
# print(air[cond2])
answer = ex[cond1 & cond2].shape
answer2 = ex[cond11 & cond2].shape

print(mak[cond1], mak2[cond11])
print(mak[0:20])
# print(mak, mak11)
