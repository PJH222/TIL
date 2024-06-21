# import time
# timee = time.time()
#
# import pandas as pd
#
# train = pd.read_csv("carprice_train.csv")
# test = pd.read_csv("carprice_test.csv")
# y_test = pd.read_csv("carprice_y_test.csv")
#
# y_train = train['price']
# X_train = train.copy().drop('price',axis = 1)
# y_test = y_test['price']
# X_test = test
# # print(y_test['price'])
# # print(train.isna().sum()) # 결측치 없음
#
# b = time.time()
# for i in X_train.columns:
#     if X_train[i].dtype == 'object':
#         a = X_train[i].unique()
#         idx = 0
#         tmp = {}
#         for j in a:
#             tmp[j] = idx
#             idx += 1
#         X_train[i] = X_train[i].map(tmp)
#         X_test[i] = X_test[i].map(tmp)
#     # print(i,":",len(a),"   ",X_train[i].dtype)
# print(round(time.time() - b, 2),"map 실행시, 소요시간")
#
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier as rf
# from sklearn.metrics import mean_squared_error as MSE
#
# X_tr , X_val , y_tr , y_val = train_test_split(
#     X_train,y_train, random_state = 23
# )
# # print(timee)
# rff = rf(n_estimators = 50)
# b = time.time()
# model = rff.fit(X_tr,y_tr)
# print(round(time.time() - b, 2),"fit 실행시, 소요시간")
# # print(timee)
# pred = model.predict(X_val)
# score = MSE(y_val,pred) ** 0.5
#
# print("RMSE :",score)
#
# obj = {"pred" : pred}
#
# result = pd.DataFrame(obj)
# result.to_csv("result.csv",index = False)
#
# real_pred = model.predict(X_test)
# real_score = MSE(y_test, real_pred) ** 0.5
#
# print("RMSE :",real_score)
# print(round(time.time() - timee, 3),"초 소요 되었습니다.")

