import pandas as pd
import numpy as np

exam1 = pd.read_csv('C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv')

lenn = exam1['Length'].rank(method = 'average')
stdd = exam1['Length'][lenn <= 30]
print(lenn)
print(round( stdd.std() , 3))
# result = round(stdd,3)
# print(result)












