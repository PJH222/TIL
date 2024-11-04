import pandas as pd
import numpy as np

exam1 = pd.read_csv('C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv')

meann = exam1['Wheelbase'].mean()
stdd_15 = exam1['Wheelbase'].std() * 1.5
stdd_20 = exam1['Wheelbase'].std() * 2
stdd_25 = exam1['Wheelbase'].std() * 2.5

mean_15_plus = meann + stdd_15
mean_20_plus = meann + stdd_20
mean_25_plus = meann + stdd_25

mean_15_minus = meann - stdd_15
mean_20_minus = meann - stdd_20
mean_25_minus = meann - stdd_25

answer_15 = exam1['Wheelbase'][(exam1['Wheelbase'] > mean_15_minus) & (exam1['Wheelbase'] < mean_15_plus)]
answer_20 = exam1['Wheelbase'][(exam1['Wheelbase'] > mean_20_minus) & (exam1['Wheelbase'] < mean_20_plus)]
answer_25 = exam1['Wheelbase'][(exam1['Wheelbase'] > mean_25_minus) & (exam1['Wheelbase'] < mean_25_plus)]

result = answer_15.mean() + answer_20.mean() + answer_25.mean() - exam1['Wheelbase'].mean() * 3
print(round(result,4))






