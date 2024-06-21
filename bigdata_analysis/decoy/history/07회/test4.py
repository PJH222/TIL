# import pandas as pd
#
# da = pd.read_csv("test_score.csv")
# da = da.copy().dropna()
# # print(da.columns) ['연도', '직종', '회차', '일련번호', '과목명', '과목별점수', '총점', '합격여부', '성별', '연령대']
#
#
# da['tmp'] = 1
# # print(da.groupby('연령대')['tmp'].sum()) 20대
# name = da['과목명']
# gen = da['연령대']
#
# condition = (gen == 20) & (name == "기본간호학")
#
# score = da.copy()[condition]
#
# avgg = score['과목별점수'].mean()
# stdd = score['과목별점수'].std()
#
# score['standard'] = (score['과목별점수'] - avgg) / stdd
#
# print(round(score['standard'].max(), 4))

# import pandas as pd
# import numpy as np
# da = pd.read_csv("diabetes.csv")
#
# # corr = da.corr()['progression'].abs().sort_values() bmi
# print(round(da['bmi'].max() , 2))


# import pandas as pd
# da = pd.read_csv("iris.csv")
#
# sep = da['sepal_length']
# q1, q3 = sep.quantile(0.25) , sep.quantile(0.75)
# iqr = q3 - q1
#
# low = q1 - iqr * 1.5
# up = q3 + iqr * 1.5
#
# aa = (sep > up) | (sep < low)
# print(aa.value_counts().min())

# import pandas as pd
#
# da = pd.read_csv("StudentsPerformance.csv")
# da['gender'] = da.copy()['gender'].map({'male':1,'female':0})
#
#
# dd = pd.get_dummies(da,columns=['race'],drop_first = True)
# # dd['gender'] = dd.copy()['gender'].map({'male':1,'female':0})
# for i in dd.columns:
#     if dd[i].dtype == 'bool':
#         dd[i] = dd[i].copy().map({True : 1, False:0})
#         pass
#
# train = dd.copy().iloc[:800]
# test = dd.copy().iloc[800:1000]
#
# y_train = train.copy()['gender']
# X_train = train.copy().drop('gender', axis = 1)
#
# y_test = test.copy()['gender']
# X_test = test.copy().drop('gender', axis = 1)
#
# import statsmodels.api as sm
#
# y = y_train.copy()
# x = X_train.copy()
# # x = sm.add_constant(x)
#
# result = sm.GLM(y,x,family= sm.families.Binomial()).fit()
# # print(result.summary())
#
# import numpy as np
#
# answer = []
# answer.append(round(np.exp(0.3770),2))
# answer.append(466.94)
#
# from sklearn.metrics import accuracy_score as acs
# model =  sm.GLM(y_test,X_test, family=sm.families.Binomial())
# pred = result.predict(X_test)
#
# new_pred = []
# for i in pred:
#     if i > 0.5:
#         new_pred.append(1)
#     else:
#         new_pred.append(0)
#
# aa = acs(y_test,new_pred)
# print(1 - round(aa,2))
#
#
# import pandas as pd
#
# da = pd.read_csv("StudentsPerformance.csv")
# da['gender'] = da['gender'].copy().map({'male':1,'female':0})
#
# da = pd.get_dummies(da.copy(), columns=['race'],drop_first = True)
#
# for i in da.columns:
#     if da[i].dtype == 'bool':
#         da[i] = da[i].copy().map({True:1,False:0})
#
# X_train = da.iloc[:800].copy().drop('gender',axis = 1)
# y_train = da.iloc[:800].copy()['gender']
#
# X_test = da.iloc[800:1000].copy().drop('gender', axis = 1)
# y_test = da.iloc[800:1000].copy()['gender']
#
# import statsmodels.api as sm
#
# result = sm.GLM(y_train, X_train, family = sm.families.Binomial()).fit()
# print(result.summary())
#
# import numpy as np
#
# answer = []
# answer.append(round(np.exp(0.3770), 2))
#
# answer.append(466.94)
#
#
# from sklearn.metrics import accuracy_score as asc
#
#
# pred = result.predict(X_test)
# predd = []
# for i in pred:
#     if i > 0.5:
#         predd.append(1)
#     else:
#         predd.append(0)
#
# score = asc(y_test , predd)
#
# # print(1 - round(score,2))
#
#
# import pandas as pd
#
# da = pd.read_csv("mtcars.csv")
#
# col = ['disp','hp','drat','wt','mpg']
#
# corr = da[col].corr()['mpg'].abs().sort_values()
# # print(corr) #wt
# answer = []
# answer.append(round(0.867659,3))
#
# daa = da[col].copy()
#
# import statsmodels.api as sm
#
# y = daa['mpg']
# x = daa.copy().drop('mpg',axis=1)
# x = sm.add_constant(x)
#
# result = sm.OLS(y,x).fit()
# print(result.summary())
#
# answer.append(round(0.838,3))
# answer.append(round(0.0038,3))
#
# print()
# print(answer)



# import pandas as pd
#
# train = pd.read_csv("Flight_train.csv")
# test = pd.read_csv("Flight_test.csv")
# y_test = pd.read_csv("Flight_y_test.csv")
#
# # print(train)
#
# y_train = train.copy()['price']
# X_train = train.copy().drop(['price','flight'], axis=1)
#
# y_test = y_test.copy()['price']
# X_test = test.copy().drop('flight',axis = 1)
# # print(X_train)
# # print(X_train.info()) # 결측치 없음
# for i in X_train.columns:
#     if X_train[i].dtype == 'object':
#         a = X_train[i].unique()
#         # print(i,":",len(a), X_train[i].dtype) #flight 제거 필요
#         idx = 0
#         tmp = {}
#         for j in a:
#             tmp[j] = idx
#             idx += 1
#         X_train[i] = X_train[i].copy().map(tmp)
#         X_test[i] = X_test[i].copy().map(tmp)
#
#
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error as MSE
# from sklearn.ensemble import RandomForestClassifier as rf
#
# X_tr , X_val , y_tr, y_val = train_test_split(
#     X_train, y_train, random_state = 23
# )
#
# rff = rf()
# model = rff.fit(X_tr,y_tr)
# pred = model.predict_proba(X_val)[:,1]
# score = MSE(y_val, pred) ** 0.5
# print(score)
#
# obj = {'pred' : pred }
# result = pd.DataFrame(obj)
# result.to_csv("result.csv")
#
# real_pred = model.predict_proba(X_test)[:,1]
# real_score = MSE(y_test,real_pred) ** 0.5
# print(real_score)

# 5432.421248975333
# 5540.496739907948


import pandas as pd

da =  pd.read_csv("sejong_fire.csv")

print(da)