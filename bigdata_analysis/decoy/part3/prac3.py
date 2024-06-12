import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/고객_등급리스트.csv")

# from scipy.stats import chi2_contingency
#
# tb = pd.crosstab(da['Segment'],da['Region'])
#
# a,b,c,d = chi2_contingency(tb)
# # print(a,b,c,d)
#
# print("a번 정답 :",round(d[1][2],2))
#
# print("b번 정답 :", int(a))
#
# print("c번 정답 :", round(b,3), "채택")



from scipy.stats import chi2_contingency

aa = pd.crosstab(da['Segment'], da['Region'])

a,b,c,d = chi2_contingency(aa)

print("a번 정답 :", round(d[1][2],2))

print("b번 정답 :", int(a))

print("c번 정답 :", round(b,3), "채택")








