# import pandas as pd
#
# da = pd.read_csv("Cars93.csv")
#
# # print(da.columns) Turn_circle
# tur = da['Turn_circle']
#
# # q1 = tur.quantile(0.25)
# # q2 = tur.quantile(0.5)
# #
# # answer_b = abs(q2 - q1)
# # print(int(answer_b))
#
#
# import pandas as pd
#
# da = pd.read_csv("facebook_subset.csv")
#
# # print(da.columns)
#
# da['ratio'] = da['mobile_likes_received'] / (da['mobile_likes_received'] + da['www_likes_received'])
#
# rat = da['ratio']
# gen = da['gender']
#
# cond1 = (rat > 0.6) & (rat < 0.7)
# cond2 = (gen == 'male')
# # print(gen)
# print(len(da[cond1 & cond2]))

# import pandas as pd
#
# da = pd.read_csv("netflix_subset.csv")
#
# # print(da.info())
#
# # for i in da.columns:
# #     a = da[i].unique()
# #     print(i,":",len(a))
#
# # print(da[['release_year','date_added','duration']])
# da['month'] = da['date_added'].str[3:6]
# mon = da['month']
# yea = da['release_year']
# lis = da['listed_in']
#
# condition = (mon == 'Jan') & (yea == 2021)
# idx = 0
# idx_list = []
# for i in lis:
#     if "Dramas" in i:
#         idx_list.append(idx)
#         idx += 1
#         # print(1)
#
# aa = da[condition].index()
# print(aa)


# import pandas as pd
#
# train = pd.read_csv("bodyPerfor_train.csv")
# test = pd.read_csv("bodyPerfor_test.csv")
# y_train = train['class']
# X_train = train.drop(['class','id'],axis=1)
#
# X_test = test.drop(['id'],axis=1)
# # print(test)
#
#
# y_test = pd.read_csv("bodyPerfor_class.csv")
# y_test = y_test['class']
# # print(y_test)
# # print(train.info()) # 결측치 없음
#
# for i in X_train.columns:
#     if X_train[i].dtype == 'object':
#         a = X_train[i].unique()
#     # print(i,":",len(a),",",train[i].dtype) #id는 없애야함
#         idx = 0
#         tmp = {}
#         for j in a:
#             tmp[j] = idx
#         X_train[i] = X_train[i].map(tmp)
#         X_test[i] = X_test[i].map(tmp)
#
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier as rf
# from sklearn.metrics import f1_score as F1
#
# X_tr , X_val , y_tr , y_val = train_test_split(
#     X_train, y_train , random_state = 23
# )
#
# rff = rf()
# model = rff.fit(X_tr,y_tr)
# pred = model.predict(X_val)
# score = F1(y_val, pred , average = 'macro')
#
# print(score)
# obj = {"class" : pred}
# result = pd.DataFrame(obj)
#
# result.to_csv("result.csv")
#
# real_pred = model.predict(X_test)
# real_score = F1(y_test,real_pred, average ='macro')
#
# print(real_score)


