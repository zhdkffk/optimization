import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

df = pd.read_csv('generator.csv')
# sns.lmplot('RPM', 'VIBRATION', data=df, hue='STATUS', fit_reg=False)
# plt.show()

train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

knn = KNeighborsClassifier(n_neighbors=2)  #클러스터 2개
knn.fit(train[['RPM', 'VIBRATION']], train['STATUS'])  #RPM, 진동을 기준으로 내 위치(status)가 나올 것이다
score = knn.score(test[['RPM', 'VIBRATION']], test['STATUS'])  #train을 test데이터한테 비교하는 거.. 예측률
# print(score)

guess = pd.DataFrame(columns=['RPM','VIBRATION'])
guess.loc[0] = [800,200] #좌표임.. 이미 클러스터가 만들어져있잖아? 그래서이걸넣으면분류해주는거
print(knn.predict(guess))

