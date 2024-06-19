# import pandas as pd
# da = pd.read_csv("economics.csv")
#
# # print(da.) 데이터수집월  개인소비지출_십억달러      총인구_천명  개인저축률  중앙_실업기간_주  실업자수_천명
#
# da['데이터수집월'] = da['데이터수집월'].str.replace(' ','')
# da['year'] = da['데이터수집월'].str[:4].copy()
#
# year = da['year'].copy()
#
# aa = da.groupby('year')['실업자수_천명'].sum().idxmax()
# print(aa) # 2010
# answer = (da[year == "2010"]['실업자수_천명'] / 10).var()
# print(round(answer,2)) # 1111.35

# import pandas as pd
# da = pd.read_csv("Airline.csv")
# # print(da.columns)['Gender', 'Ages', 'Customer_Type', 'Class',
# #        'Departure_Delay_in_Minutes', 'Arrival_Delay_in_Minutes']
#
# print(da['Ages'].unique())
#
# tmp = { "[10, 20)" :  "10_19",
#         "10_19" : "10_19",
#         "20_29": "20_29",
#         "30_39" : "30_39",
#         "40_49":"40_49",
#         "50_59":"50_59",
#         "[20, 30)" : "20_29",
#         "[40, 50)":"40_49",
#         "[50, 60)":"50_59"  }
#
# da['Ages'] = da['Ages'].copy().map(tmp)
#
# aa = da.groupby('Ages')['Departure_Delay_in_Minutes'].mean()
# print(aa.idxmax()) # 50_59
# age = da['Ages']
# typ = da['Customer_Type']
#
#
#
# ans1 = (age == "50_59")
# ans2 = (typ == "L")
# print(len(da[ans2 & ans1])) # 1101



