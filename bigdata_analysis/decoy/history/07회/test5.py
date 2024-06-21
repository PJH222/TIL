# import pandas as pd
#
# da  = pd.read_csv("StudentsPerformance.csv")
# da['gender'] = da.copy()['gender'].map({'male':1,'female':0})
# da = pd.get_dummies(da.copy(), columns = ['race'],drop_first = True)
#
# # print(da.info())
#
# tmp = {True : 1 , False : 0}
#
# for i in da.columns:
#     if da[i].dtype == 'bool':
#         da[i] = da[i].copy().map(tmp)
#
#
# train = da.iloc[:800].copy()
# test = da.iloc[800:1000].copy()
#
# y = train['gender']
# x = train.copy().drop('gender',axis = 1)
#
# import statsmodels.api as sm
# import numpy as np
# from sklearn.metrics import accuracy_score as ACC
#
# model = sm.GLM(y,x,family = sm.families.Binomial())
# result = model.fit()
# # print(result.summary())
#
# answer = []
# answer.append(round(np.exp(0.3770),2))
# answer.append(round(466.94,2))
# print(answer)
# y_test = test['gender']
# X_test = test.copy().drop('gender',axis = 1)
#
# # print(test)
#
# pred = result.predict(X_test)
# # print(pred)
# predd = []
# for i in pred:
#     if i > 0.5:
#         predd.append(1)
#     else:
#         predd.append(0)
#
#
# score = round(ACC(y_test, predd),2)
# print(1 - score)
#
#

#
# import pandas as pd
# da = pd.read_csv("mtcars.csv")
#
# ind_col = ['disp','hp','drat','wt']
# dep_col = ['mpg']
#
# corrr = da.corr()['mpg'].abs().sort_values() # wt
# # print(corrr)
#
# answer = []
# answer.append(round(0.867659,3))
#
# import statsmodels.api as sm
#
# y = da[dep_col]
# x = da[ind_col]
# x = sm.add_constant(x)
#
# result = sm.OLS(y,x).fit()
# print(result.summary())
#
# answer.append(round(0.838,3))
# answer.append(round(0.0038,3))
#
# print(answer)