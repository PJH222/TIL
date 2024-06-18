import pandas as pd
import time
a = time.time()

X_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/FIFA_X_train.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/FIFA_y_train.csv")
X_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/FIFA_X_test.csv")

##### STEP3. 데이터셋 전처리
###### STEP3-1. 불필요한 컬럼 삭제
# ID 컬럼은 선수에 대한 고유 정보로 key 역할로 모델에는 불필요함
# 결과 제출 시에는 X_test의 ID 컬럼이 필요하기 때문에 별도 저장
ID = X_test['ID'].copy()

# 데이터들에서 ID 컬럼 삭제
X_train = X_train.drop(columns = 'ID')
X_test = X_test.drop(columns = 'ID')
y_train = y_train.drop(columns = 'ID')

X_train['Position_Class'] = X_train['Position_Class'].fillna('unknown') # unknown으로 대체

PC_train = X_train['Position_Class'].copy()
PC_train[X_train['Position'] == 'LF'] = 'Forward'
PC_train[X_train['Position'] == 'CM'] = 'Midfielder'
PC_train[X_train['Position'] == 'RDM'] = 'Defender'
PC_train[X_train['Position'] == 'RWB'] = 'Defender'
PC_train[X_train['Position'] == 'GK'] = 'GoalKeeper'
X_train['Position_Class'] = PC_train

# X_test에 대해 누락된 카테고리 채우기
PC_test = X_test['Position_Class'].copy()
PC_test[X_test['Position'] == 'LF'] = 'Forward'
PC_test[X_test['Position'] == 'CM'] = 'Midfielder'
PC_test[X_test['Position'] == 'RDM'] = 'Defender'
PC_test[X_test['Position'] == 'RWB'] = 'Defender'
PC_test[X_test['Position'] == 'GK'] = 'GoalKeeper'
X_test['Position_Class'] = PC_test

####### Height_cm 컬럼
# 단위가 인치와 피트인 문자열 Height를 단위 변환하는 과정에서 누락되었을 것
# 기존의 Height를 활용해 결측치를 대체
# X_train에 대해 누락된 값 채우기
Height_train = X_train['Height'].copy()
Height_cm_train = X_train['Height_cm'].copy()

# '를 기준으로 앞은 피트 * 30, 뒤는 인치 * 2.5한 후 합
# '를 기준으로 문자열을 분리한 후, expand = True를 통해 다른 열에 할당함
# 잘린 문자열은 수치형이랑 곱할 수 없으므로 astype() 메소드를 통해
# 각 열(시리즈)들의 dtype을 float64로 저장되도록 함
split_str_train = Height_train.str.split("'", expand = True).astype('float64')

# 결측치 대체
Height_cm_train = Height_cm_train.fillna(split_str_train[0] * 30 + split_str_train[1] * 2.5)
X_train['Height_cm'] = Height_cm_train

# X_test에 대해 누락된 값 채우기
Height_test = X_test['Height'].copy()
Height_cm_test = X_test['Height_cm'].copy()

# '를 기준으로 앞은 피트 * 30, 뒤는 인치 * 2.5한 후 합
# '를 기준으로 문자열을 분리한 후, expand = True를 통해 다른 열에 할당함
# 잘린 문자열은 수치형이랑 곱할 수 없으므로 astype() 메소드를 통해
# 각 열(시리즈)들의 dtype을 float64로 저장되도록 함
split_str_test = Height_test.str.split("'", expand = True).astype('float64')

# 결측치 대체
Height_cm_test = Height_cm_test.fillna(split_str_test[0] * 30 + split_str_test[1] * 2.5)
X_test['Height_cm'] = Height_cm_test

# 완료 후 Height 컬럼을 삭제
X_train = X_train.drop(columns = 'Height')
X_test = X_test.drop(columns = 'Height')

cond_na = X_train['Weight_lb'].isna()

# y_train에 대해 X_train에 누락된 Weight_lb가 있는 행을 삭제함
y_train = y_train[~ cond_na]

# X_train에 대해 X_train에 누락된 Weight_lb가 있는 행을 삭제함
X_train = X_train[~ cond_na]

####### Age컬럼
# 일부 선수의 나이가 일의 자리가 마스킹 되어있음
# Age_gp(연령대)인 카테고리형 파생변수 생성
X_train['Age_gp'] = X_train['Age'].str[0]
X_test['Age_gp'] = X_test['Age'].str[0]

# 완료 후 Age 컬럼을 삭제
X_train = X_train.drop('Age', axis = 1)
X_test = X_test.drop('Age', axis = 1)

X_train = X_train.drop(columns = 'Club')
X_test = X_test.drop(columns = 'Club')

####### Work_Rate컬럼
# 공격 운동량/ 방어 운동량
# '/'를 기준으로 앞은 공격 운동량(WR_Attack), 뒤는 방어 운동량(WR_Defend) 컬럼으로 생성
# '/' 뒤에 공백하나가 있음으로 이에 대한 제거가 필요
# 그 이후 '/'를 기준으로 문자열을 분리한 후, expand = True를 통해 다른 열에 할당
# train
Work_Rate_train = X_train['Work_Rate'].copy()
Work_Rate_train = Work_Rate_train.str.replace(' ','') # 공백 제거

