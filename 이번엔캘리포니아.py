from sklearn.datasets import fetch_california_housing  #캘리포니아 집값
import pandas as pd
from sklearn.linear_model import LinearRegression

california_data = fetch_california_housing()

california = pd.DataFrame(data=california_data.data, columns=california_data.feature_names)
california['target'] = california_data.target

train = california.sample(frac=0.8, random_state=200)
test = california.drop(train.index)

mlr = LinearRegression()
mlr.fit(train[['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']], train['target'])
#함수x값, y값 이렇게친거임
print(mlr.intercept_) #절편
print(mlr.coef_) #기울기

sum_difference = 0
for i, row in test.iterrows():
    estimate = row['MedInc'] * mlr.coef_[0] + row['HouseAge'] * mlr.coef_[1] + row['AveRooms']* mlr.coef_[2] + \
        row['AveBedrms']* mlr.coef_[3] + row['Population'] * mlr.coef_[4] + row['AveOccup'] * mlr.coef_[5] + \
        row['Latitude'] * mlr.coef_[6] + row['Longitude'] * mlr.coef_[7] + mlr.intercept_

    difference = abs(row['target'] - estimate) #오차 = 실제 - 예측
    sum_difference += difference #오차의 절댓값의 합

print(sum_difference)