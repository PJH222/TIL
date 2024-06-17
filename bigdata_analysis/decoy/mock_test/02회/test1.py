# 모의고사 2 회

# 작업형 1유형
# 1번
#
# import pandas as pd
# da = pd.read_csv("USArrests.csv")
#
# # print(da)     Murder  Assault  UrbanPop  Rape
#
# urb = da['UrbanPop']
# mru = da['Murder']
# ass = da['Assault']
#
# dff = da[urb >= 60].copy()
# dff['sum'] = dff['Murder'] + dff['Assault']
# dff['ratio'] = dff['Assault'] / dff['sum']
#
# new_dff = dff[dff['ratio'] >= 0.05]
# print(len(new_dff))


# 2번
# import pandas as pd
# da = pd.read_csv("swiss.csv")
# # print(da)     Fertility  Agriculture  Examination  Education  Catholic  Infant.Mortality
#
# dff = da.sort_values("Fertility", ascending = False,ignore_index = True)
# # print(dff)
#
# import numpy as np
#
# alll = np.arange(1,48)
# odd = (alll % 2 == 1)
# even = (alll % 2 == 0)
#
# diff = dff[odd].mean() - dff[even].mean()




# import pandas as pd
# da = pd.read_csv("swiss.csv")
# fer = da['Fertility'].sort_values(ascending=False , ignore_index=True)
#
# odd, even = 0 , 0
# cnt1 , cnt2 = 0, 0
# for i in range(len(fer)):
#     if i%2 == 0:
#         odd += fer[i]
#         cnt1 += 1
#     else:
#         even += fer[i]
#         cnt2 += 1
# else:
#     m1 = odd / cnt1
#     m2 = even / cnt2
#
# answer = round(m1 - m2, 3)
# print(answer)


# 3번
# import pandas as pd
# da = pd.read_csv("CO2.csv")

# print(da)            Type   Treatment  conc  uptake
# typ = da['Type']
# con = da['conc']
#
# cond1 = (typ == "Mississippi")
# cond2 = (con // 100 == 5) | (con.astype("string").str.endswith("5"))
#
# condition = cond1 & cond2
# print((da[condition]).shape[0])

# con1 = (da['Type'] == 'Mississippi')
# hun = (da['conc'] // 100 == 5)
# onee = da['conc'].astype("string").str.endswith("5")
#
# con2 = hun | onee
#
# print(da[con1 & con2].shape[0])

# 3유형
# 1번

# import pandas as pd
# da = pd.read_csv("survey.csv")
#
# se = da['성별']
# q1 = da['1번문항']
#
# ct = pd.crosstab(se,q1)
#
# from scipy.stats import chi2_contingency
# stat, pval, dof, df = chi2_contingency(ct)
# print(int(df[0][2]))
#
# print(int(stat))
#

# 2번
# import pandas as pd
# da = pd.read_csv("Cars93.csv")
#
# ori = da['Origin']
# mxx = da['Max_Price']
#
# non = mxx[ori == "non-USA"]
# uss = mxx[ori == 'USA']
#
# answer_a = non.mean() - uss.mean()
# print(round(answer_a , 2))
#
# from scipy.stats import ttest_ind
#
# stat, pval = ttest_ind(non,uss,equal_var = False)
# # 검정 = 점추정 / 오차
#
# err = round(answer_a / stat , 2)
# print(err)

# 1유형
# 1번

# import pandas as pd
#
# da = pd.read_csv("USArrests.csv")
# # print(da)     Murder  Assault  UrbanPop  Rape
#
# urb = da['UrbanPop']
# aa = da[urb >= 60].copy()
#
# aa['ratio'] = aa['Assault'] / (aa['Assault'] + aa['Murder'])
# condition = (aa['ratio'] >= 0.05)
# answer = aa[condition].shape[0]
#
# print(answer)

# 2번

# import pandas as pd
# da = pd.read_csv("swiss.csv")
#
# # print(da)     Fertility  Agriculture  Examination  Education  Catholic  Infant.Mortality
#
# aa = da['Fertility'].sort_values(ascending = False).reset_index(drop=True) # 총길이 47
#
# import numpy as np
# idx = np.arange(1,48)
#
# cond1 = (idx % 2 == 1)
# cond2 = (idx % 2 == 0)
#
# odd = aa[cond1].mean()
# even = aa[cond2].mean()
#
# answer = round(odd - even, 3)
# print(answer)


# 3 번
# import pandas as pd
# da = pd.read_csv("CO2.csv")
#
# # print(da)            Type   Treatment  conc  uptake
#
# typ = da['Type']
# con = da['conc']
#
# cond1 = (typ == 'Mississippi')
# # print(max(da['conc']) , min(da['conc']))  1000 95
# cond2 = ((con//100)==5 ) | ((con.astype('string').str.endswith('5')))
# print(da[cond1 & cond2].shape[0])


# 3유형
# 1번
# import pandas as pd
# da = pd.read_csv("survey.csv")
#
# q1 = da['1번문항']
# se = da['성별']
#
# from scipy.stats import chi2_contingency
#
# ct = pd.crosstab(se, q1)
# stat, pval, dof , dff = chi2_contingency(ct)
#
# answer = []
# # print(dff)
# answer.append(87)
#
# answer.append(int(stat))
#
# answer.append(round(pval,4))
#
# if pval < 0.05:
#     answer.append("기각")
# else:
#     answer.append("채택")
#
# print(answer)



# 2번
# import pandas as pd
# da = pd.read_csv("Cars93.csv")
#
# ori = da['Origin']
# pri = da['Max_Price']
#
# m1 = pri[ori == "USA"]
# m2 = pri[ori != "USA"]
#
# answer = []
# answer.append(round(m2.mean() - m1.mean() , 2))
#
# # 검정 통계량 = 점 추정량 / 표준 오차
# print(answer)
# from scipy.stats import ttest_ind, t
# stat, pval= ttest_ind(m2 , m1, equal_var = False)
# dof = len(m1) + len(m2) - 2
#
# answer.append(round(answer[0]/stat , 2))
# pval = round(pval , 4)
# answer.append(round(stat,4))
#
# if pval < 0.05:
#     answer.append("기각")
# else:
#     answer.append("채택")
#
# print(answer)
