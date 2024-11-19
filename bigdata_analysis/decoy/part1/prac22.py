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

# mak = ex['Make'].copy()

# # print(mak)
# mak2 = mak.copy().str.strip()
# cond1 = mak.str.startswith(('Chevrolet','Pontiac','Hyundai'))
# cond11 = mak2.str.startswith(('Chevrolet','Pontiac','Hyundai'))
# print(mak[cond1].shape)
# print(mak2[cond1].shape)
# air = ex['AirBags']
# cond2 = (air == "Driver only")
# # print(air[cond2])
# answer = ex[cond1 & cond2].shape
# answer2 = ex[cond11 & cond2].shape

# print(mak[cond1], mak2[cond11])
# print(mak[0:20])
# # print(mak, mak11)

# mak = ex['Make']
# df1 = mak.copy()
# df1 = df1.str.strip()
# cond1 = df1.str.startswith(('Chevrolet','Pontiac','Hyundai'))

# air = ex['AirBags']
# # print(air.value_counts())
# cond2 = (air == 'Driver only')

# answer = ex[cond1 & cond2].shape
# print(answer[0])

# ex = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit.csv")

# dos = ex['Dose']
# tmp1 = dos.quantile(0.75)
# tmp2 = dos.quantile(0.5)
# answer = abs(tmp1 - tmp2)
# print(int(answer))


# ex = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Boston.csv")
# # print(max(ex['medv']))

# ex['medv_cut'] = pd.cut(ex['medv'],bins = [0,10,20,30,40,50,60])
# # print(medv_cut.max())

# mode = ex['medv_cut'].value_counts().idxmax()
# cond = (ex['medv_cut'] == mode)

# print(round(ex['dis'][cond].median(),2))

ex = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Melanoma.csv")
# df1 = ex[:123]
# df2 = ex[123:]

# thi1 = df1['thickness']
# thi2 = df2['thickness']

# men1 = thi1.mean()
# men2 = thi2.mean()

# std1 = thi1.std()
# std2 = thi2.std()

# aa = (thi1 - men1)/std1
# bb = (thi2 - men2)/std2

# result1 = aa[(aa >= -1) & (aa <= 1)].median()
# result2 = bb[(bb >= -1) & (bb <= 1)].median()

# answer = round(result1 + result2, 4)
# print(answer)

# df1 = ex.copy().iloc[:123]
# df2 = ex.copy().iloc[123:]

# men1 = df1['thickness'].mean()
# men2 = df2['thickness'].mean()

# sd1 = df1['thickness'].std()
# sd2 = df2['thickness'].std()

# aa1 = (df1['thickness'] - men1) / sd1
# aa2 = (df2['thickness'] - men2) / sd2

# res1 = aa1[(aa1>=-1)&(aa1<=1)].median()
# res2 = aa2[(aa2>=-1)&(aa2<=1)].median()
# print(round(res1+res2,4))

# df1 = ex.iloc[:123]
# df2 = ex.iloc[123:]

# avg = df1['thickness'].mean()
# sd = df1['thickness'].std()

# std1 = (df1['thickness'] - avg) / sd
# std2 = (df2['thickness'] - avg) / sd

# res1 = std1[(std1 > -1)&(std1 < 1)].median()
# res2 = std2[(std2 > -1)&(std2 < 1)].median()

# answer = round(res1+res2 , 4)
# print(answer)

ex = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
# ex['rank'] = ex['Length'].rank(method = "average")
# rank = ex['rank']

# a = ex['Length'][rank < 30].std()
# answer = round(a,3)
# print(answer)

# maxx = ex['Max_Price'].sort_values(ascending=False, ignore_index = True)
# minn = ex['Min_Price'].sort_values(ascending=True, ignore_index = True)

# answer = round((maxx - minn).std(),3)
# print(answer)
# wei = ex['Weight']
# men = wei.mean()
# stdd = wei.std()

# wei = (wei - wei.min()) / (wei.max() - wei.min())
# aa = wei[wei < 0.5].var()
# bb = wei[wei > 0.5].var()
# answer = round(abs(aa-bb),3)
# print(answer)

# aa = ex.drop_duplicates(('Manufacturer','Origin')).shape[0]
# ex['22'] = ex['Manufacturer'].str[:2]
# bb = ex.drop_duplicates(('22','Origin')).shape[0]

# answer = abs(aa - bb)
# print(answer)

