# import pandas as pd
#
# # 1유형
# # 1번
# da = pd.read_csv("economics.csv")
#
# # print(da.columns) Index(['데이터수집월', '개인소비지출_십억달러', '총인구_천명', '개인저축률', '중앙_실업기간_주', '실업자수_천명'], dtype='object')
#
# da['데이터수집월'] = da['데이터수집월'].str.replace(' ','')
# da['year'] = da['데이터수집월'].str[:4]
# da['month'] = da['데이터수집월'].str[5:7]
#
# aa = da.groupby('year')['실업자수_천명'].sum().idxmax() # 2010년
#
# yearr = da['year'].copy()
#
# date = da[yearr == '2010'].copy()
# date['실업자수_만명'] = date['실업자수_천명'].copy() / 10
#
# # print(aa, yearr)
#
# answer = date['실업자수_만명'].var()
# print(round(answer,2))


# import pandas as pd
#
# da = pd.read_csv("Airline.csv")
#
# # print(da.columns)['Gender', 'Ages', 'Customer_Type', 'Class',
# #        'Departure_Delay_in_Minutes', 'Arrival_Delay_in_Minutes']
#
# # for i in da.columns:
# #     print(da[i].value_counts())
#
# tmp = {"[40, 50)" : "40_49",
#        "[50, 60)" : "50_59",
#        "[10, 20)" : "10_19",
#        "[20, 30)" : "20_29",
#        "40_49" : "40_49",
#        "50_59" : "50_59",
#        "30_39" : "30_39",
#        "20_29" : "20_29",
#        "10_19" : "10_19"}
# # print(da['Ages'].value_counts())
# da['Ages'] = da['Ages'].map(tmp)
# # [40, 50)    834
# # [50, 60)    758
# # 40_49       469
# # 50_59       421
# # 30_39       274
# # 20_29       103
# # 10_19        39
# # [10, 20)      1
# # [20, 30)      1
# # print(da['Ages'].value_counts())
#
# aa = da.groupby('Ages')['Departure_Delay_in_Minutes'].mean().idxmax() # 50_59
#
# age = da['Ages'].copy()
# typ = da['Customer_Type'].copy()
#
# cond1 = (age == aa)
# cond2 = (typ == "L")
#
# answer = da[cond1 & cond2].count()
# print(int(answer.iloc[0]))

# import pandas as pd
#
# da = pd.read_csv("spb_daily.csv")
# # print(da.columns) ['자전거ID', '대여일시', '대여소번호', '대여소명', '이용시간', '이용거리']
#
# for i in da.columns:
#     # print(da[i].unique())
#     pass
#
# # print(da['대여일시'].head()) 2022-06-01 11:01
#
# da['대여소번호'] = (da['대여소번호'].str.replace(' ',''))
# da['대여시간대'] = da['대여일시'].str[-5:-3]
# # print(da['대여시간대'], da['대여일시'])
#
# center_number = da['대여소번호'].copy()
# times = da['대여시간대'].copy()
#
# # print(da.info())
#
# cond1 = (center_number.str[0] == '4')
#
# da = da[cond1].copy()
#
# aa = da.groupby('대여시간대')['이용시간'].sum()
# # print(sorted(aa)) # 3637 시간, 18시에 가장 많이 빌림
# times = da['대여시간대'].copy()
#
# cond2 = (times == '18')
# bb = da[cond2].groupby('대여소번호')['이용거리'].sum()
# print(bb) # 79701.72 >>> 420
#
# answer = 420
# print(answer)


# 3 유형
# 1번

