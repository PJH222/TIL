import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

# 1번
# wb = da['Wheelbase']
# avgg = wb.mean()
# stdd = wb.std()
#
# # case1  std 1.5배
# avgg11 = avgg + stdd * 1.5
# avgg12 = avgg - stdd * 1.5
#
# cond1 = (wb < avgg11) & (wb > avgg12)
# result1 = wb[cond1].mean()
#
# # case2  std 2배
# avgg21 = avgg + stdd * 2
# avgg22 = avgg - stdd * 2
#
# cond2 = (wb < avgg21) & (wb > avgg22)
# result2 = wb[cond2].mean()
#
# # case3  std 2.5배
# avgg31 = avgg + stdd * 2.5
# avgg32 = avgg - stdd * 2.5
#
# cond3 = (wb < avgg31) & (wb > avgg32)
# result3 = wb[cond3].mean()
#
# result = 3 * avgg - (result1 + result2 + result3)
# answer = round(result, 4)
# print(answer)


# 2 번

# leng = da['Length'].rank(method='max')
# aa = da['Length'][leng <= 30]
#
# stdd = aa.std()
# answer = round(stdd, 3)
# print(answer)



# 3 번

# 1) Max_price, Min_Price컬럼을 각각 정렬하기
# 2) 정렬된 순서에 따라 레코드별로 Max_ Min_ 차이를 구하기
# 3) 차이값에 대한 표준편차 구하기
# maxx = da['Max_Price'].copy()
# minn = da['Min_Price'].copy()
#
# aa = maxx.sort_values(ascending = False, ignore_index = True)
# bb = minn.sort_values(ignore_index = True)
# # 이거 안쓰면 틀린다...
#
# cc = aa - bb
# result = cc.std()
# answer = round(result, 3)
# print(answer)
#




# 4 번
# minn = min(da['Weight'])
# maxx = max(da['Weight'])
#
#
# da['Weight'] = (da['Weight'] - minn) / (maxx - minn)
# wei = da['Weight']
#
# aa = da['Weight'][wei < 0.5].var()
# bb = da['Weight'][wei > 0.5].var()
#
# result = abs(aa - bb)
# answer = round(result, 3)
# print(answer)



# 5 번
# aa = da[['Manufacturer', 'Origin']].drop_duplicates()
# result1 = aa.shape[0]
#
# da['strr'] = da['Manufacturer'].str[:2]
# bb = da[['strr', 'Origin']].drop_duplicates()
# result2 = bb.shape[0]
#
# answer = result1 - result2
# print(answer)



# 6 번

# cnt = da.groupby(['Type', 'Man_trans_avail'])['RPM'].count()
# summ = da.groupby(['Type', 'Man_trans_avail'])['RPM'].sum()
# medd = da.groupby(['Type', 'Man_trans_avail'])['RPM'].median()
#
# result = medd - summ / cnt
# answer = round(sum(result), 0)
# print(answer)



# 7 번
# avgg = da['RPM'].mean()
# da['RPM'] = da['RPM'].fillna(avgg)
# # 실수하지말라...
#
# rpm_avgg = da['RPM'].mean()
# rpm_stdd = da['RPM'].std()
#
# wb_avgg = da['Wheelbase'].mean()
# wb_stdd = da['Wheelbase'].std()
#
# da['RPM'] = (da['RPM'] - rpm_avgg)/(rpm_stdd)
# da['Wheelbase'] = (da['Wheelbase'] - wb_avgg)/(wb_stdd)
#
# result = da['Wheelbase'] * -36 - da['RPM']
# answer = round(result.std(), 3)
# print(answer)




# 8 번
# da1 = da.copy()
# da2 = da.copy()
#
# pri_avgg = da1['Price'].mean()
# da1['Price'] = da1['Price'].fillna(pri_avgg)
# # avgg = (da1['Max_Price'] + da1['Min_Price']) / 2
# avgg = da1[['Max_Price','Min_Price']].mean(axis=1)
# # print(avgg)
# aa = da1[da1['Price'] < avgg]
#
# result1 = aa.groupby('Origin')['Price'].sum()
#
#
# pri_med = da2['Price'].median()
# da2['Price'] = da2['Price'].fillna(pri_med)
#
# qa3 = da2['Min_Price'].quantile(0.75)
#
# cc = da2[da2['Price'] < qa3]
# result2 = cc.groupby('Origin')['Price'].sum()
#
# result = max(result1 + result2)
# # answer = int(result)
# print(int(result))




# 9 번

# na = da['Price'].isna()
#
# pri = da['Price'].copy()
# maxx = da['Max_Price'].copy()
# minn = da['Min_Price'].copy()
# typee = da['Type'].copy()
#
# pri[na] = (maxx[na] + minn[na]) / 2
#
# cond1 = pri < 14.7
# cond2 = (pri > 25.3) & (typee == 'Large')
#
# condition = cond1 | cond2
# print(pri[condition].count())




# 10 번
# makk = da['Make']
# air = da['AirBags']
#
# cond1 = makk.str.contains("Chevrolet") | makk.str.contains("Pontiac") | makk.str.contains("Hyundai")
# cond2 = (air == "Driver only")
#
# condition = cond1 & cond2
#
# result = da['Make'][condition].count()
# print(result)


# 11 번

# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit.csv")
# q3 = da['Dose'].quantile(0.75)
# q2 = da['Dose'].quantile(0.50)
#
# result = abs(q3 - q2)
# answer = int(result)
#
# print(answer)


# 12 번

# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Boston.csv")
# da['bin'] = pd.cut(da['medv'], bins=[0,10,20,30,40,50])
# aa = da['bin'].value_counts().idxmax()
#
# result = da['dis'][da['bin'] == aa].median()
# # print(result)
#
# answer = round(result,2)
# #
# print(answer)



# 13 번
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Melanoma.csv")
#
# d1 = da.iloc[:123].copy()
# d2 = da.iloc[123:].copy()
#
# avgg = d1['thickness'].mean()
# stdd = d1['thickness'].std()
#
# d1['zz'] = (d1['thickness'] - avgg)/stdd
# d2['zz'] = (d2['thickness'] - avgg)/stdd
#
# zz1 = d1['zz']
# zz2 = d2['zz']
#
# cond11 = (zz1 > -1)
# cond12 = (zz1 < 1)
# condition1 = cond11 & cond12
#
# cond21 = (zz2 > -1)
# cond22 = (zz2 < 1)
# condition2 = cond21 & cond22
#
# result1 = zz1[condition1].median()
# result2 = zz2[condition2].median()
#
# result = result1 + result2
# answer = round(result, 4)
# print(answer)