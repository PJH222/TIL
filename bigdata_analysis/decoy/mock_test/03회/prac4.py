import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/train_insurance.csv")
# # x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/test_insurance.csv")
# # # print(x_train.columns)
# # y_train = x_train['charges']

# # y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/insurance_y_test.csv")

# # x_train = x_train.copy().drop(columns = 'charges' , axis = 1)

# # tmp = []

# # for i in x_train.columns:
# #     a = x_train[i].unique()
# #     b = x_train[i].dtype
# #     c = x_train[i].isna().sum()
# #     print(b,len(a),i,c)
# #     if b == 'object':
# #         tmp.append(i)

# # from sklearn.preprocessing import LabelEncoder as le

# # lle = le()

# # for i in tmp:
# #     a = lle.fit(x_train[i])
# #     x_train[i] = a.transform(x_train[i])
# #     x_test[i]  = a.transform(x_test[i])


# # from sklearn.model_selection import train_test_split as tts

# # x , x_val , y , y_val = tts(x_train, y_train, test_size = 0.2, random_state = 1234)

# # from sklearn.ensemble import RandomForestRegressor as rff
# # from xgboost import XGBRegressor as xgg
# # from lightgbm import LGBMRegressor as lgg
# # from sklearn.metrics import mean_absolute_percentage_error as mape

# # rf , xg , lg = rff(), xgg(), lgg()
# # rf_model , xg_model, lg_model = rf.fit(x,y) , xg.fit(x,y), lg.fit(x,y)
# # rf_pred , xg_pred, lg_pred = rf_model.predict(x_val), xg_model.predict(x_val) , lg_model.predict(x_val)
# # rf_score, xg_score, lg_score = mape(y_val, rf_pred) , mape(y_val , xg_pred) , mape(y_val , lg_pred)
# # print(rf_score, xg_score, lg_score)

# # pred = rf_model.predict(x_test)
# # obj = {"pred" : pred}
# # result = pd.DataFrame(obj)
# # result.to_csv("result.csv" , index = False)

# # actual_score = mape(y_test , pred)
# # print(actual_score)

# df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/satisfy.csv")

# # df = pd.get_dummies(df,columns = ['성별','등급'],drop_first = True)

# # # print(df)

# # for i in df.columns:
# #     a = df[i].dtype
# #     if a == 'bool':
# #         df[i] = df[i].map({True : 1 , False : 0})

# # import statsmodels.api as sm

# # y = df['만족']
# # x = df.drop(columns = '만족', axis = 1)
# # x = sm.add_constant(x)

# # a = sm.GLM(y,x,family = sm.families.Binomial())
# # b = a.fit()
# # print(b.summary())

# # answer1 = round(0.0846 , 2)
# # print(answer1)

# # answer2 = round(np.exp(0.0846) , 2)
# # print(answer2)

# # answer3 = 3256.0
# # print(answer3)

# # answer4 = 0
# # print(answer4)

# df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/airpollution.csv")

# import statsmodels.api as sm
# from statsmodels.stats.outliers_influence import OLSInfluence as oi

# ci = df.copy()['city']
# df = df.drop(columns = 'city' , axis = 1)
# y = df['SO2']
# x = df.drop(columns = 'SO2' , axis = 1)
# x = sm.add_constant(x)

# model = sm.OLS(y,x).fit()

# print(oi(model).summary_frame())

# cond = (oi(model).summary_frame()['cooks_d'] > 0.5)
# print(cond.value_counts())

# answer1 = 0
# print(answer1)

# cond = (oi(model).summary_frame()['dffits'] > 0.9)
# # print(cond.value_counts())
# answer2 = 2
# print(answer2)

# cond = ((oi(model).summary_frame()['standard_resid'] > 3) | ((oi(model).summary_frame()['standard_resid'] < -3)))
# # print(cond.value_counts())
# answer3 = 1
# print(answer3)


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/economics.csv")

# # print(df.columns) ['데이터수집월', '개인소비지출_십억달러', '총인구_천명', '개인저축률', '중앙_실업기간_주', '실업자수_천명']
# # print(df['데이터수집월'].unique())
# df['실업자수_천명'] = df['실업자수_천명'] / 10
# df['데이터수집월'] = df['데이터수집월'].str.replace(' ','')
# df['year'] = df['데이터수집월'].str[:4]
# df['month'] = df['데이터수집월'].str[5:7]

# a = df.groupby(['year'])['실업자수_천명'].mean().idxmax()
# print(a)

# # a = df.groupby(['year','month'])['실업자수_천명'].value_counts()
# # print(a)

