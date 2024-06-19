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

# import pandas as pd
# da = pd.read_csv("spb_daily.csv")
#
# # print(da) ['자전거ID', '대여일시', '대여소번호', '대여소명' , '이용시간', '이용거리']
#
# da['시간'] = da['대여일시'].str[-5:-3].copy()
# da['대여소번호'] = da['대여소번호'].copy().str.replace(" ","")
#
# cen = da['대여소번호'].copy()
# tim = da['시간'].copy()
# # da['대여소번호'] = da['대여소번호'].copy().str[0]
#
# print(da['대여소번호'].unique())
#
#
# aa = da.groupby('시간')['이용시간'].sum()
# print(aa.idxmax()) # 18시에 가장 많이 이용
# print(da)
#
# cond1 = (cen.str[0] == "4")
# cond2 = (tim == "18")
# bb = da[cond1 & cond2]
#
# cc = da.groupby('대여소번호')['이용거리'].sum()
# print(cc.idxmax())
# answer = 420
# #
# import pandas as pd
# X_train = pd.read_csv("train_insurance.csv")
# X_test = pd.read_csv("test_insurance.csv")
#
# # print(X_train.columns) ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
# y_train = X_train.copy().drop(['age', 'sex', 'bmi', 'children', 'smoker', 'region'],axis = 1)
# X_train = X_train.copy().drop(columns = 'charges')
#
# # print(X_train.info()) # 결측치는 없음
#
# for i in X_train.columns:
#     # print(i,":",X_train[i].unique(), len(X_train[i].unique()))
#     if X_train[i].dtypes == "object":
#         a = X_train[i].unique()
#         idx = 0
#         tmp = {}
#         for j in a:
#             tmp[j] = idx
#             idx += 1
#         X_train[i] = X_train[i].map(tmp)
#
# for i in X_train.columns:
#     # print(i,":",X_train[i].unique(), len(X_train[i].unique()))
#     if X_test[i].dtypes == "object":
#         a = X_test[i].unique()
#         idx = 0
#         tmp = {}
#         for j in a:
#             tmp[j] = idx
#             idx += 1
#         X_test[i] = X_test[i].map(tmp)
#
# from sklearn.model_selection import train_test_split
#
# for i in X_train.columns:
#     X_train[i] = X_train[i].astype('float64')
#     X_test[i] = X_test[i].astype('float64')
#
# y_train['charges'] = y_train['charges'].copy()
#
# X_tra , X_val, y_tra, y_val = train_test_split(
#     X_train, y_train,
#     random_state = 2323
# )
#
# # print(y_tra.shape)
#
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder as le
# from sklearn.linear_model import LinearRegression as rff
# from sklearn.preprocessing import PolynomialFeatures as pol
#
# # enc = le()
# # y = enc.
# # print(X_tra)
# # print(y_tra)
# rf = pol(degree=3)
# model = rf.fit(X_tra, y_tra)
# pred = model.predict(X_val)
#
# from sklearn.metrics import mean_absolute_percentage_error as MAPE
#
# mape = MAPE(y_val, pred)
# print(mape)
#
# pred_test = model.predict(X_test)
# # print(pred_test.shape)
# # print(pred_test)
#
# # obj = {"pred" : pred_test}
# # result = pd.DataFrame(obj)
# # result.to_csv("result.csv", index=False)
#
# actual = pd.read_csv("insurance_y_test.csv")
# actual = actual['test']
# # print(actual)
#
# print(MAPE(actual, pred_test))


# import pandas as pd
# X_train = pd.read_csv("train_insurance.csv")
# X_test = pd.read_csv("test_insurance.csv")
#
# # print(X_train.columns)
# y_train = X_train.drop(['age', 'sex', 'bmi', 'children', 'smoker', 'region'], axis = 1)
# X_train = X_train.copy().drop('charges',axis = 1)

#
# import pandas as pd
# da = pd.read_csv("satisfy.csv")
# # print(da.columns) ['만족', '성별', '등급']
# dummies = pd.get_dummies(da, ['등급', '성별'],drop_first=True)
#
# tmp = {True : 1 , False : 0}
#
# for i in ['등급_M',   '성별_B',   '성별_S']:
#     dummies[i] = dummies[i].map(tmp)
#
# import statsmodels.api as sm
#
# y = dummies['만족']
# x = dummies.copy().drop(['만족'],axis = 1)
# x = sm.add_constant(x)
#
# result = sm.GLM(y,x,family=sm.families.Binomial()).fit()
# print(result.summary())
#
# answer_a = round(0.0846 , 2)
#
# import numpy as np
# answer_b = round(np.exp(0.0846), 2)
#
# answer_c = result.deviance
#
# stats = result.null_deviance - result.deviance
#
# from scipy.stats import chi2
# pval = 1 - chi2.cdf(stats, 3)
# print(pval)
# answer_d = 0

#
# import pandas as pd
#
# da = pd.read_csv("airpollution.csv")
#
# from statsmodels.stats.outliers_influence import OLSInfluence
# import statsmodels.api as sm
# # print(da)  city  SO2  temp  manu  popul  wind  precip  predays
#
# y = da['SO2']
# x = da.copy().drop(['SO2','city'],axis=1)
# x = sm.add_constant(x)
#
# result = sm.OLS(y,x).fit()
#
# # print(OLSInfluence(result).summary_frame().columns)
# # ['dfb_const', 'dfb_temp', 'dfb_manu', 'dfb_popul', 'dfb_wind',
# #        'dfb_precip', 'dfb_predays', 'cooks_d', 'standard_resid', 'hat_diag',
# #        'dffits_internal', 'student_resid', 'dffits']
# # x = OLSInfluence(y,x)
#
# result = OLSInfluence(result).summary_frame()
# pre_answer = (result['cooks_d'] > 0.5)
# print(result[pre_answer]) # 0
#
# pre_answer = (result['dffits'] > 0.9)
# print(result[pre_answer]) # 2
#
# pre_answer = (result['student_resid'] > 3) | (result['student_resid'] < -3)
# print(result[pre_answer]) # 1
#
# # 32번째 도시를 제거하고 다시 측정할 것
#
# # print(da['city']) Providence
# city = da['city']
#
# y2 = y[city != 'Providence']
# x2 = x[city != 'Providence']
# result = sm.OLS(y,x).fit().summary()
# result2 = sm.OLS(y2,x2).fit().summary()
# print(result, result2)
# # temp manu popul
# # manu wind
#
# answer_d = 1