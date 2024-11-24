import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/04회/bodyPerfor_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/04회/bodyPerfor_test.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/04회/bodyPerfor_class.csv")

y_train = x_train.copy()["class"]
x_train = x_train.drop(columns = ["class","id"], axis = 1)
x_test = x_test.drop(columns = ["id"], axis = 1)

y_train = y_train.map({"A":0 , "B":1 , "C":2 , "D":3 })

# 결측치 없음
# print(x_train.info())
# print(x_test.info())

x_train["gender"] = x_train["gender"].map({"M" : 1, "F" : 0})
x_test["gender"] = x_test["gender"].map({"M" : 1, "F" : 0})


from sklearn.model_selection import train_test_split as tts

x , x_val , y , y_val = tts(x_train, y_train, random_state = 1234 , test_size = 0.2, stratify = y_train)


from sklearn.ensemble import RandomForestClassifier as rf
from xgboost import XGBClassifier as xgb

rff = rf()
xg = xgb()

rf_model = rff.fit(x,y)
xgb_model = xg.fit(x,y)

rf_pred = rf_model.predict(x_val)
xgb_pred = xgb_model.predict(x_val)


from sklearn.metrics import f1_score as f1

rf_f1 = f1(y_val, rf_pred, average = "macro")
xgb_f1 = f1(y_val, xgb_pred, average = "macro")

print(rf_f1 , xgb_f1)

pred = xgb_model.predict(x_test)

obj = {"class" : pred}
result = pd.DataFrame(obj)

result["class"] = result["class"].map({0 : "A", 1 : "B", 2 : "C", 3 : "D"})
result.to_csv("result.csv", index = False)

y_test["class"] = y_test["class"].map({"A":0 , "B":1 , "C":2 , "D":3 })

actual_f1 = f1(y_test["class"], pred, average = "macro")
print(actual_f1)


