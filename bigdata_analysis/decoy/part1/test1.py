import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

# 5번
# aa = da[['Manufacturer', 'Origin']].drop_duplicates()
# result1 = aa.shape[0]
#
# da['str'] = da['Manufacturer'].str[:2]
# bb = da[['str', 'Origin']].drop_duplicates()
# result2 = bb.shape[0]
#
# answer = result1 - result2
# print(answer)

# 6번
# cntt = da.groupby(['Type' ,'Man_trans_avail'])['RPM'].count()
# summ = da.groupby(['Type' ,'Man_trans_avail'])['RPM'].sum()
# medd = da.groupby(['Type' ,'Man_trans_avail'])['RPM'].median()
#
# result = sum(medd - summ / cntt)
#
# answer = round(result, 0)
# print(answer)


# 7 번
# 1) RPM 컬럼 결측치를 평균으로 대체
# avgg = da['RPM'].mean()
# da['RPM'] = da['RPM'].fillna(avgg)
#
# rpm = da['RPM']
# rpm_avgg = rpm.mean()
# rpm_std = rpm.std()
#
# da['RPM'] = (rpm - rpm_avgg) / rpm_std
# # rpm2 = (da['RPM'] - rpm_avgg) / rpm_std
#
# wb = da['Wheelbase']
# wb_avgg = wb.mean()
# wb_std = wb.std()
#
# da['Wheelbase'] = (wb - wb_avgg) / wb_std
#
# da['diff'] = da['Wheelbase'] * (-36) - da['RPM']
# answer = round(da['diff'].std(), 3)
# print(answer )



# 8번
# case 1
# da1 = da.copy()
#
# da1_avgg = da1['Price'].mean()
# da1['Price'] = da1['Price'].fillna(da1_avgg)
# minmax = (da1['Max_Price'] + da1['Min_Price']) / 2
#
# aa1 = da1[da1['Price'] < minmax]
# result1 = aa1.groupby('Origin')['Price'].sum()
#
# # case 2
# da2 = da.copy()
# medd = da2['Price'].median()
#
# da2['Price'] = da2['Price'].fillna(medd)
#
# qa3 = da2['Min_Price'].quantile(0.75)
# bb = da2[da2['Price'] < qa3]
#
# result2 = bb.groupby("Origin")['Price'].sum()
#
# result = result1 + result2
# print(int(max(result)))


# 9 번
# pri = da['Price'].copy()
# maxx = da['Max_Price'].copy()
# minn = da['Min_Price'].copy()
#
# na = pri.isna()
#
# pri[na] = (da['Max_Price'][na] + da['Min_Price'][na]) / 2
# # print(pri)
# typee = da['Type'].copy()
#
# cond1 = pri < 14.7
# cond2 = (pri > 25.3) & (typee == 'Large')
#
# condition = cond1 | cond2
#
# result = da[condition]
# print(result.shape[0])



# 10 번

# makee = da['Make'].copy()
# cond1 = makee.str.contains("Chevrolet") | makee.str.contains("Pontiac") | makee.str.contains("Hyundai")
#
# air = da['AirBags'].copy()
# cond2 = (air == "Driver only")
#
# condition = cond1 & cond2
# result = da[condition]
# print(result.shape[0])


# 11 번
# daa = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit.csv")
#
# qa2 = daa['Dose'].quantile(0.5)
# qa3 = daa['Dose'].quantile(0.75)
#
# result = abs(qa3 - qa2)
# answer = int(result)
#
# print(answer)



# 12 번
# daa = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Boston.csv")
# # print(max(daa['medv']))
#
# aa = pd.cut(daa['medv'], bins =[0,10,20,30,40,50,60])
# daa['bin'] = aa
#
# bb = (daa['bin'].value_counts().idxmax())
#
#
# print(bb)
# cc = daa[daa['bin'] == bb]
#
# result = cc['dis'].median()
# answer = round(result,2)
# print(answer)


# 13 번
da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Melanoma.csv")

da1 = da.iloc[:123].copy()
da2 = da.iloc[123:].copy()

avgg = da1['thickness'].mean()
stdd = da1['thickness'].std()

# case 1
da1['stdd'] = (da1['thickness'] - avgg) / stdd
ddd = da1['stdd']
cond11 = ( ddd < 1 ) & ( ddd > -1 )
result1 = da1['stdd'][cond11].median()
# print(result1)

# case 2
da2['stdd'] = (da2['thickness'] - avgg) / stdd
dd2 = da2['stdd']
cond22 = (dd2 < 1) & (dd2 > -1)
result2 = da2['stdd'][cond22].median()

answer = round(result1 + result2, 4)
print(answer)
