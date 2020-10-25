from sklearn.datasets import load_boston  #보스턴 집값(1960년대)
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

#데이터 시각적 표현!

boston_data = load_boston()  #보스턴집값불러오는ㅅ함수

boston = pd.DataFrame(data=boston_data.data, columns=boston_data.feature_names) #DataFrame = 데이터처리하는기준
boston['target'] = boston_data.target #타겟 = 데이터의결과(묶어서보기위해추가)

#데이터 분리하기
train = boston.sample(frac=0.8, random_state=200) #frac=샘플링하는데이터의양(80%라는뜻)
test = boston.drop(train.index)  #샘플링된 데이터들을 제외한 나머지 데이터로 검증함

scatter_matrix(boston.drop(columns=["RM","B","PTRATIO","DIS","ZN"]))  #시각적 표현
plt.show()
