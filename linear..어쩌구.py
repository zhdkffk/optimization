from sklearn.datasets import load_boston  #보스턴 집값(1960년대)
import pandas as pd
from sklearn.linear_model import LinearRegression

boston_data = load_boston()

boston = pd.DataFrame(data=boston_data.data, columns=boston_data.feature_names)  #2차원배열루,,
boston['target'] = boston_data.target

train = boston.sample(frac=0.8, random_state=200)
test = boston.drop(train.index)

#회귀분석
mlr = LinearRegression()
mlr.fit(train[['PTRATIO','INDUS','NOX','B','CHAS','RAD','TAX','ZN','DIS','CRIM','RM','LSTAT','AGE']], train['target'])
#함수x값, y값 이렇게친거임
print(mlr.intercept_) #절편
print(mlr.coef_) #기울기

sum_difference = 0
for i, row in test.iterrows():
    #예측
    estimate = row['PTRATIO'] * mlr.coef_[0] + row['INDUS'] * mlr.coef_[1] + row['NOX']* mlr.coef_[2] + \
        row['B']* mlr.coef_[3] + row['CHAS'] * mlr.coef_[4] + row['RAD'] * mlr.coef_[5] + \
        row['TAX'] * mlr.coef_[6] + row['ZN'] * mlr.coef_[7] + row['DIS'] * mlr.coef_[8] + \
        row['CRIM'] * mlr.coef_[9] + row['RM'] * mlr.coef_[10] + row['LSTAT'] * mlr.coef_[11] + \
        row['AGE'] * mlr.coef_[12] + mlr.intercept_

    difference = abs(row['target'] - estimate) #오차 = 실제 - 예측
    sum_difference += difference

print(sum_difference)