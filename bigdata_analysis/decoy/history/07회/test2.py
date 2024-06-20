# import pandas as pd
#
# da = pd.read_csv("test_score.csv")
#
# da = da.copy().dropna()
#
# # 응시자가 가장 많은 연령대
# # print(da['연령대'].value_counts()) # 20
# age = da['연령대']
# # print(da.columns) ['연도', '직종', '회차', '일련번호', '과목명', '과목별점수', '총점', '합격여부', '성별', '연령대']
# # print(da['과목명']
#
# da = da[age == 20]
#
# ada = da['과목명']
# # score = da['과목별점수']
#
# da = da[ada == '기본간호학']
# score = da['과목별점수']
# avgg = score.mean()
# stdd = score.std()
#
# da['std'] = (da['과목별점수'] - avgg) / stdd
#
# print(round(da['std'].max(),4))



# import pandas as pd
# da = pd.read_csv("diabetes.csv")
#
# # print(da.columns) ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6', 'progression']
#
# # corr = da.corr()['progression'].abs().sort_value() bmi
# # print(corr)
#
# print(round(da['bmi'].max() , 2))

# import pandas as pd
# da = pd.read_csv("iris.csv")
#
# for i in da.columns:
#     if da[i].isna().sum() > 0:
#         med = da[i].median()
#         da[i] = da[i].copy().fillna(med)
# # print(da.columns) ['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
# #        'species']
# sep = da['sepal_length']
#
# q1 = sep.quantile(0.25)
# q3 = sep.quantile(0.75)
# iqr = q3 - q1
#
# cond = (sep < q1 - iqr * 1.5) | (sep > q3 + iqr * 1.5)
#
# print(len(da[cond]))


import pandas as pd
da = pd.read_csv("")