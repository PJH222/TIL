# # import pandas as pd
# # from datetime import datetime,timedelta
# #
# # da = pd.read_csv("sejong_fire.csv")
# #
# # # print(da.columns) ['관할서명', '서센터명', '화재구분', '접수일시', '상황종료일시']
# #
# # # print(da.iloc[54]) 조치원119구조대
# # # 2021-06-18 6:47
# # # print(da['접수일시'])
# # da['start'] = da['접수일시'].apply(lambda x: datetime.strptime(x,"%Y-%m-%d %H:%M"))
# # da['end'] = da['상황종료일시'].apply(lambda x: datetime.strptime(x,"%Y-%m-%d %H:%M"))
# # da['diff'] = round((da['end'] - da['start']).dt.total_seconds() / 60)
# #
# # cen = da['서센터명']
# # dif = da['diff']
# #
# # cond1 = (cen == "조치원119구조대")
# # aa = da[cond1]
# # bb = aa['diff'].mean()
# # answer = int(bb)
# # print(answer)
#
# import pandas as pd
# da = pd.read_csv("busan_school_Info.csv")
# # print(da.info())
# # print(da.columns) ['school_name', 'student_1', 'student_2', 'student_3', 'student_4',
# #        'student_5', 'student_6', 'teacher']
#
#
# stu_col = ['student_1', 'student_2', 'student_3', 'student_4', 'student_5', 'student_6']
# da['total'] = da['student_1'] + da['student_2'] + da['student_3'] +da['student_4'] +da['student_5'] +da['student_6']
# da['ratio'] = da['total'] / da['teacher']
# # print(da['ratio'].sort_values().idx) # 21
#
# print(da.iloc[da['ratio'].idxmax()])




# ratio = da.iloc[:,1:7].sum(axis=1)/da['teacher']
#
# print(ratio)
# aa = da['school_name'][ratio.argmax()]
# df = da.loc[da['school_name'] == aa].copy()
#
# result = df['teacher'][ratio.argmax()]
#
# print(result)

# import pandas as pd
# da = pd.read_csv("five_crime.csv")
# # print(da.columns)
# da['total'] = da['살인_발생건수'] +da['강도_발생건수']  +da['강간_강제추행_발생건수'] + da['절도_발생건수'] + da['폭력_발생건수']
# # da['year'] = da['연월']
# # aa = da['total'].idxmax()
# # tot = da['연월']
# # print(da.iloc[aa])
# # print(da['연월'].unique())
# da['연월'] = da['연월'].copy().str.replace(' ','')
# # print(da['연월'].unique()) '2008.01월'
# da['year'] = da['연월'].str[:4]
# # print(da['year'])
# da['mon'] = da['연월'].str[5:7]
# # print(da['mon'])
#
# # aa = da.groupby('year')['total'].mean().idxmax()
# # print(aa)
# # # print(aa) 2012
# # # print(aa)
# # year = da['year']
# # cond = (year == '2012')
# # bb = da[cond]
# # print(bb['폭력_검거건수'].mean())
#
# # da['total'] = da.iloc[:,range(1,11,2)].sum(axis=1)
# bb = da.groupby('year')['total'].mean()
# # print(bb)
# max_year = bb.argmax()
# print(max_year)
# result = da.groupby('year')['폭력_검거건수'].mean()
# print(result)
# # aa = da.groupp

import pandas as pd

train = pd.read_csv("Airline_train.csv")
test = pd.read_csv("Airline_test.csv")
y_test = pd.read_csv("Airline_y_test.csv")

y_train = train['Satisfaction'].map({"Yes" : 1,"No":0})
X_train = train.copy().drop('Satisfaction', axis=1)
X_test = test
y_test = y_test['Satisfaction'].map({"Satisfied":1,"Not satisfied":0})
# print(y_test)
# print(y_test.value_counts())
# print(y_train

# print(X_train.columns)

# ['Gender', 'Ages', 'Customer_Type', 'Class', 'Inflight_wifi_service',
#        'Departure_Arrival_time_convenient', 'Ease_of_Online_booking',
#        'Gate_location', 'Food_and_drink', 'Online_boarding', 'Seat_comfort',
#        'Inflight_entertainment', 'On_board_service', 'Leg_room_service',
#        'Baggage_handling', 'Checkin_service', 'Inflight_service',
#        'Cleanliness', 'Departure_Delay_in_Minutes',
#        'Arrival_Delay_in_Minutes']

# print(X_train.info()) # 결측치 없음
for i in X_train.columns:
    if X_train[i].dtype == 'object':
        a = X_train[i].unique()
        idx = 0
        tmp = {}
        for j in a:
            tmp[j] = idx
            idx += 1
        X_train[i] = X_train[i].map(tmp)
        X_test[i] = X_test[i].map(tmp)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.metrics import f1_score

X_tr, X_val, y_tr , y_val = train_test_split(
    X_train, y_train, random_state = 23
)

rff = rf()
model = rff.fit(X_tr,y_tr)
pred = model.predict(X_val)
score = f1_score(y_val,pred)

obj = {"pred" : pred}
result = pd.DataFrame(obj)
# print(result)
result.to_csv("result.csv",index=False)

real_pred = model.predict(X_test)
real_score = f1_score(y_test,real_pred)
print(score, real_score)
