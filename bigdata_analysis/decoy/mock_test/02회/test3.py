# import pandas as pd
# import time
# timee = time.time()
#
# X_train = pd.read_csv("BlackFriday_X_train.csv")
# y_train = pd.read_csv("BlackFriday_y_train.csv")
# X_test = pd.read_csv("BlackFriday_X_test.csv")
# y_test = pd.read_csv("BlackFriday_y_test.csv")
# # print(X_train.info()) Product_Category_2 Product_Category_3 제거 필요
#
# del_col = ['Product_Category_2', 'Product_Category_3','User_ID', 'Product_ID']
#
# X_train, X_test = X_train.copy().drop(del_col,axis=1), X_test.copy().drop(del_col,axis=1)
# # print(X_train.head())
# # print(X_train.info())
#
# y_train , y_test = y_train['Purchase'] , y_test['Purchase']
# # print(y_train)
#
# for i in X_train.columns:
#     if X_train[i].dtype == 'object':
#         a = X_train[i].unique()
#         idx = 0
#         tmp = {}
#
#         for j in a:
#             tmp[j] = idx
#             idx += 1
#         for k in tmp:
#             tmp[k] = tmp[k] / idx
#         # print(tmp)
#         X_train[i] = X_train[i].copy().map(tmp)
#         X_test[i] = X_test[i].copy().map(tmp)
#
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import mean_absolute_error as MAE
#
# X_tr , X_val , y_tr, y_val = train_test_split(
#     X_train, y_train, random_state = 23
# )
#
# rf = RandomForestClassifier()
# model = rf.fit(X_tr,y_tr)
# pred = model.predict(X_val)
# score = MAE(y_val, pred)
#
# # print(pred)
# print(score, "예측 점수")
#
# obj = {"Purchase" : pred}
# result = pd.DataFrame(obj)
# result.to_csv("result.csv")
#
# real_pred = model.predict(X_test)
# real_score = MAE(y_test,real_pred)
# print(real_score, "실제 점수")
#
# print(round(time.time() - timee , 2),"초 소요")