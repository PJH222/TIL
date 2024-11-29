import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/test_score.csv")
# print(df)
# df = df.dropna()
# for i in df.columns:
#     a = df[i].unique()
#     b = df[i].value_counts()
#     # print(b , i)

# # 20 대가 가장 많음
# ge = df['연령대']
# gr = df['과목명']
# sc = df['과목별점수']

# cond1 = (ge == 20)
# cond2 = (gr == "기본간호학")
# tmp = (df[cond1 & cond2]['과목별점수'])
# tmp = tmp.dropna()
# aa = tmp.mean()
# bb = tmp.std()
# tmp['a'] = (tmp.copy() - aa) / bb

# t = tmp['a'].argmax()
# print(tmp['a'].iloc[t])

# answer = round(tmp['a'].iloc[t] , 4)
# print(answer)

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/diabetes.csv")

# print(df.corr()['progression'].sort_values())

# tmp = (df['bmi'].argmax())
# answer = (df['bmi'].iloc[tmp])
# print(df['bmi'])

# print(round(answer , 2))

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/iris.csv")

# print(df.columns)

# se = df['sepal_length']
# iqr = se.quantile(.75) - se.quantile(.25)
# q1 = se.quantile(.25)
# q3 = se.quantile(.75)

# cond = ((se > q3 + 1.5 * iqr) | (se < q1 - 1.5 * iqr))

# print(se[cond].shape)


x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/Flight_train.csv")
# x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/Flight_test.csv")
# y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/Flight_y_test.csv")

# y_train = x_train['price'].copy()
# x_train = x_train.copy().drop(columns = 'price' , axis = 1)

# x_train = x_train.drop(columns = 'flight' , axis = 1)
# x_test = x_test.drop(columns = 'flight' , axis = 1)
# tmp = []
# for i in x_train.columns:
#     a = x_train[i].unique()
#     b = x_train[i].dtype
#     # print(b, len(a) , i)
#     if b == 'object':
#         tmp.append(i)
#     # flight 제거

# from sklearn.preprocessing import LabelEncoder as le

# lle = le()

# for i in tmp:
#     a = lle.fit(x_train[i])
#     x_train[i] = a.transform(x_train[i])
#     x_test[i] = a.transform(x_test[i])


# from sklearn.model_selection import train_test_split as tts

# x , x_val , y , y_val = tts(x_train, y_train, random_state = 1234 , test_size = 0.2)

# from sklearn.ensemble import RandomForestRegressor as rff
# from xgboost import XGBRegressor as xgg
# from lightgbm import LGBMRegressor as lgg
# from sklearn.metrics import root_mean_squared_error as rmse

# rf , xg , lg = rff(),xgg(),lgg()
# rf,xg,lg = rf.fit(x,y),xg.fit(x,y),lg.fit(x,y)
# rf_pred,xg_pred,lg_pred = rf.predict(x_val),xg.predict(x_val),lg.predict(x_val)
# rf_score,xg_score,lg_score = rmse(y_val, rf_pred),rmse(y_val, xg_pred),rmse(y_val, lg_pred)
# print(rf_score,xg_score,lg_score)

# pred = lg.predict(x_test)
# obj = {"pred" : pred}
# result = pd.DataFrame(obj)

# result.to_csv("result.csv" , index = False)

# score = rmse(y_test , pred)
# print(score)

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/StudentsPerformance.csv")
# df = pd.get_dummies(df, columns = ['race'], drop_first = True)
# print(df)

# df['gender'] = df['gender'].map({"male" : 1 , "female" : 0})

# tmp = []
# for i in df.columns:
#     a = df[i].dtype
#     if a == 'bool':
#         tmp.append(i)

# for i in tmp:
#     df[i] = df[i].map({True : 1 , False : 0})

# train = df.iloc[:800]
# test = df.iloc[800:1000]

# import statsmodels.api as sm

# y = train['gender']
# x = train.drop(columns = 'gender' , axis = 1)

# a = sm.GLM(y,x,family = sm.families.Binomial())
# b = a.fit()
# print(b.summary())

# answer1 = round(np.exp(0.3770) , 2)
# print(answer1)

# answer2 = round(466.94 , 2)
# print(answer2)
# y_test = test['gender']
# x_test = test.drop(columns = 'gender' , axis = 1)
# c = b.get_prediction(x_test)

# a = np.where(c.summary_frame()['mean'] > 0.5 , 1, 0)

# from sklearn.metrics import accuracy_score as ass

# answer = 1 - ass(y_test , a)
# print(round(answer , 2))

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/mtcars.csv")

print(df.corr()['mpg'].sort_values(ascending = False))

tmp = ['disp','hp','drat','wt','mpg']
df = df[tmp]

import statsmodels.api as sm

y = df['mpg']
x = df.drop(columns = 'mpg', axis = 1)
x = sm.add_constant(x)

a = sm.OLS(y,x).fit()
print(a.summary())
answer = 0.838
print(answer)

answer2 = round(0.0038 , 3)
print(answer2)
