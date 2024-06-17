import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/USArrests.csv")

# print(da.columns) ['Murder', 'Assault', 'UrbanPop', 'Rape']

from sklearn.decomposition import PCA

pca = PCA()
pca.fit_transform(da)

aa = pca.components_
print(round(aa[0,1],3))

pcaa = PCA()
bb = pcaa.fit_transform(da)
print(round(bb[33][0],3))

result = pcaa.explained_variance_ratio_
print(round(result[0],2))
print(result)


