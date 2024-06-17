import pandas as pd

X_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/FIFA_X_train.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/FIFA_y_train.csv")
X_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/FIFA_X_test.csv")

ID = X_test['ID'].copy()
X_train = X_train.drop(columns = 'ID')
X_test = X_test.drop(columns = 'ID')
y_train = y_train.drop(columns = 'ID')

# print(X_train.isna().sum())
# print(X_test.isna().sum())

# print(X_train['Position_Class'].value_counts())
X_train['Position_Class'] = X_train['Position_Class'].fillna('unknown')
print()
# print(X_train['Position_Class'].value_counts())
print()
aa = pd.crosstab(columns = X_train['Position_Class'], index = X_train['Position'])
# print(aa)

pct = X_train['Position_Class'].copy()
pot = X_train['Position'].copy()

pct[pot == "CM"] = 'Midfielder'
pct[pot == 'GK'] = 'GoalKeeper'
pct[pot == 'LF'] = 'Forward'
pct[pot == 'RDM'] = 'Defender'
pct[pot == 'RWB'] = 'Defender'

X_train['Position_Class'] = pct

# print(X_train['Position_Class'].isna().sum())
X_test['Position_Class'] = X_test['Position_Class'].fillna('unknown')
bb = pd.crosstab(columns = X_test['Position_Class'], index = X_test['Position'])

pcte = X_test['Position_Class'].copy()
pote = X_test['Position'].copy()

pcte[pote == 'CM'] = 'Midfielder'
pcte[pote == 'GK'] = 'GoalKeeper'
pcte[pote == 'LF'] = 'Forward'
pcte[pote == 'RDM'] = 'Defender'
pcte[pote == 'RWB'] = 'Defender'

X_test['Position_Class'] = pcte

# print(X_train.isna().sum()) Height_cm 292 Weight_lb 72

xtr_he = X_train['Height'].copy()
xtr_hecm = X_train['Height_cm'].copy()

aa = xtr_he.str.split("'", expand=True).astype('float64')
xtr_hecm = xtr_hecm.fillna(aa[0] * 30 + aa[1] * 2.5)
X_train['Height_cm'] = xtr_hecm

xtr_he = X_test['Height'].copy()
xtr_hecm = X_test['Height_cm'].copy()

aa = xtr_he.str.split("'", expand=True).astype('float64')
xtr_hecm = xtr_hecm.fillna(aa[0] * 30 + aa[1] * 2.5)
X_test['Height_cm'] = xtr_hecm

X_train = X_train.drop(columns='Height')
X_test = X_test.drop(columns='Height')


cond_na = X_train['Weight_lb'].isna()
y_train = y_train[~ cond_na]
X_train = X_train[~ cond_na]

# print(X_train['Age'])


print(X_train['Contract_Valid_Until'].value_counts())

