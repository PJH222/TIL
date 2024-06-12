import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit.csv")

dose = da['Dose']
qa2 = dose.quantile(0.50)
qa3 = dose.quantile(0.75)
print(qa2, qa3)

tmp = abs(qa2 - qa3)
print(int(tmp))

