# import pandas as pd
#
# da = pd.read_csv("test_score.csv")
# # print(da.columns) ['연도', '직종', '회차', '일련번호', '과목명', '과목별점수', '총점', '합격여부', '성별', '연령대']
# # print(da['연령대'].unique())
# # a = da.isna().sum() > 0
# # print(a) 회차 과목별점수 총점 합격여부
#
# da = da.copy().dropna()
# # da['tmp'] = 1
# # a = da.groupby('연령대')['tmp'].sum()
# # print(a) # 20대가 가장 많음
#
# age = da['연령대']
# aca = da['과목명']
#
# # da['std'] = (da['과목별점수'] - avgg) / stdd
# cond = (age == 20) & (aca == '기본간호학')
#
# aa = da[cond].copy()
# avgg = aa['과목별점수'].mean()
# stdd = aa['과목별점수'].std()
#
# aa['std'] = (aa['과목별점수'] - avgg) / stdd
# answer = round(aa['std'].max(),4)
# print(answer)
#
# import pandas as pd
#
# da = pd.read_csv("diabetes.csv")
# # print(da.columns) ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6',
# #        'progression']
#
# # a = da.corr()
# # print(a)
#
# max_name = ''
# max_num = 0
#
# a = da.corr()['progression']
# # print(a)
# maxx = 0
# maxx_idx = 0
# print(a)
# for i in range(len(a)):
#     if a[i] != 1.0 and a[i] > maxx:
#         maxx = a.iloc[i]
#         maxx_idx = i
# # bmi
# print(round(da['bmi'].max() , 2))


# import pandas as pd
#
# da = pd.read_csv("iris.csv")
# # print(da) sepal_length 의 이상치 개수
#
# q1, q3  = da['sepal_length'].quantile(0.25) , da['sepal_length'].quantile(0.75)
# stdd = da['sepal_length'].std()
#
# loww = q1 - stdd * 1.5
# uppe = q3 + stdd * 1.5
#
# sep = da['sepal_length']
# condition = (sep < loww) | (sep > uppe)
#
# print(len(da[condition]))
# print(5)

# import pandas as pd
#
# da = pd.read_csv("iris.csv")
#
# # print(da.isna().sum())
# print(da.info())
# for i in da.columns:
#     if da[i].isna().sum() > 0 :
#         med = da[i].median()
#         da[i] = da[i].fillna(med)
#
# sep = da['sepal_length']
#
# q1 = sep.quantile(0.25)
# q3 = sep.quantile(0.75)
# iqr = q3 - q1
#
# condition = (sep > q3 + 1.5 * iqr) | (sep < q1 - 1.5 * iqr)
# print(len(da[condition]))
#
# import time
# import pandas as pd
# aaaa = time.time()
# X_train = pd.read_csv("Flight_train.csv")
# X_test = pd.read_csv("Flight_test.csv")
# y_train = X_train.copy().drop(['airline', 'flight', 'source_city', 'departure_time', 'stops', 'arrival_time', 'destination_city', 'class', 'duration', 'days_left'], axis = 1)
# y_test = pd.read_csv("Flight_y_test.csv")
# # print(X_train.columns)
# # print(X_train.isna().sum()) # 결측치는 없음
# # ['airline', 'flight', 'source_city', 'departure_time', 'stops',
# #        'arrival_time', 'destination_city', 'class', 'duration', 'days_left',
# #        'price']
# # for i in X_train.columns:
# #     print(i, len(X_train[i].value_counts())) #  flight duration 지워야 함
#
# X_train = X_train.copy().drop(['flight', 'duration','price'], axis = 1)
# X_test = X_test.copy().drop(['flight', 'duration'], axis = 1)
#
# for i in X_train.columns:
#     a = X_train[i].unique()
#     # print(i,":",a,len(a), X_train[i].dtype)
#     if X_train[i].dtype == "object":
#         idx = 0
#         tmp = {}
#         for j in a:
#             tmp[j] = idx
#             idx += 1
#         # for k in tmp:
#         #     tmp[k] = tmp[k] / idx
#
#         X_train[i] = X_train[i].map(tmp)
#         X_test[i] = X_test[i].map(tmp)
# # for i in X_test.columns:
# #     a = X_test[i].unique()
# #     # print(i,":",a,len(a), X_train[i].dtype)
# #     if X_test[i].dtype == "object":
# #         idx = 0
# #         tmp = {}
# #         for j in a:
# #             tmp[j] = idx
# #             idx += 1
# #         # for k in tmp:
# #         #     tmp[k] = tmp[k] / idx
# #         X_test[i] = X_test[i].map(tmp)
#
# # print(X_train)
#
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
# from lightgbm import LGBMClassifier
#
# X_tra, X_val , y_tra, y_val = train_test_split(
#     X_train, y_train, random_state = 23
# )
#
# rf = RandomForestClassifier()
# model = rf.fit(X_tra,y_tra)
# score = model.predict(X_val)
#
# from sklearn.metrics import mean_squared_error as MAE
#
# mae = MAE(y_val,score,squared=False)
# print(mae,"예측 점수")
#
# pred = model.predict(X_test)
# score = MAE(y_test, pred, squared=False)
# print(score,"실제 점수")
#
# print(time.time() - aaaa,"초")

# import pandas as pd
#
# da = pd.read_csv("StudentsPerformance.csv")
#
# tmp = {"male" : 1, "female" : 0}
#
# da['gender'] = da['gender'].copy().map(tmp)
# # print(da.info())
# # print(da)
#
# import statsmodels.api as sm
#
# # X_train, X_test = da.iloc[:800], da.iloc[800:]
#
# # y = da['gender']
# # x = da.copy().drop('gender',axis=1)
# # x = sm.add_constant(x)
#
# da = pd.get_dummies(da,['race'],drop_first = True )
#
# X_train, test = da.iloc[:800], da.iloc[800:1000]
# y_train = X_train['gender']
# # print(da)
# y = y_train
# x = X_train.copy().drop('gender',axis=1)
# # x = sm.add_constant(x)
#
# tmp = {True:1,False:0}
# for i in x.columns:
#     if x[i].dtype != 'int64':
#         x[i] = x[i].map(tmp)
# # x = x.map(tmp)
# import numpy as np
# print(round(np.exp(0.3770),2))
#
# aaa = sm.GLM(y,x,family = sm.families.Binomial()).fit()
# print(aaa.summary())
#
# print(round(466.94,2))
#
# from sklearn.metrics import accuracy_score
#
# y_test = test['gender']
# X_test = test.drop('gender',axis = 1)
#
# for i in X_test.columns:
#     if X_test[i].dtype != 'int64':
#         X_test[i] = X_test[i].map(tmp)
#
# print(X_test, y_test)
#
# pred = aaa.predict(X_test)
# label = np.where(pred > 0.5 , 1, 0)
#
# result = accuracy_score(y_test,label)
# print(round(1 - result , 2))


# import pandas as pd
#
# da = pd.read_csv("mtcars.csv")
# col = ['disp', 'hp', 'drat', 'wt', 'mpg']
#
# df = da[col]
# corr = df.corr()['mpg'].abs() # wt
# # print(corr)
# answer_a = 0.867659
# print(round(0.867659,3))
#
# import statsmodels.api as sm
#
# y = df['mpg']
# x = df.copy().drop('mpg', axis = 1)
# x = sm.add_constant(x)
#
# result = sm.OLS(y,x).fit()
# # print(result.summary())
#
# answer_b = 0.838
# print(round(0.838, 3))
#
# print(round(0.0038,3))

