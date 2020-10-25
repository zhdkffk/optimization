from sklearn.datasets import fetch_california_housing
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

boston_data = fetch_california_housing()  #캘리포니아집값불러오는ㅅ함수

boston = pd.DataFrame(data=boston_data.data, columns=boston_data.feature_names) #DataFrame = 데이터처리하는기준
boston['target'] = boston_data.target #타겟 = 데이터의결과(묶어서보기위해추가)

train = boston.sample(frac=0.8, random_state=200) #frac=샘플링하는데이터의양(80%라는뜻)
test = boston.drop(train.index)

scatter_matrix(boston.drop(columns=['MedInc','HouseAge','AveRooms']))
plt.show()