# '/'를 기준으로 문자열을 분리하여 파생변수 WR_Attack, WR_Defend 생성
X_train['WR_Attack'] = Work_Rate_train.str.split("/", expand = True)[0]
X_train['WR_Defend'] = Work_Rate_train.str.split("/", expand = True)[1]

# test
Work_Rate_test = X_test['Work_Rate'].copy()
Work_Rate_train = Work_Rate_train.str.replace(' ','') # 공백 제거

# '/'를 기준으로 문자열을 분리하여 파생변수 WR_Attack, WR_Defend 생성
X_test['WR_Attack'] = Work_Rate_test.str.split("/", expand = True)[0]
X_test['WR_Defend'] = Work_Rate_test.str.split("/", expand = True)[1]

# 완료 후 Work_Rate 컬럼을 삭제
X_train = X_train.drop(columns = 'Work_Rate')
X_test = X_test.drop(columns = 'Work_Rate')

X_train = X_train.drop('Jersey_Number', axis = 1)
X_test = X_test.drop('Jersey_Number', axis = 1)

X_train['CVU_gp'] = X_train['Contract_Valid_Until'].astype('object') # dtype변환
X_test['CVU_gp'] = X_test['Contract_Valid_Until'].astype('object') # dtype변환

# 완료 후 Contract_Valid_Until 컬럼을 삭제
X_train = X_train.drop('Contract_Valid_Until', axis = 1)
X_test = X_test.drop('Contract_Valid_Until', axis = 1)

####### 수치형 컬럼 간 상관관계 확인
# 상관관계를 확인할 컬럼만
colnm_conti = ['Overall', 'Height_cm', 'Weight_lb', 'Release_Clause', 'Wage']
X_train[colnm_conti].corr()

# Release_Clause 컬럼을 제외
X_train = X_train.drop('Release_Clause', axis = 1)
X_test = X_test.drop('Release_Clause', axis = 1)

from sklearn.model_selection import train_test_split

# X_train과 y_train을 학습용(X_TRAIN, y_TRAIN)과 검증용(X_VAL, y_VAL)로 분할
X_TRAIN, X_VAL, y_TRAIN, y_VAL = train_test_split(X_train, y_train, random_state =1234, test_size = 0.3)

from sklearn.preprocessing import OneHotEncoder

# 인코딩할 카테고리형 컬럼만 별도 저장
X_TRAIN_category = X_TRAIN.select_dtypes('object').copy()
X_VAL_category = X_VAL.select_dtypes('object').copy()
X_TEST_category = X_test.select_dtypes('object').copy()

# Nationality의 유일 값 수가 데이터셋마다 다름
# handle_unknown = 'ignore'은 Train에 없는 레이블이 Test에 있더라도 이들을 모두 0이됨
enc = OneHotEncoder(handle_unknown = 'ignore').fit(X_TRAIN_category)

# 원-핫 인코딩
X_TRAIN_OH = enc.transform(X_TRAIN_category)
X_VAL_OH = enc.transform(X_VAL_category)
X_TEST_OH = enc.transform(X_TEST_category)

###### STEP3-7. 스케일링
from sklearn.preprocessing import StandardScaler

# 스케일링할 컬럼만 별도 저장
colnm_conti = ['Overall', 'Height_cm', 'Weight_lb', 'Wage']
X_TRAIN_conti = X_TRAIN[colnm_conti].copy()
X_VAL_conti = X_VAL[colnm_conti].copy()
X_TEST_conti = X_test[colnm_conti].copy()

# TRAIN 데이터 기준으로 스케일링함
scale = StandardScaler().fit(X_TRAIN_conti)

# z-점수 표준화
X_TRAIN_STD = scale.transform(X_TRAIN_conti)
X_VAL_STD = scale.transform(X_VAL_conti)
X_TEST_STD = scale.transform(X_TEST_conti)

###### STEP3-8. 입력 데이터셋 준비
import numpy as np

# 인코딩과 스케일링된 넘파이 ndarray 연결
# X_TRAIN = np.concatenate([X_TRAIN_OH, X_TRAIN_STD], axis = 1)
# X_VAL = np.concatenate([X_VAL_OH, X_VAL_STD], axis = 1)

# 1차원 넘파이 ndarray로 평탄화
# y_TRAIN = y_TRAIN.values.ravel()
# y_VAL = y_VAL.values.ravel()

##### STEP4. 모델 학습
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, BaggingRegressor, AdaBoostRegressor
print(X_TRAIN.describe())
###### STEP4-1. random forest
rf = RandomForestRegressor(n_estimators = 500, max_depth = 3, min_samples_leaf = 10, max_features = 50, random_state = 2022)
model_rf = rf.fit(X_TRAIN, y_TRAIN)