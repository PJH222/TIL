import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/sejong_fire.csv")

# df['소요시간'] = (pd.to_datetime(df['상황종료일시']) - pd.to_datetime(df['접수일시']))
# maxx = df['소요시간'].max()

# tmp = df[df['소요시간'] == maxx].index
# print(df.iloc[tmp]) 

# se = df['서센터명']
# cond = (se == '조치원119구조대')
# print(df['소요시간'][cond].mean())

# answer = 1 * 24 * 60 + 2 * 60 + 13
# print(answer)


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/busan_school_Info.csv")
# df['sum'] = 
# print(df.columns) ['school_name', 'student_1', 'student_2', 'student_3', 'student_4',
#        'student_5', 'student_6', 'teacher']
# df['sum'] = df['student_1']+ df['student_2']+ df['student_3']+ df['student_4']+df['student_5']+ df['student_6']
# df['ratio'] =  df['sum'] / df['teacher']
# tmp = df['ratio'].argmax()
# tmp2 = df['school_name'][df['ratio'].argmax()]
# print(tmp2)
# print(df.iloc[tmp])

# answer = 7
# print(answer)

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/five_crime.csv")
# ['연월', '살인_발생건수', '살인_검거건수', '강도_발생건수', '강도_검거건수', '강간_강제추행_발생건수',
#        '강간_강제추행_검거건수', '절도_발생건수', '절도_검거건수', '폭력_발생건수', '폭력_검거건수']

# df['연월'] = df['연월'].str.replace(' ','')

# # for i in df.columns:
# #     print(df[i].unique())

# df['year'] = df['연월'].str[:4]
# df['month'] = df['연월'].str[5:7]
# df['sum'] = df['살인_발생건수'] +   df['강도_발생건수']   +df['강간_강제추행_발생건수']+    df['절도_발생건수']    +df['폭력_발생건수']  

# tmp = df.groupby('year')['sum'].mean().idxmax()
# answer = df['폭력_발생건수'][df['year'] == tmp].mean()
# print(int(answer))


x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/Airline_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/Airline_test.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/Airline_y_test.csv")

y_train = x_train['Satisfaction'].copy()
x_train = x_train.drop(columns = 'Satisfaction' , axis = 1)
# print(y_train, y_test)

y_train = y_train.map({"Yes" : 1 , "No" : 0})
y_test = y_test['Satisfaction'].map({"Satisfied" : 1 , "Not satisfied" : 0})
# print(x_train.columns)

# print(x_train.info(), x_test.info(), y_train.info())
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

x , x_val, y , y_val = tts(x_train, y_train, random_state = 1234 , test_size = 0.2, stratify = y_train)

from sklearn.ensemble import RandomForestClassifier as rff
from xgboost import XGBClassifier as xgg
from lightgbm import LGBMClassifier as lgg
from sklearn.metrics import f1_score as f1

rf , xg , lg = rff(),xgg(),lgg()
rf,xg,lg = rf.fit(x,y),xg.fit(x,y),lg.fit(x,y)
rf_model,xg_model,lg_model = rf.predict(x_val),xg.predict(x_val),lg.predict(x_val)
rf1,xg1,lg1 = f1(y_val, rf_model),f1(y_val, xg_model),f1(y_val, lg_model)

print(rf1,xg1,lg1)

real = lg.predict(x_test)
# real = real.map({1 : "Satisfied" , 0 : "Not satisfied"})
obj = {"pred" : real}
print(real)
result = pd.DataFrame(obj)
# print(result)
result = result["pred"].map({1 : "Satisfied" , 0 : "Not satisfied"})

result.to_csv("result.csv" , index = False)

tmp = f1(y_test , real)
print(tmp)
