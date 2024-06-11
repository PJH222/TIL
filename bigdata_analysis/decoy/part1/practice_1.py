# Cars93데이터셋의 Wheelbase 컬럼에 대해 평균값에서 표준편

import pandas as pd

exam1 = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
# exam1 = pd.read_csv('data/연습문제/Cars93.csv')

# print(exam1)

# std 1.5배
wheelbase = exam1['Wheelbase']
# print(wheelbase)
wheelbase_mean = wheelbase.mean()
wheelbase_std = wheelbase.std()





