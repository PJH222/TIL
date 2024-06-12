# Cars93데이터셋의 Wheelbase 컬럼에 대해 평균값에서 표준편

import pandas as pd

exam1 = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
# exam1 = pd.read_csv('data/연습문제/Cars93.csv')

# print(exam1)

# std 1.5배
wheelbase = exam1['Wheelbase']
# print(wheelbase)
meann = wheelbase.mean()
wheelbase_std = wheelbase.std()

std_15 = wheelbase_std * 1.5
std_2 = wheelbase_std * 2
std_25 = wheelbase_std * 2.5

a_plus = meann + std_15
a_minus = meann - std_15

b_plus = meann + std_2
b_minus = meann - std_2

c_plus = meann + std_25
c_minus = meann - std_25

avg_1 = wheelbase[(wheelbase > a_minus) & (wheelbase < a_plus)].mean()
avg_2 = wheelbase[(wheelbase > b_minus) & (wheelbase < b_plus)].mean()
avg_3 = wheelbase[(wheelbase > c_minus) & (wheelbase < c_plus)].mean()

result = meann * 3 - (avg_1 + avg_2 + avg_3)
print(round(result,4))





