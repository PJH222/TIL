import pandas as pd

exam1 = pd.read_csv("decoy/practice/Cars93.csv")
# exam1 = pd.read_csv('data/연습문제/Cars93.csv')

print(exam1)

# std 1.5배
wheelbase = exam1['Wheelbase']
# print(wheelbase)
wheelbase_mean = wheelbase.mean()
print(wheelbase_mean)



