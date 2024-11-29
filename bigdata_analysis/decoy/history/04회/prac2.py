import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/04회/Cars93.csv")

# tu = df['Turn_circle']
# a1 = tu.quantile(.25)
# a2 = tu.quantile(.5)
# answer = int(abs(a1 - a2))
# print(answer) # 2

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/04회/facebook_subset.csv")

# print(df.columns) ['userid', 'age', 'dob_day', 'dob_year', 'dob_month', 'gender', 'tenure',
#        'friend_count', 'friendships_initiated', 'likes', 'likes_received',
#        'mobile_likes', 'mobile_likes_received', 'www_likes',
#        'www_likes_received']

# df['ratio'] = df['mobile_likes_received'] / df['likes_received']
# ra = df['ratio']
# ge = df['gender']

# cond1 = ((ra > 0.6) & (ra < 0.7))
# cond2 = (ge == 'male')

# print(df[cond1 & cond2].shape[0])


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/04회/netflix_subset.csv")
# print(df.columns) ['show_id', 'type', 'title', 'cast', 'country', 'date_added',
#        'release_year', 'rating', 'duration', 'listed_in']
df['date_added'] = df['date_added'].str.replace(' ','')
# print(df['date_added'])
df['year'] = df['date_added'].str[7:9]
df['month'] = df['date_added'].str[3:6]
# df['date_added'] = df['date_added'].str.replace(' ','')

# print(df['month'])

cond1 = ((df['year'] == "21") & (df['month'] == 'Jan'))
cond2 = (df['listed_in'] == "Dramas")
# # print(df['listed_in'].unique())
# print(df[cond1 & cond2].shape[0])

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/04회/bodyPerfor_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/04회/bodyPerfor_test.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/04회/bodyPerfor_class.csv")

y_train = x_train['class'].copy()
x_train = x_train.drop(columns = 'class' , axis = 1)

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtype
    print(b , len(a) , i)
    # id는 제거 필요

x_train = x_train.drop(columns = "id" , axis = 1)
x_test = x_test.drop(columns = "id" , axis = 1)

# print(y_train.value_counts())

# y_train = y_train.map(tmp)
y_test  = y_test.drop(columns = 'id', axis = 1) 

tmp = []

for i in x_train.columns:
    a = x_train[i].dtype
    if a == 'object':
        tmp.append(i)

from sklearn.preprocessing import LabelEncoder as le

lle = le()

for i in tmp:
    a = lle.fit(x_train[i])
    x_train[i] = a.transform(x_train[i])
    x_test[i] = a.transform(x_test[i])

y_test = np.ravel(y_test)

a = lle.fit(y_train)
y_train = a.transform(y_train)
y_test = a.transform(y_test)

from sklearn.model_selection import train_test_split as tts

x , x_val, y , y_val = tts(x_train, y_train, random_state = 1234 , test_size = 0.2 , stratify = y_train)

# print(x.shape, y.shape)

from sklearn.ensemble import RandomForestClassifier as rff
from xgboost import XGBClassifier as xgg
from lightgbm import LGBMClassifier as lgg
from sklearn.metrics import f1_score as f1

rf , xg , lg = rff() , xgg(), lgg()
rf_model , xg_model, lg_model = rf.fit(x,y), xg.fit(x,y) , lg.fit(x,y)
rf_pred , xg_pred , lg_pred = rf_model.predict(x_val),xg_model.predict(x_val),lg_model.predict(x_val)
rf_score = f1(y_val , rf_pred, average = 'macro')
xg_score = f1(y_val , xg_pred, average = 'macro')
lg_score = f1(y_val , lg_pred, average = 'macro')

print(rf_score,xg_score,lg_score)

pred = lg_model.predict(x_test)
obj = {'class' : pred}
result = pd.DataFrame(obj)
result.to_csv("result.csv", index = False)

actual = f1(y_test , pred , average = 'macro')
print(actual)