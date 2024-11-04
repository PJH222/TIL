import pandas as pd
import numpy as np

exam1 = pd.read_csv('C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv')

maxx = exam1['Max_Price'].sort_values(ascending = True, ignore_index = True)
minn = exam1['Min_Price'].sort_values(ascending = False, ignore_index = True)

aa = maxx - minn
print(round(aa.std(),3))


