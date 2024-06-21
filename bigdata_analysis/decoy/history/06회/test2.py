# import pandas as pd
#
# da = pd.read_csv("cancer.csv")

# print(da)
# answer = []
# answer.append(da['x'].isna().sum())
#
# # print(answer)
#
# from scipy.stats import chisquare
# import numpy as np
#
# a = da.value_counts().to_numpy()
# a = np.append(a, answer[0])
# n = da.shape[0]
# b = np.array([0.05,0.05,0.1,0.8]) * n
#
# stat , pval = chisquare(a,b)
#
# answer.append(int(round(stat,0)))
# answer.append(int(round(pval,0)))
#
# print(answer)


# import pandas as pd
# da = pd.read_csv("airquality.csv")
# da = da.copy().dropna()
#
# ind_col = ['Solar.R','Wind','Temp']
# dep_col = ['Ozone']
#
# import statsmodels.api as sm
#
# y = da[dep_col]
# x = da[ind_col]
# x = sm.add_constant(x)
#
# result = sm.OLS(y,x).fit()
# # print(result.summary())
# answer = []
#
# answer.append(round(0.0637,2))
# answer.append(round(2.234,2))
#
# new_da = pd.read_csv("airquality_new.csv")
# new_x = new_da[ind_col]
# new_x = sm.add_constant(new_x)
#
# pred = result.get_prediction(new_x)
# # print(pred.summary_frame().loc[9])
# answer.append(round(91.763178,2))
#
# print(answer)

# import pandas as pd
# da = pd.read_csv("sejong_fire.csv")
#
# # print(da.columns) ['관할서명', '서센터명', '화재구분', '접수일시', '상황종료일시']
# # print(da) 2021-06-21 11:36
#
# from datetime import datetime
#
# da['start'] = da['접수일시'].apply(lambda x : datetime.strptime(x,"%Y-%m-%d %H:%M"))
# da['end'] = da['상황종료일시'].apply(lambda x : datetime.strptime(x,"%Y-%m-%d %H:%M"))
# da['total'] = (round((da['end'] - da['start']).dt.total_seconds() / 60))
# # print(da['total'].idxmax()) 54
# center = da['서센터명']
# aa = da.iloc[54]
# # print(center) 조치원119구조대
#
# answer = da[center == '조치원119구조대']['total'].mean()
# print(int(answer))




# import pandas as pd
# da = pd.read_csv("sejong_fire.csv")
#
# from datetime import datetime
# # print(da.columns) ['관할서명', '서센터명', '화재구분', '접수일시', '상황종료일시']
# # print(da) 2021-06-18 6:47
# da['start'] = da['접수일시'].apply(lambda x : datetime.strptime(x,"%Y-%m-%d %H:%M"))
# da['end'] = da['상황종료일시'].apply(lambda x : datetime.strptime(x,"%Y-%m-%d %H:%M"))
# da['total'] = ((da['end'] - da['start']).dt.total_seconds()) / 60
#
# # print(da['서센터명'].iloc[da['total'].idxmax()]) 조치원119구조대
#
# cen = da['서센터명']
#
# aa = round(da[cen == "조치원119구조대"]['total'].mean())
# print(int(aa))

# import pandas as pd
#
# da = pd.read_csv("busan_school_Info.csv")
# # print(da.columns) ['school_name', 'student_1', 'student_2', 'student_3', 'student_4', 'student_5', 'student_6', 'teacher']
# da['total_student'] = da.iloc[:,1:7].sum(axis=1)
# da['ratio'] = da['total_student'] / da['teacher']
# a = da['ratio'].idxmax()
#
# answer = da['teacher'][a]
# print(answer)

# import pandas as pd
# da = pd.read_csv("five_crime.csv")
# # print(da.columns) ['연월', '살인_발생건수', '살인_검거건수', '강도_발생건수', '강도_검거건수', '강간_강제추행_발생건수',
# #        '강간_강제추행_검거건수', '절도_발생건수', '절도_검거건수', '폭력_발생건수', '폭력_검거건수']
# # print(da)
# import numpy as np
# da['total'] = da.iloc[:,np.arange(1,10,2)].sum(axis=1)
# # print(da['total'].idxmax()) 38
# da['month'] = da['연월'].str[:4]
# # aa = da.groupby('month')['total'].sum().idxmax() 2012
# answer = da[da['month'] == '2012']['폭력_검거건수'].mean()
# print(int(round(answer)))

# import pandas as pd
# import numpy as np
#
# da = pd.read_csv("cancer.csv")
# n = da.copy().shape[0]
# nan = da.isna().sum()
# da = da['x'].value_counts()
#
# aa = da.to_numpy()
# bb = np.append(aa,nan)
#
# cc = np.array([0.05,0.05,0.1,0.8]) * n
#
# answer = []
# answer.append(nan)
#
# from scipy.stats import chisquare
#
# stat, pval = chisquare(bb, cc)
# answer.append(int(round(stat)))
# answer.append(int(round(pval)))
#
# print(answer)

# import pandas as pd
# da = pd.read_csv("airquality.csv")
# da = da.copy().dropna()
#
# ind_col = ['Solar.R','Wind','Temp']
# dep_col = ['Ozone']
#
# import statsmodels.api as sm
#
# y = da[dep_col]
# x = da[ind_col]
# x = sm.add_constant(x)
#
# model = sm.OLS(y,x)
# result = model.fit()
#
# # print(result.summary())
#
# answer = []
# answer.append(round(0.0637,2))
# answer.append(round(2.234,2))
#
# da_new = pd.read_csv("airquality_new.csv")
#
# new_x = da_new[ind_col]
# new_x = sm.add_constant(new_x)
# new_result = result.get_prediction(new_x)
# # print(new_result.summary_frame().iloc[9])
# answer.append(round(91.763178,2))
#
# print(answer)
#
# import pandas as pd
#
# train  = pd.read_csv("Airline_train.csv")
# test   = pd.read_csv("Airline_test.csv")
# y_test = pd.read_csv("Airline_y_test.csv")
#
# y_train = train['Satisfaction'].map({"Yes" : 1,"No":0})
# X_train = train.copy().drop('Satisfaction', axis=1)
# X_test = test
# # y_test = y_test.copy().map({"Satisfied" : 1, "Not satisfied":0})
# # print(y_test, y_train)
# y_test = y_test['Satisfaction'].map({"Satisfied" : 1,"Not satisfied":0})
#
# # print(y_train)
#
# # print(X_train.info()) # 결측치 없음
#
# for i in X_train.columns:
#     if X_train[i].dtype == 'object':
#         a = X_train[i].unique()
#         idx = 0
#         tmp = {}
#         for j in a:
#             tmp[j] = idx
#             idx += 1
#         X_train[i] = X_train[i].copy().map(tmp)
#         X_test[i] = X_test[i].copy().map(tmp)
#
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import f1_score
# from sklearn.ensemble import RandomForestClassifier as rf
#
# X_tr , X_val , y_tr , y_val = train_test_split(
#     X_train, y_train, random_state = 23
# )
#
# rff = rf()
# model = rff.fit(X_tr,y_tr)
# pred = model.predict(X_val)
# score = round(f1_score(y_val, pred)*100 , 4)
# print("F1_score는",score,"점 입니다.")
#
# obj = {"pred" : pred}
# result = pd.DataFrame(obj)
# result.to_csv("result.csv", index = False)
#
#
# real_pred = model.predict(X_test)
# real_score = round(f1_score(y_test, real_pred) * 100 , 4)
# print("F1_score는",real_score,"점 입니다.")






