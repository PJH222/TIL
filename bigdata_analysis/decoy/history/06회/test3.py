# import pandas as pd

# da = pd.read_csv("sejong_fire.csv")

# print(da) 관할서명        서센터명      화재구분              접수일시            상황종료일시
# 조치원소방서   전의119안전센터      기타화재  2012-08-28 16:36  2012-08-28 17:09

# for i in da.columns:
#     a = da[i].unique()
#     for j in a:
#         print(j)

# from datetime import datetime
#
# da['start'] = da['접수일시'].copy().apply(lambda x : datetime.strptime(x,'%Y-%m-%d %H:%M'))
# da['end'] = da['상황종료일시'].copy().apply(lambda x : datetime.strptime(x,'%Y-%m-%d %H:%M'))
# da['total'] = round((da['end'] - da['start']).dt.total_seconds() / 60)
# # print(da['total'].idxmax()) 54
# # print(da.iloc[54]) 조치원119구조대
#
# tot = da['total'].copy()
# cen = da['서센터명']
# cond = (cen == '조치원119구조대')
#
# a = int(round(da[cond]['total'].mean()))
# print(a)


# import pandas as pd
#
# da = pd.read_csv("busan_school_Info.csv")
#
# # print(da.columns) ['school_name', 'student_1', 'student_2', 'student_3', 'student_4',
# #        'student_5', 'student_6', 'teacher']
#
# # da['total'] = da['student_1']+ da['student_2']+ da['student_3']+ da['student_4'] + da['student_5']+da['student_6']
# # print(da['total'])
# #
# da['total'] = da.iloc[:,1:7].sum(axis=1)
# da['ratio'] = da['total'] / da['teacher']
# a = da['ratio'].idxmax()
# # answer = da['teacher'].iloc[a]
# # print(answer)
#
#
#
# import pandas as pd
#
# da = pd.read_csv("five_crime.csv")
#
# # print(da.columns) ['연월', '살인_발생건수', '살인_검거건수', '강도_발생건수', '강도_검거건수', '강간_강제추행_발생건수',
#        # '강간_강제추행_검거건수', '절도_발생건수', '절도_검거건수', '폭력_발생건수', '폭력_검거건수']
# import numpy as np
#
# da['total'] = da.iloc[:,np.arange(1,10,2)].sum(axis=1)
# # print(da) 2008. 01 월
# da['year'] = da['연월'].str[:4]
# aa = da.groupby('year')['total'].sum()
# # print(aa.idxmax()) 2012
# year = da['year']
#
# cond = (year == '2012')
# print(int(round(da[cond]['폭력_검거건수'].mean())))

#
# import pandas as pd
#
# da = pd.read_csv("cancer.csv")
# n = da.shape[0]
# # print(da.isna().sum())
# answer = []
# answer.append(81)
#
# import numpy as np
#
# daa = da.copy().value_counts().to_numpy()
# daa = np.append(daa, answer[0])
#
# bb = np.array([0.05,0.05,0.1,0.8]) * n
#
# from scipy.stats import chisquare as ch
#
# stat , pval = ch(daa , bb)
# answer.append(int(round(stat)))
#
# answer.append(int(round(pval)))
#
# print(answer)


import pandas as pd

da = pd.read_csv("airquality.csv")
da = da.copy().dropna()

import statsmodels.api as sm

ind_col = ['Solar.R','Wind','Temp']
dep_col = ['Ozone']

y = da[dep_col]
x = da[ind_col]
x = sm.add_constant(x)

result = sm.OLS(y,x).fit()
print(result.summary())

import numpy as np

answer = []
answer.append(round(0.0637,2))
answer.append(round(2.234,2))

new_da = pd.read_csv("airquality_new.csv")

new_x = new_da.copy()[ind_col]
new_x = sm.add_constant(new_x)
# print(new_x, x)

pred = result.get_prediction(new_x)
new_y = new_da[dep_col]

# print(pred)
from sklearn.metrics import accuracy_score as ACC
# print(pred.summary_frame().iloc[9])

answer.append(round(91.763178,2))

# score = ACC(new_y,pred)
# print(score)

print(answer)