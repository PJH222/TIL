# # # 1번
# #
# # import pandas as pd
# #
# # da = pd.read_csv("iris.csv")
# #
# # # print(da.columns)
# # # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width',
# # #        'Species']
# #
# # sep = da['Sepal.Width']
# # avgg = sep.mean()
# # stdd = sep.std()
# #
# # aa = sep[sep >= avgg + stdd * 3]
# #
# # answer = sum(aa)
# # print(answer)
#
#
#
# # 2번
# # import pandas as pd
# #
# # da = pd.read_csv("mtcars1.csv")
# #
# # # print(da) mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
# #
# # da['rank'] = da['disp'].rank(method='min',ascending=False)
# # result = da['disp'][da['rank'] < 20].std()
# #
# #
# #
# # answer = round(result, 2)
# # print(answer)
#
# # 3 번
# # import pandas as pd
# # da = pd.read_csv("Cars93.csv")
# #
# # a = da.shape[0] # 93
# # print(a)
# #
# # b = len(da.columns[da.isna().sum() > 0]) # 6
# # print(b)
# #
# # c = sum(da.isna().sum()) # 72
# # print(c)
# #
# # d = da.columns[da.isna().sum() > 10]
# # dd = (da[d].copy().dropna()).shape[0]
# # print(dd)
# #
# # e = sum(list(da.index[da.isna().sum(axis=1) >= 2]))
# # print()
# # print()
# # print()
# #
# # # for i in da.loc[e]:
# # #     print(i)
# #
# # print(a+b+c+dd+e)
#
# # 1번
#
# import pandas as pd
#
# da = pd.read_csv("iris.csv")
# # print(da.columns)
# # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']
#
# sep = da['Sepal.Width']
# avgg = sep.mean()
# stdd = sep.std()
#
# aa = sep[sep >= avgg + stdd * 3]
#
# answer_1 = sum(aa)
# print(answer_1)

# 2번

# import pandas as pd
#
# da = pd.read_csv("mtcars1.csv")
#
# # print(da)
# # mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
# # 0   21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
# # 1   21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
#
# diss = da['disp'].rank(method='min', ascending= False)
# aa = da['disp'][diss < 20]
#
# stdd = aa.std()
# answer_2 = round(stdd, 2)
# print(answer_2)


# 3번
# import pandas as pd
# da = pd.read_csv("Cars93.csv")
#
# a = da.shape[0]
# b = sum(da.isna().sum() > 0)
# c = sum(da.isna().sum())
#
# coll = da.columns[da.isna().sum() >= 10]
# da2 = da.copy()
# d = da2[coll].dropna().shape[0]
#
# e = sum(da.index[da.isna().sum(axis=1) >= 2])
# print(a+b+c+d+e)
# # 1090



# 3유형 1번
# import pandas as pd
# da = pd.read_csv("Cars93.csv")
#
# from scipy.stats import ttest_rel, t , ttest_ind
#
# # print(da.columns)
# typee = da['Type']
# pri = da['Price']
#
# m1 = pri[typee == "Large"].reset_index(drop=True).dropna()
# m2 = pri[typee == "Small"].reset_index(drop=True).dropna()
#
# answer_1 = m1.mean() - m2.mean()
# print(round(answer_1, 5))
#
# stat, pval = ttest_ind(m1,m2)
#
# print(round(answer_1 / stat , 2))
#
# ci = t.interval(0.95, 27, loc = answer_1, scale = round(answer_1 / stat , 2))
# print(ci)
#
# print(pval)

# pri = da['Price']
# typ = da['Type']
#
# m1 = pri[typ == "Large"].reset_index(drop=True).dropna()
# m2 = pri[typ == "Small"].reset_index(drop=True).dropna()
#
# answer_a = round(m1.mean() - m2.mean(),2)
# print(answer_a)
#
# # 검정통계량 = 점추정량 / 표준오차
#
# from scipy.stats import t, ttest_ind
#
# stat , pval = ttest_ind(m1, m2,equal_var = True)
# dff = 27
#
# err = stat / answer_a # 계산 실수하지마라...
# answer_b = round(1/err , 2)
# print(answer_b)
#
# # print(t.interval(0.95,27,answer_a,answer_b)) # 신뢰도, df, 점추정량, 표준오차 순으로 들어간다. 검정 통계량은 안들어가니 주의할 것...
#
# answer_c = t.interval(0.95,dff,answer_a,answer_b)
# print(answer_c)
# print(round(answer_c[0] , 1))
#
# print(stat)

# pri = da['Price']
# typ = da['Type']
#
# m1 = pri[typ == 'Large'].copy().reset_index(drop=True).dropna()
# m2 = pri[typ == 'Small'].copy().reset_index(drop=True).dropna()
#
# answer_a = round(m1.mean() - m2.mean(), 2)
# print(answer_a)

# 검정 통계량 = 점추정량 / 표준오차

# from scipy.stats import ttest_ind as tt
#
# stat, pval = tt(m1, m2, equal_var = True)
# dff = len(m1) + len(m2) - 2
#
# answer_b = round( answer_a / stat , 2)
# print(answer_b)
#
# from scipy.stats import t
#
# intt = t.interval(0.95, dff, loc = answer_a, scale = answer_b)
# answer_c1 = round(intt[0] , 1)
# print(answer_c1)
#
# if stat < answer_c1:
#     print("기각")
# else:
#     print("채택")
#


# 작업형 3 유형
# 2번

# import pandas as pd
# da = pd.read_csv("dices.csv")
#
# # 적합도 검정
# from scipy.stats import chisquare
#
# tb = da['scale'].value_counts().sort_index()
#
# expp = tb.sum()*1/6
# answer_a = int(expp)
# print(answer_a)
#
# stat, pval = chisquare(tb)
# print(int(stat))
#
# pval = round(pval, 4)
#
# if pval < 0.0001:
#     pval = 0
#
# print(pval)
# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")


# 2 번
#
# import pandas as pd
# da = pd.read_csv("dices.csv")
#
# sca = da['scale']
#
# aa = sca.value_counts().sort_index()
#
# # print(aa)
#
# answer_a = aa.sum() * 1/ 6
#
# print(answer_a)
#
# from scipy.stats import chisquare
#
# stat, pval = chisquare(aa)
# print(int(stat))
#
# pval = round(pval, 4)
# if pval < 0.0001:
#     pval = 0
# print(pval)
#
# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")