# import pandas as pd
#
# da = pd.read_csv("satisfy.csv")
# # 만족 성별 등급
#
# sex = da['성별'].copy()
#
# for i in da.columns:
#     a = da[i].unique()
#     idx = 0
#     tmp = {}
#     if da[i].dtype == 'object':
#         for j in a:
#             tmp[j] = idx
#             idx += 1
#         da[i] = da[i].map(tmp).astype('float64')
#
# da['만족'] = da['만족'].astype('float64')
#
# print(da['등급'].value_counts())
# print(da.info())
# import statsmodels.api as sm
# import numpy as np
#
# # da['만족'] = (da['만족'])
# # da['만족'] = da['만족'].map({1 : "Yes" , 0 : "No"})
# # print(da['만족'])
#
# dummies = pd.get_dummies(da, columns = ['성별','등급'],drop_first = True)
# print(dummies)
# y = dummies['만족']
# X = dummies[['성별_1.0',  '등급_1.0'  ,'등급_2.0']]
# X = sm.add_constant(X)
# print(y,X)
#
# model = sm.GLM(y,X,family=sm.families.Binomial())
# result = model.fit()
#
# print(result.summary())
#
# import pandas as pd
# da = pd.read_csv("satisfy.csv")
#
# import statsmodels.api as sm
# import numpy as np
# from scipy.stats import chi2
#
# dummies = pd.get_dummies(da,columns=['성별','등급'],drop_first=True)
# # print(dummies)
# tmp = {True : 1, False : 0}
# for i in ['성별_M',   '등급_B',   '등급_S']:
#     dummies[i] = dummies[i].map(tmp)
#
# # print(dummies)
# y = dummies['만족']
# x = dummies[['성별_M',   '등급_B',   '등급_S']]
# x = sm.add_constant(x)
#
#
#
#
# result = sm.GLM(y,x , family=sm.families.Binomial()).fit()
#
# print(result.summary())
#
# answer_a = 0.0846
# answer_b = np.exp(0.0846)
# # print(answer_a)
# answer_c = 3256
#
# a =(result.null_deviance)
# b = (result.deviance)
# print(a-b)
# pval = 1 - chi2.cdf(a-b,3)
# print(pval)


# import pandas as pd
# da = pd.read_csv("satisfy.csv")
#
# import statsmodels.api as sm
# import numpy as np
# from scipy.stats import chi2
#
# dummies = pd.get_dummies(da, ['성별','등급'], drop_first = True)
# # print(dummies)
#
# tmp = {True : 1, False : 0}
# for i in ['성별_M',   '등급_B',   '등급_S']:
#     dummies[i] = dummies[i].map(tmp)
#
# y = dummies['만족']
# x = dummies[['성별_M',   '등급_B',   '등급_S']]
# x = sm.add_constant(x)
#
# result = sm.GLM(y,x,family=sm.families.Binomial()).fit()
# print(result.summary())
#
# answer_a = round(0.0846,2)
# answer_b = np.exp(0.0846)
# answer_c = result.deviance
#
# stat = result.null_deviance - result.deviance
# pval = 1 - chi2.cdf(stat,3)
# print(pval)
# answer_d = 0
# print(answer_a, answer_b, int(answer_c), answer_d)





# import pandas as pd
#
# da = pd.read_csv("airpollution.csv")
# # city  SO2  temp  manu  popul  wind  precip  predays
# # da = da.drop('city')
# # print
# import statsmodels.api as sm
# from statsmodels.stats.outliers_influence import OLSInfluence
#
# city = da['city'].copy()
# y = da['SO2']
# x = da.drop(['SO2','city'], axis=1)
# x = sm.add_constant(x)
#
# result = sm.OLS(y,x).fit()
# # print(result.summary())
#
# a = OLSInfluence(result).summary_frame()
# print(len(a[a['cooks_d'] > 0.5])) # 0
# print(len(a[a['dffits_internal'] > 0.9])) # 2
# print(a[a['dffits_internal'] > 0.9]) # 30, 32 Phoenix Providence
# print(da['city'][30])
# print(da['city'][32])
#
# stu = a['student_resid']
# condition = (stu < -3) | (stu > 3)
# print(a[condition]) # 1 Providence
#
# y2 = y[city != 'Providence']
# x2 = x[city != 'Providence']
# result2 = sm.OLS(y2,x2).fit()
# print(result.summary(), result2.summary())
# manu, wind
# temp, manu, popul,
#
#
# temp          -0.9833      0.498     -1.973      0.057      -1.997       0.031
# manu           0.0516      0.013      4.004      0.000       0.025       0.078
# popul         -0.0248      0.012     -1.988      0.055      -0.050       0.001
# wind          -3.7941      1.451     -2.615      0.013      -6.746      -0.842
# precip         0.2768      0.293      0.944      0.352      -0.320       0.874
# predays        0.0401      0.131      0.307      0.761      -0.226       0.306


# import pandas as











