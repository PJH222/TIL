import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/전국_종량제봉투_가격표준.csv")
# print(df.columns) '시도명', '시군구명', '종량제봉투종류', '종량제봉투처리방식', '종량제봉투용도', '종량제봉투사용대상', '1L가격',
#        '1.5L가격', '2L가격', '2.5L가격', '3L가격', '5L가격', '10L가격', '20L가격', '30L가격',
#        '50L가격', '60L가격', '75L가격', '100L가격', '120L가격', '125L가격']

# df = df.drop(columns = ['시도명','시군구명','2.5L가격', '3L가격', '5L가격', '10L가격', '20L가격', '30L가격',
#        '50L가격', '60L가격', '75L가격', '100L가격', '120L가격', '125L가격','1L가격',  '1.5L가격','종량제봉투사용대상','종량제봉투처리방식'])
# l22 = df['2L가격']

# df = df[l22 > 0]


# df = df[df["종량제봉투종류"] == "규격봉투"]
# df = df[df['종량제봉투용도'] == "음식물쓰레기"]
# print(int(df['2L가격'].mean()))


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/bmi.csv")

# df['bmi'] = (df['Weight'] / (df['Height']/100)**2)
# bm = df['bmi']
# print(bm)
# cond1 = ((bm >= 18.5 )&(bm < 23))
# cond2 = ((bm >= 23 )&(bm < 25))
# print(df[cond1])
# print(abs(df[cond1].shape[0] - df[cond2].shape[0]))


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/2022_부산초등학교_전출입학생현황.csv")

# print(df.columns)

# df = df.drop(columns = ['설립구분', '1학년전입학생수', '1학년전출학생수', '1학년전체학생수', '2학년전입학생수',
#        '2학년전출학생수', '2학년전체학생수', '3학년전입학생수', '3학년전출학생수', '3학년전체학생수', '4학년전입학생수',
#        '4학년전출학생수', '4학년전체학생수', '5학년전입학생수', '5학년전출학생수', '5학년전체학생수', '6학년전입학생수',
#        '6학년전출학생수', '6학년전체학생수'] , axis = 1)

# df['sum'] = df['전입학생수합계'] - df['전출학생수합계']
# cond = (df['sum'] > 0)
# df = df[cond]
# tmp = df['sum'].argmax()
# print(df.iloc[tmp])

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/carprice_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/carprice_test.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/carprice_y_test.csv")

y_train = x_train['price'].copy()
x_train = x_train.drop(columns = 'price' , axis = 1)

tmp = []

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtype
    # print(b,len(a) , i)
    if b == 'object':
        tmp.append(i)

from sklearn.preprocessing import LabelEncoder as le

lle = le()

for i in tmp:
    a = lle.fit(x_train[i])
    x_train[i] = a.transform(x_train[i])
    x_test[i] = a.transform(x_test[i])


from sklearn.model_selection import train_test_split as tts

x , x_val , y , y_val = tts(x_train, y_train, random_state = 1234 , test_size = 0.2 )

from sklearn.ensemble import RandomForestRegressor as rff
from xgboost import XGBRegressor as xgg
from lightgbm import LGBMRegressor as lgg
from sklearn.metrics import root_mean_squared_error as rmse

rf , xg , lg = rff() , xgg() , lgg()
rf_model , xg_model , lg_model = rf.fit(x,y) , xg.fit(x,y) , lg.fit(x,y)
rf_pred , xg_pred ,lg_pred = rf_model.predict(x_val),xg_model.predict(x_val),lg_model.predict(x_val)
rf , xg , lg = rmse(y_val , rf_pred),rmse(y_val , xg_pred),rmse(y_val , lg_pred)

print(rf , xg , lg)

pred = xg_model.predict(x_test)
obj = {"pred" : pred}
result = pd.DataFrame(obj)

result.to_csv("result.csv" , index = False)

real = rmse(y_test , pred)
print(real)


