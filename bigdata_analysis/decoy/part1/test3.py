import pandas as pd

 # 2번
da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
# leng = da['Length'].rank(method='average',ascending = True)
# aa = da['Length'][leng < 30]
# result = aa.std()
# answer = round(result, 3)
# print(answer)


 # 3번
# aa = da['Max_Price'].copy()
# bb = da['Min_Price'].copy()
#
# cc = aa.sort_values(ascending = False, ignore_index=1)
# dd = bb.sort_values(ignore_index=1)
# # print(cc, dd)
# ee = cc - dd
# # print(ee)
# result = ee.std()
#
# answer = round(result, 3)
# print(answer)


 # 5번
# result1 = da[['Manufacturer', 'Origin']].drop_duplicates().shape[0]
#
# da['strr'] = da['Manufacturer'].str[:2]
# result2 = da[['strr', 'Origin']].drop_duplicates().shape[0]
#
# print(result1 - result2)


 # 10번
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
# makk = da['Make'].copy()
# cond1 = da['Make'].str.contains('Chevrolet') | da['Make'].str.contains('Pontiac') | da['Make'].str.contains('Hyundai')
#
# # print(da['AirBags'])
# cond2 = da['AirBags'].str.contains('Driver only')
# condition = cond1 & cond2
# result = da[condition].shape[0]
#
# print(result)


 # 12번
da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Boston.csv")
# print(max(da['medv']))

da['bin'] = pd.cut(da['medv'], bins=[i for i in range(0, 100 , 10)])
aa = da['bin'].value_counts().idxmax()
result = da['dis'][da['bin'] == aa].median()
answer = round(result, 2)
print(answer)



