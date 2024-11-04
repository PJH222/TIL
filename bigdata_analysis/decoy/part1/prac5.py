import pandas as pd
import numpy as np

exam1 = pd.read_csv('C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv')

uniq = exam1[['Manufacturer','Origin']].drop_duplicates()
answer1 = uniq.shape[0]

exam1['str2'] = exam1['Manufacturer'].str[:2]

answer2 = exam1[['str2','Origin']].drop_duplicates().shape[0]

answer = answer1 - answer2
print(answer)