# tmp = df['실업자수_천명']
# answer = round(df['실업자수_천명'][df['year'] == a].var() , 2)
# print(answer)

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/Airline.csv")

# # print(df.columns) ['Gender', 'Ages', 'Customer_Type', 'Class',
# #        'Departure_Delay_in_Minutes', 'Arrival_Delay_in_Minutes']

# for i in df.columns:
#     # print(i , df[i].unique())
#     print()
# ag = df['Ages'].copy()

# tmp = (ag == "[10, 20)")
# ag[tmp] = "10_19"
# tmp = (ag == "[40, 50)")
# ag[tmp] = "40_49"
# tmp = (ag == "[50, 60)")
# ag[tmp] = "50_59"
# tmp = (ag == "[20, 30)")
# ag[tmp] = "20_29"
# df['Ages'] = ag.copy()

# tmp = df.groupby('Ages')['Departure_Delay_in_Minutes'].mean().idxmax()
# print(tmp)

# cond1 = (df['Ages'] == tmp)
# cond2 = (df['Customer_Type'] == "L")

# result = df[cond1 & cond2]
# print(result.shape[0])


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/satisfy.csv")
# print(df.columns)
# print(df)

# df = pd.get_dummies(df , columns = ['성별','등급'], drop_first = True)

# for i in df.columns:
#     a = df[i].dtype
#     if a == 'bool':
#         df[i] = df[i].map({True : 1 , False : 0})

# import statsmodels.api as sm

# y = df['만족']
# x = df.copy().drop(columns = '만족', axis = 1)
# x = sm.add_constant(x)

# model = sm.GLM(y,x , family = sm.families.Binomial()).fit()
# print(model.summary())

# answer1 = round(0.0846 , 2)
# print(answer1)

# answer2 = round(np.exp(0.0846) , 2)
# print(answer2)

# answer3 = 3256.0
# print(answer3)



df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/airpollution.csv")

# print(df.columns) ['city', 'SO2', 'temp', 'manu', 'popul', 'wind', 'precip', 'predays']

ci  = df['city'].copy()

from statsmodels.stats.outliers_influence import OLSInfluence as ol
import statsmodels.api as sm


y = df['SO2']
x = df.copy().drop(columns = ['city','SO2'], axis = 1)
x = sm.add_constant(x)

model = sm.OLS(y,x).fit()
# print((ol(model).summary_frame()['cooks_d'] > 0.5).value_counts())
answer1 = 0
# print(ol(model).summary_frame().columns) ['dfb_const', 'dfb_temp', 'dfb_manu', 'dfb_popul', 'dfb_wind',
#        'dfb_precip', 'dfb_predays', 'cooks_d', 'standard_resid', 'hat_diag',
#        'dffits_internal', 'student_resid', 'dffits']

# print((ol(model).summary_frame()['dffits'] > 0.9).value_counts())
answer2 = 2

cond = (ol(model).summary_frame()['dffits'] > 0.9)
# print(ci[cond]) 30       Phoenix, Providence
a = ((ol(model).summary_frame()['standard_resid'] > 3) | (ol(model).summary_frame()['standard_resid'] < -3))
# print(a.value_counts())
answer3 = 1

cond = (ol(model).summary_frame()['standard_resid'] > 3) | (ol(model).summary_frame()['standard_resid'] < -3)
# print(ci[cond])  Providence

tmp = (~(ci == 'Providence'))

print(model.summary())


x['city'] = ci
x = x[tmp]
y = y[tmp]
x = x.drop(columns = 'city' , axis = 1)

model = sm.OLS(y,x).fit()
print(model.summary())


'''
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        111.7285     47.318      2.361      0.024      15.567     207.890
temp          -1.2679      0.621     -2.041      0.049      -2.530      -0.006
manu           0.0649      0.016      4.122      0.000       0.033       0.097
popul         -0.0393      0.015     -2.595      0.014      -0.070      -0.009
wind          -3.1814      1.815     -1.753      0.089      -6.870       0.507
precip         0.5124      0.363      1.412      0.167      -0.225       1.250
predays       -0.0521      0.162     -0.321      0.750      -0.381       0.277

                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         95.7709     37.826      2.532      0.016      18.813     172.729
temp          -0.9833      0.498     -1.973      0.057      -1.997       0.031
manu           0.0516      0.013      4.004      0.000       0.025       0.078
popul         -0.0248      0.012     -1.988      0.055      -0.050       0.001
wind          -3.7941      1.451     -2.615      0.013      -6.746      -0.842
precip         0.2768      0.293      0.944      0.352      -0.320       0.874
predays        0.0401      0.131      0.307      0.761      -0.226       0.306
'''