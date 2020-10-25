import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

df = pd.read_csv('seoul.csv')
label_count = len(df['name'].unique())  #레이블이 총 몇개인지계산
# sns.lmplot('lat', 'lon', data=df, hue='name', fit_reg=False)
# plt.show()

train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

#knn구하기
knn = KNeighborsClassifier(n_neighbors=label_count)
knn.fit(train[['lat','lon']], train['name'])
score = knn.score(test[['lat', 'lon']], test['name'])
print(score)

guess = pd.DataFrame(columns=['lat','lon'])
guess.loc[0] = [37.520040, 127.110136]
# print(knn.predict(guess))