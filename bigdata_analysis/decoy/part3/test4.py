# 3번

# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/고객_등급리스트.csv")
#
# # print(da.columns)
# # ['Customer_ID', 'ID', 'Name', 'Age', 'City', 'State', 'Region',
# #        'Segment'],
#
# seg, reg = da['Segment'], da['Region']
#
# ct = pd.crosstab(seg,reg)
#
# from scipy.stats import chi2_contingency
#
# stat, pval, dof, dff = chi2_contingency(ct)
# # print()??
#
# print(round(dff[1,2], 2))
#
# print(int(stat))
#
# print(round(pval,3), "채택")



# # 6번
#
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/USArrests.csv")
#
# # 차원 축소
# # print(da.columns) ['Murder', 'Assault', 'UrbanPop', 'Rape']
# ass = da['Assault']
#
# from sklearn.decomposition import PCA
#
# pca = PCA(n_components = 4)
# aa = pca.fit_transform(da)
# print(aa)
#
# print(pca.components_)
#
# # print(round(pca.components_[0,1],3))
# #
# # print(round(aa[33,0],3))
# #
# # ratioo = pca.explained_variance_ratio_
# # print(round(ratioo[0],2), 3)
#
#


# 7 번

# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# col_for_drop = ['Rev_per_mile','Weight','Length','EngineSize','Price']
# df = da[col_for_drop].copy().dropna()
#
# y = df['Price']
# x = df[['Rev_per_mile','Weight','Length','EngineSize']]
#
# import statsmodels.api as sm
#
# x = sm.add_constant(x)
# aa = sm.OLS(y,x)
# result = aa.fit()
#
# print(result.summary())
#
# print(0.396)
#
#
# print(0.0023)
#
# print(0.158)
#
# upper = result.conf_int(alpha=0.05)
# print(upper)
#
# print(0.005)



# 6번

# import pandas as pd
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/USArrests.csv")
#
# from sklearn.decomposition import PCA
#
# # print(da.columns) ['Murder', 'Assault', 'UrbanPop', 'Rape']
# pca = PCA()
# aa = pca.fit_transform(da)
# result = pca.components_
# print(round(result[0,1], 3))
#
# print(round(aa[33,0] ,  3))
#
# bb = pca.explained_variance_ratio_
#
# print(round(bb[0] , 2), 3)