# cnt = ex.groupby(['Type','Man_trans_avail'])['RPM'].count()
# summ = ex.groupby(['Type','Man_trans_avail'])['RPM'].sum()
# medd = ex.groupby(['Type','Man_trans_avail'])['RPM'].median()

# # print(cnt,summ,medd)

# res = sum(medd - summ / cnt)
# answer = res
# print(round(answer,0))

# menn = ex['RPM'].mean()
# ex['RPM'] = ex['RPM'].fillna(menn)

# r = ex['RPM']
# mm = r.mean()
# sd = r.std()

# a = (r - mm) / sd

# w = ex['Wheelbase']
# m = w.mean()
# sdd = w.std()

# b = (w - m) / sdd

# result = b * -36 - a
# answer = round(result.std(), 3)
# print(answer)

# ex1 = ex.copy()
# ex2 = ex.copy()


# pri = ex['Price'].copy()
# men = pri.mean()
# ex1['Price'] = pri.fillna(men)
# pri = ex1['Price']


# men = (ex['Max_Price'] + ex['Min_Price']) / 2

# tmp1 = ex[pri < men]
# # print(tmp1)
# aa = tmp1.groupby(['Origin'])['Price'].sum()
# print(aa)



# pri = ex2['Price']
# med = pri.median()
# ex2['Price'] = ex2['Price'].fillna(med)

# q3 = ex2['Min_Price'].quantile(0.75)
# cond = (pri < q3)

# ex2 = ex[cond]
# tmp2 = ex2.groupby(['Origin'])['Price'].sum()
# print(tmp2)

# print(((aa + tmp2).max()))

# ex1 = ex.copy()
# ex2 = ex.copy()

# menn = ex1['Price'].mean()
# ex1['Price'] = ex1['Price'].fillna(menn)
# ex1['menn'] = (ex['Max_Price'] + ex['Min_Price']) / 2
# mennn = ex1['menn']
# pri = ex1['Price']
# cond1 = (pri < mennn)
# ex1 = ex1[cond1]

# result1 = ex1.groupby(['Origin'])['Price'].sum()

# med = ex2['Price'].median()
# ex2['Price'] = ex2['Price'].fillna(med)

# q3 = ex2['Min_Price'].quantile(0.75)
# pri2 = ex2['Price']
# cond2 = (pri2 < q3)
# ex2 = ex2[cond2]

# result2 = ex2.groupby(['Origin'])['Price'].sum()

# answer = max(result1 + result2)
# print(int(answer))

# ex['menn'] = (ex['Max_Price'] + ex['Min_Price']) / 2
# cond = ex['Price'].isna()

# pri = ex['Price']
# pri[cond] = ex['menn']

# cond1 = (pri < 14.7)

# # print(ex.columns)
# ty = ex['Type']
# cond2 = ((pri > 25.3) & (ty == "Large"))
# answer = ex[cond1 | cond2].shape[0]
# print(answer)


# mak = ex['Make']
# mak = mak.str.strip()
# cond1 = mak.str.startswith(('Chevrolet','Pontiac','Hyundai'))

# ai = ex['AirBags']
# cond2 = (ai == 'Driver only')

# answer = ex[cond1 & cond2].shape[0]
# print(answer)

# ex = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit.csv")

# do = ex['Dose']
# q2 = do.quantile(0.5)
# q3 = do.quantile(0.75)

# answer = int(abs(q2-q3))
# print(answer)

# ex = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Boston.csv")

# # print(ex['medv'].max())
# medv_bin = pd.cut(ex['medv'],bins = [0,10,20,30,40,50,60])
# cnt = medv_bin.value_counts().idxmax()

# cond = (medv_bin == cnt)
# res = ex['dis'][cond].median()
# answer = round(res,2)
# print(answer)

ex = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Melanoma.csv")
df1 = ex.copy()[:123]
df2 = ex.copy()[123:]

men = df1['thickness'].mean()
sd = df1['thickness'].std()

print(men, sd)
dt1 = df1['thickness']
dt2 = df2['thickness']

df1['zz'] = (dt1 - men) / sd
df2['zz'] = (dt2 - men) / sd


zz1 = df1['zz'].copy()
zz2 = df2['zz'].copy()
# print(zz1)
cond1 = ((zz1 < 1) & (zz1 > -1))
cond2 = ((zz2 < 1) & (zz2 > -1))

res1 = zz1[cond1].median()
res2 = zz2[cond2].median()

answer = round(res1 + res2 , 4)
print(answer)