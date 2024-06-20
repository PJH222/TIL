# import time
#
# timee = time.time()
#
# import pandas as pd
#
# train = pd.read_csv("Flight_train.csv")
# X_test = pd.read_csv("Flight_test.csv")
# y_test = pd.read_csv("Flight_y_test.csv")
#
#
#
# y_train = train['price']
#
# X_train = train.copy().drop(['price','flight', 'duration'],axis=1)
# X_test = X_test.copy().drop(['flight', 'duration'],axis=1)
# y_test = y_test['price']
#
# # print(train.columns) ['airline', 'flight', 'source_city', 'departure_time', 'stops',
# #        'arrival_time', 'destination_city', 'class', 'duration', 'days_left',
# #        'price']
#
# # print(X_train.isna().sum()) # 결측치 없음
# for i in X_train.columns:
#     if X_train[i].dtype == "object":
#         a = X_train[i].unique()
#         idx = 0
#         tmp = {}
#         for j in a:
#             tmp[j] = idx
#             idx += 1
#         X_train[i] = X_train[i].map(tmp)
#         X_test[i] = X_test[i].map(tmp)
#
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier as rf, AdaBoostClassifier as ada
# from sklearn.metrics import mean_squared_error as MSE
# from lightgbm import LGBMClassifier as lgbm
# from xgboost import XGBClassifier as xgb
# X_tr, X_val, y_tr, y_val = train_test_split(
#     X_train, y_train, random_state = 23
# )
#
# rff = rf()
# model = rff.fit(X_tr,y_tr)
# pred = model.predict(X_val)
# score = MSE(y_val, pred, squared = False)
#
# print(score)
# obj = {"pred" : pred}
# result = pd.DataFrame(obj)
# result.to_csv("result.csv")
#
# real_pred = model.predict(X_test)
# score = MSE(y_test, real_pred, squared = False)
# print(score)
#
# print(round(time.time() - timee, 2) , "초 소요되었습니다.")